"""Side-view blueprint diagrams for Link-A-Link builds, rendered as inline SVG.

Units are millimetres in "world" space (y up). Colours come from CSS classes
defined in docs/stylesheets/extra.css so the drawings follow light/dark mode.
"""
import math

ROSETTE_R = 28          # rosette (toothed joint) radius, ~55.9 mm dia
BAR_W = 26              # drawn link thickness
PIVOT_H = {             # approx height of the first pivot above the mounting surface
    "clamp": 95, "rot-clamp": 110, "round": 95, "foot": 95, "fixed-rot": 110,
    "weighted": 120, "wall": 95, "cup": 150, "rail": 85,
}


class Diagram:
    def __init__(self):
        self.items = []      # (z, svg) so we can layer
        self.pts = []        # for bounds
        self.callouts = []   # (x, y, label)

    def add(self, svg, z=1, pts=()):
        self.items.append((z, svg))
        self.pts.extend(pts)

    # ---------- primitives ----------
    def bar(self, a, b, cls="lnk", w=BAR_W):
        self.add(f'<line x1="{a[0]:.1f}" y1="{-a[1]:.1f}" x2="{b[0]:.1f}" y2="{-b[1]:.1f}" '
                 f'class="{cls}" stroke-width="{w}" stroke-linecap="round"/>', 2,
                 [(a[0]-w, a[1]-w), (b[0]+w, b[1]+w), (a[0]+w, a[1]+w), (b[0]-w, b[1]-w)])

    def joint(self, p, dots=None):
        x, y = p
        s = f'<circle cx="{x:.1f}" cy="{-y:.1f}" r="{ROSETTE_R}" class="jnt"/>'
        s += f'<circle cx="{x:.1f}" cy="{-y:.1f}" r="7" class="jnt-hole"/>'
        self.add(s, 3, [(x-ROSETTE_R, y-ROSETTE_R), (x+ROSETTE_R, y+ROSETTE_R)])

    def callout(self, p, label, dx=0, dy=0):
        self.callouts.append((p[0]+dx, p[1]+dy, label))

    # ---------- bases ----------
    def base(self, kind):
        h = PIVOT_H[kind]
        p = (0, h)
        if kind in ("clamp", "rot-clamp"):
            # desk slab (top at y=0) whose front edge is at x=-40; the clamp wraps that edge
            self.add('<rect x="-40" y="0" width="440" height="30" class="surface"/>', 0, [(-40, -30), (400, 0)])
            self.add('<path d="M 40 -14 L -62 -14 L -62 44 L 40 44 L 40 30 L -48 30 L -48 0 L 40 0 Z" class="base"/>', 1,
                     [(-62, -44), (40, 14)])
            self.add('<rect x="-4" y="44" width="8" height="26" class="base"/><rect x="-14" y="70" width="28" height="8" rx="3" class="base"/>', 1,
                     [(-14, -78), (14, -44)])
            self.bar((0, 14), (0, h), cls="base", w=40)
        elif kind in ("round", "foot"):
            self.add('<rect x="-200" y="0" width="560" height="10" class="surface"/>', 0, [(-200, -10), (360, 0)])
            self.add('<rect x="-100" y="-16" width="200" height="16" rx="6" class="base"/>', 1, [(-100, 0), (100, 16)])
            self.bar((0, 16), (0, h), cls="base", w=40)
        elif kind == "fixed-rot":
            self.add('<rect x="-200" y="0" width="560" height="28" class="surface"/>', 0, [(-200, -28), (360, 0)])
            self.add('<path d="M -36 0 L -26 -38 L 26 -38 L 36 0 Z" class="base"/>', 1, [(-36, 0), (36, 38)])
            self.bar((0, 38), (0, h), cls="base", w=40)
        elif kind == "weighted":
            self.add('<rect x="-220" y="0" width="580" height="10" class="surface"/>', 0, [(-220, -10), (360, 0)])
            self.add('<path d="M -112 0 L -100 -64 L 100 -64 L 112 0 Z" class="base"/>', 1, [(-112, 0), (112, 64)])
            self.add('<text x="0" y="-26" class="dimtxt" text-anchor="middle">ballast</text>', 4)
            self.bar((0, 64), (0, h), cls="base", w=40)
        elif kind == "wall":
            self.add('<rect x="-28" y="-420" width="28" height="560" class="surface"/>', 0, [(-28, -140), (0, 420)])
            self.add('<path d="M 0 -135 L 38 -125 L 38 -65 L 0 -55 Z" class="base"/>', 1, [(0, 55), (38, 135)])
            h = 95
            self.bar((38, h), (70, h), cls="base", w=40)
            p = (70, h)
        elif kind == "cup":
            self.add('<path d="M -140 0 L -48 0 L -48 90 L 48 90 L 48 0 L 260 0 L 260 -30 L -140 -30 Z" '
                     'class="surface"/>', 0, [(-140, -90), (260, 30)])
            self.add('<rect x="-42" y="-76" width="84" height="76" rx="8" class="base" transform="translate(0,90)"/>', 1,
                     [(-42, -90), (42, 0)])
            self.add('<text x="-60" y="60" class="dimtxt" text-anchor="end">cup holder</text>', 4, [(-200, -60)])
            h = 60
            self.bar((0, 14), (0, h), cls="base", w=40)
            p = (0, h)
        elif kind == "rail":
            self.add('<rect x="-200" y="0" width="560" height="28" class="surface"/>', 0, [(-200, -28), (360, 0)])
            self.add('<rect x="-100" y="-12" width="200" height="12" class="base"/>', 1, [(-100, 0), (100, 12)])
            self.bar((0, 12), (0, h), cls="base", w=40)
        self.joint(p)
        return p

    # ---------- chain ----------
    def chain(self, start, segs):
        """segs: list of dicts {len, ang, cls?, tag?, branch?: [segs...], payload?: (kind, ang)}"""
        p = start
        for s in segs:
            L, a = s["len"], math.radians(s["ang"])
            q = (p[0] + L*math.cos(a), p[1] + L*math.sin(a))
            if s.get("cls") == "mod":
                # modular link: bar with a lighter middle "body"
                self.bar(p, q, cls="lnk")
                ux, uy = math.cos(a), math.sin(a)
                m1 = (p[0]+ux*45, p[1]+uy*45); m2 = (q[0]-ux*45, q[1]-uy*45)
                self.bar(m1, m2, cls="mod", w=BAR_W-8)
            elif s.get("cls") == "branch":
                self.bar(p, q, cls="lnk", w=BAR_W+6)
            elif s.get("cls") == "pl":
                self.bar(p, q, cls="pl", w=BAR_W-4)
                self.add(f'<rect x="{q[0]-9:.1f}" y="{-q[1]-9:.1f}" width="18" height="18" rx="3" class="pl-end" '
                         f'transform="rotate({-s["ang"]} {q[0]:.1f} {-q[1]:.1f})"/>', 3)
            else:
                self.bar(p, q, cls=s.get("cls", "lnk"))
            if s.get("tag"):
                mid = ((p[0]+q[0])/2, (p[1]+q[1])/2)
                nx, ny = -math.sin(a), math.cos(a)
                off = s.get("tagoff", 42)
                self.callout((mid[0]+nx*off, mid[1]+ny*off), s["tag"])
            if s.get("cls") != "pl":
                self.joint(q)
            if "branch" in s:
                # branch point sits at the middle of this segment
                bp = ((p[0]+q[0])/2, (p[1]+q[1])/2) if s.get("branch_at") == "mid" else q
                if s.get("branch_at") == "mid":
                    self.joint(bp)
                for sub in s["branch"]:
                    self.chain(bp, sub)
            if "payload" in s:
                self.payload(q, *s["payload"])
            p = q
        return p

    # ---------- payload glyphs ----------
    def payload(self, p, kind, ang=0, tag=None):
        x, y = p
        t = f'transform="translate({x:.1f},{-y:.1f}) rotate({-ang})"'
        g = {
            "phone":   '<rect x="18" y="-80" width="14" height="160" rx="6" class="dev"/>',
            "tablet":  '<rect x="18" y="-130" width="14" height="260" rx="6" class="dev"/>',
            "monitor": '<rect x="22" y="-115" width="20" height="230" rx="4" class="dev"/>',
            "laptop":  '<rect x="-150" y="-62" width="300" height="14" rx="5" class="dev"/>'
                       '<rect x="-156" y="-296" width="12" height="236" rx="5" class="dev" transform="rotate(-14 -150 -60)"/>'
                       '<rect x="-12" y="-48" width="24" height="30" class="dev"/>',
            "camera":  '<rect x="-38" y="-78" width="84" height="56" rx="8" class="dev"/>'
                       '<rect x="46" y="-66" width="36" height="34" rx="6" class="dev"/>'
                       '<rect x="-4" y="-40" width="10" height="18" class="dev"/>',
            "cam-down": '<rect x="20" y="-42" width="56" height="84" rx="8" class="dev"/>'
                        '<rect x="20" y="42" width="40" height="36" rx="6" class="dev" transform="translate(8,0)"/>',
            "mic":     '<rect x="-14" y="30" width="44" height="150" rx="20" class="dev"/>',
            "light":   '<ellipse cx="34" cy="0" rx="12" ry="120" class="dev"/>',
            "clamp":   '<path d="M 18 -40 L 70 -40 L 70 -26 L 34 -26 L 34 26 L 70 26 L 70 40 L 18 40 Z" class="dev"/>',
        }[kind]
        self.add(f'<g {t}>{g}</g>', 2)
        # rough bounds
        r = {"monitor": 190, "tablet": 150, "laptop": 300, "light": 140, "mic": 190, "phone": 100}.get(kind, 110)
        self.pts.extend([(x-r, y-r), (x+r, y+r)])
        if tag:
            self.callout((x, y), tag, dx=0, dy=-50)

    # ---------- dimension ----------
    def dim_h(self, x1, x2, y, text):
        self.add(f'<line x1="{x1:.1f}" y1="{-y:.1f}" x2="{x2:.1f}" y2="{-y:.1f}" class="dim" marker-start="url(#ar)" marker-end="url(#ar)"/>'
                 f'<text x="{(x1+x2)/2:.1f}" y="{-y+26:.1f}" class="dimtxt" text-anchor="middle">{text}</text>', 5,
                 [(x1, y-40), (x2, y+10)])

    def dim_v(self, x, y1, y2, text):
        self.add(f'<line x1="{x:.1f}" y1="{-y1:.1f}" x2="{x:.1f}" y2="{-y2:.1f}" class="dim" marker-start="url(#ar)" marker-end="url(#ar)"/>'
                 f'<text x="{x+10:.1f}" y="{-(y1+y2)/2:.1f}" class="dimtxt" dominant-baseline="middle">{text}</text>', 5,
                 [(x-10, y1), (x+120, y2)])

    def render(self, title=""):
        xs = [p[0] for p in self.pts]; ys = [p[1] for p in self.pts]
        k = max(0.85, min(1.7, max(max(xs)-min(xs), max(ys)-min(ys)) / 720))
        for (x, y, lab) in self.callouts:
            r = 17*k
            self.add(f'<circle cx="{x:.1f}" cy="{-y:.1f}" r="{r:.1f}" class="co"/>'
                     f'<text x="{x:.1f}" y="{-y:.1f}" class="cotxt" font-size="{19*k:.1f}" text-anchor="middle" dominant-baseline="central">{lab}</text>',
                     9, [(x-r-3, y-r-3), (x+r+3, y+r+3)])
        xs = [p[0] for p in self.pts]; ys = [p[1] for p in self.pts]
        pad = 30
        minx, maxx = min(xs)-pad, max(xs)+pad
        miny, maxy = min(ys)-pad, max(ys)+pad
        w, h = maxx-minx, maxy-miny
        body = "".join(s for _, s in sorted(self.items, key=lambda t: t[0]))
        body = body.replace('class="dimtxt"', f'class="dimtxt" font-size="{21*k:.1f}"')
        return (f'<svg class="bp" viewBox="{minx:.0f} {-maxy:.0f} {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg" '
                f'role="img" aria-label="{title}">'
                '<defs><pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">'
                '<path d="M 50 0 L 0 0 0 50" class="gridln"/></pattern>'
                '<marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                '<path d="M 0 0 L 10 5 L 0 10 z" class="arrow"/></marker></defs>'
                f'<rect x="{minx:.0f}" y="{-maxy:.0f}" width="{w:.0f}" height="{h:.0f}" fill="url(#grid)" class="bpbg"/>'
                f'{body}</svg>')


