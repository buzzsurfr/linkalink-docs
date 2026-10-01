# Link-A-Link Field Guide (unofficial)

Community documentation for the **Link-A-Link** 3D-printable modular arm system by [3D Printing Builds](https://3dprintingbuilds.com/link-a-link/): getting-started guide, parts catalog, 10 build blueprints, a load calculator, and engineering notes measured from the part geometry.

**Live site:** https://linkalink-docs.netlify.app/

> **Not affiliated with 3D Printing Builds.** This repo does **not** contain any Link-A-Link STL/3MF files or the creator's photos and renders. Buy the library from the creator. Images here are drawn from scratch or rendered from geometry by `gen/render_plates.py`.

## Run it locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python gen/build.py     # regenerate data-driven pages
mkdocs serve            # http://127.0.0.1:8000
```

## How it's built

* **MkDocs Material**. Config in `mkdocs.yml`; hand-written pages in `docs/`.
* **Generated pages** come from data in `gen/` (run `python gen/build.py`, which Netlify also runs on every deploy):

| Data / template | Generates |
|---|---|
| `gen/parts.py` | `docs/parts/**` |
| `gen/blueprints.py` + `gen/diagram.py` | `docs/blueprints/<slug>.md` + index (scale SVG side-views) |
| `gen/templates/*.md` | `docs/guide/how-it-works.md`, `docs/guide/printing.md`, `docs/reference/engineering.md` |
| `gen/stl_dims.tsv`, `gen/stl_volumes.tsv`, `gen/threemf.json`, `gen/masses.json` | File index, print plates, mass tables, calculator data |

> Edit the **sources in `gen/`**, not the generated `.md` files; those get overwritten on the next build.

* **Renders** in `docs/assets/renders/` are produced from your own copy of the library:

  ```bash
  pip install trimesh fast-simplification matplotlib numpy
  python gen/render_plates.py "/path/to/Link-A-Link Boom Arm" /tmp/renders
  # then convert to 480px .webp into docs/assets/renders/ (see gen/render_plates.py)
  ```

## Deploy

Netlify builds from `main` using `netlify.toml`:

```
pip install -r requirements.txt && python gen/build.py && mkdocs build --strict  →  publish site/
```

## Adding a blueprint

Append a `dict(...)` to `BLUEPRINTS` in `gen/blueprints.py`. `segs` is the chain from the base. Each segment has `len` (pitch in mm) and `ang` (degrees: 0 = level, 90 = up). Set `cls="pl"` for a payload link, `cls="mod"` for a Modular Link, or `cls="branch"` with `branch=[[...]]` for a Branch Link. `payload=(kind, angle, key)` draws the device: `phone, tablet, monitor, laptop, camera, cam-down, mic, light, clamp`.

## Contributing

Corrections and measurements from real prints are welcome: open an issue or PR. Anything inferred rather than measured is marked **Inferred** on the site.
