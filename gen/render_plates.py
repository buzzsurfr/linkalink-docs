"""Render every plate in every 3MF from the mesh geometry (our own renders, no creator thumbnails).

Usage: python render_plates.py <library_root> <out_dir> [slug_filter]
"""
import sys, os, re, zipfile, json
import numpy as np
import xml.etree.ElementTree as ET
import trimesh
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

NS = {'m': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
PNS = '{http://schemas.microsoft.com/3dmanufacturing/production/2015/06}path'
BASE = np.array([0.56, 0.62, 0.68])      # blue-grey, readable on light and dark
ACC = np.array([0.91, 0.64, 0.24])
LIGHT = np.array([-0.4, -0.6, 0.75]); LIGHT /= np.linalg.norm(LIGHT)


def T(s):
    a = list(map(float, s.split())); M = np.eye(4); M[:3, :3] = np.array(a[:9]).reshape(3, 3); M[3, :3] = a[9:]
    return M


def load_plates(path):
    z = zipfile.ZipFile(path)
    root = ET.fromstring(z.read('3D/3dmodel.model'))
    ms = ET.fromstring(z.read('Metadata/model_settings.config'))
    comps = {}
    for o in root.find('m:resources', NS).findall('m:object', NS):
        c = o.find('m:components', NS)
        if c is not None:
            comps[o.get('id')] = [(x.get(PNS), x.get('objectid'), x.get('transform')) for x in c.findall('m:component', NS)]
    build = {it.get('objectid'): T(it.get('transform')) for it in root.find('m:build', NS).findall('m:item', NS)}
    cache = {}

    def mesh(p, oid):
        key = (p, oid)
        if key not in cache:
            r = ET.fromstring(z.read(p.lstrip('/')))
            for o in r.iter('{%s}object' % NS['m']):
                if o.get('id') == oid:
                    v = np.array([[float(x.get(k)) for k in 'xyz'] for x in o.find('.//m:vertices', NS)])
                    f = np.array([[int(x.get(k)) for k in ('v1', 'v2', 'v3')] for x in o.find('.//m:triangles', NS)])
                    cache[key] = (v, f)
        return cache[key]

    plates = []
    for p in ms.findall('plate'):
        md = {m.get('key'): m.get('value') for m in p.findall('metadata')}
        objs = [i.find("metadata[@key='object_id']").get('value') for i in p.findall('model_instance')]
        meshes = []
        for oid in objs:
            M = build[oid]
            for path_, cid, ct in comps.get(oid, []):
                v, f = mesh(path_, cid)
                V = np.c_[v, np.ones(len(v))] @ (T(ct) if ct else np.eye(4)) @ M
                meshes.append(trimesh.Trimesh(V[:, :3], f, process=False))
        plates.append((int(md['plater_id']), meshes))
    return plates


def render(meshes, out, faces_budget=60000, size=6.0):
    m = trimesh.util.concatenate(meshes)
    m.merge_vertices()
    if len(m.faces) > faces_budget:
        try:
            import fast_simplification
            v, f = fast_simplification.simplify(m.vertices.astype(np.float32), m.faces.astype(np.int32), target_reduction=1 - faces_budget / len(m.faces))
            m = trimesh.Trimesh(v, f, process=False)
        except Exception:
            pass
    V = m.vertices - m.bounds.mean(0)
    tri = V[m.faces]
    n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    nl = np.linalg.norm(n, axis=1); keep = nl > 1e-9
    tri, n = tri[keep], n[keep] / nl[keep][:, None]
    shade = 0.35 + 0.65 * np.clip(n @ LIGHT, 0, 1)
    cols = np.clip(BASE[None, :] * shade[:, None] * 1.15, 0, 1)
    fig = plt.figure(figsize=(size, size), dpi=100)
    ax = fig.add_subplot(111, projection='3d', proj_type='ortho')
    pc = Poly3DCollection(tri, facecolors=cols, edgecolors='none', linewidths=0)
    ax.add_collection3d(pc)
    r = np.ptp(V, axis=0).max() * 0.5
    ax.set_xlim(-r, r); ax.set_ylim(-r, r); ax.set_zlim(-r, r)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=32, azim=-55)
    ax.set_axis_off()
    fig.subplots_adjust(0, 0, 1, 1)
    fig.savefig(out, transparent=True)
    plt.close(fig)


if __name__ == '__main__':
    lib, outdir = sys.argv[1], sys.argv[2]
    filt = sys.argv[3] if len(sys.argv) > 3 else ''
    os.makedirs(outdir, exist_ok=True)
    import glob
    for f in sorted(glob.glob(os.path.join(lib, '**/*.3mf'), recursive=True)):
        slug = re.sub(r'[^A-Za-z0-9]+', '-', os.path.basename(f)[:-4]).strip('-').lower()
        if filt and filt not in slug:
            continue
        for pid, meshes in load_plates(f):
            out = os.path.join(outdir, f'{slug}__p{pid}.png')
            render(meshes, out)
            print(out, flush=True)