def joint_anatomy_svg():
    """Exploded side view of one joint: screw | cone washer | link A | link B | nut."""
    return '''<svg class="bp" viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Joint anatomy">
<defs><pattern id="grid2" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" class="gridln"/></pattern></defs>
<rect width="760" height="260" fill="url(#grid2)" class="bpbg"/>
<line x1="40" y1="130" x2="720" y2="130" class="dim" stroke-dasharray="6 6"/>
<!-- screw -->
<rect x="60" y="92" width="16" height="76" rx="3" class="base"/>
<rect x="76" y="118" width="120" height="24" rx="4" class="base"/>
<path d="M 100 118 l 6 24 M 116 118 l 6 24 M 132 118 l 6 24 M 148 118 l 6 24 M 164 118 l 6 24 M 180 118 l 6 24" class="thread"/>
<text x="120" y="200" class="lbl" text-anchor="middle">T-head screw</text><text x="120" y="216" class="lbl small" text-anchor="middle">turn this to tighten</text>
<!-- washer -->
<path d="M 236 100 L 262 82 L 262 178 L 236 160 Z" class="base"/>
<text x="250" y="215" class="lbl" text-anchor="middle">cone washer</text><text x="250" y="231" class="lbl small" text-anchor="middle">keyed to the screw</text>
<!-- link A -->
<rect x="300" y="72" width="34" height="116" rx="8" class="lnk-fill"/>
<path d="M 334 78 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6" class="teeth"/>
<text x="318" y="60" class="lbl" text-anchor="middle">link end "2" (●●)</text>
<!-- link B -->
<rect x="392" y="72" width="34" height="116" rx="8" class="lnk-fill"/>
<path d="M 392 78 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6" class="teeth"/>
<text x="410" y="228" class="lbl" text-anchor="middle">link end "1" (●)</text>
<text x="364" y="30" class="lbl strong" text-anchor="middle">teeth mesh → locks angle</text>
<!-- nut -->
<path d="M 470 96 L 500 84 L 530 84 L 530 176 L 500 176 L 470 164 Z" class="base"/>
<text x="500" y="215" class="lbl" text-anchor="middle">threaded nut</text><text x="500" y="231" class="lbl small" text-anchor="middle">tabs lock it in the keyway</text>
<!-- tool -->
<circle cx="640" cy="130" r="48" class="base" fill-opacity=".35"/>
<circle cx="640" cy="130" r="18" class="bpbg-fill"/>
<text x="640" y="205" class="lbl" text-anchor="middle">Link-A-Link tool</text>
<text x="640" y="222" class="lbl small" text-anchor="middle">(tightening aid)</text>
</svg>'''
