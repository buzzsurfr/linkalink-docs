#!/usr/bin/env python3
"""Generate the data-driven pages of the Link-A-Link Field Guide.

Run from the project root:  python gen/build.py
Writes: docs/parts/**, docs/blueprints/<slug>.md + index, docs/reference/file-index.md,
        docs/reference/print-plates.md, docs/guide/how-it-works.md, docs/guide/printing.md
"""
import json, math, os, sys
from collections import OrderedDict

GEN = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(GEN)
DOCS = os.path.join(ROOT, "docs")
sys.path.insert(0, GEN)

from parts import FAMILIES                      # noqa: E402
from blueprints import BLUEPRINTS               # noqa: E402
from bpsvg import blueprint_svg                 # noqa: E402
from diagram import joint_anatomy_svg           # noqa: E402

THREEMF = json.load(open(os.path.join(GEN, "threemf.json")))
DIMS = OrderedDict(l.rstrip("\n").split("\t") for l in open(os.path.join(GEN, "stl_dims.tsv")) if l.strip())

SECTION_TITLES = {"bases": "Base Mounts", "links": "Links", "payloads": "Payload Mounts"}
SECTION_ICONS = {"bases": ":material-desk:", "links": ":material-link-variant:", "payloads": ":material-cellphone-link:"}


def write(rel, text):
    p = os.path.join(DOCS, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(text.strip() + "\n")


def tier_badge(t):
    return {"std": '<span class="tier std">Standard</span>', "ult": '<span class="tier ult">Ultimate</span>'}.get(t, "")


def plates_html(plates, depth):
    up = "../" * depth
    out = ['<div class="plates">']
    for img, cap, sub in plates:
        out.append(f'<figure><img src="{up}assets/renders/{img}.webp" alt="{cap}" loading="lazy">'
                   f'<figcaption>{cap}{f"<small>{sub}</small>" if sub else ""}</figcaption></figure>')
    out.append("</div>")
    return "\n".join(out)


def files_table(folders):
    rows = []
    for path, dim in DIMS.items():
        for fo in folders:
            if path.startswith(fo):
                rows.append((path[len(fo):], dim))
    t = ["| File | Size as printed (X × Y × Z mm) |", "|---|---|"]
    t += [f"| `{f}` | {d} |" for f, d in rows]
    return "\n".join(t)


# ------------------------------------------------------------------ parts pages
def build_parts():
    for fam in FAMILIES:
        folders = fam["folder"]
        md = ["---", f"title: \"{fam['title']}\"", "---", "", f"# {fam['title']} {tier_badge(fam['tier'])}", "", f"*{fam['summary']}*", ""]
        md.append("!!! abstract \"Where it lives\"")
        for fo in folders:
            md.append(f"    `{fo}`  ")
        md.append(f"    **3MF:** {', '.join('`'+x+'`' for x in fam['threemf'])}  ")
        md.append(f"    **Buy:** {fam['buy']}")
        md.append("")
        md.append(plates_html(fam["plates"], 2))
        md.append(fam["body"].strip())
        md.append("")
        md.append("## Files")
        md.append("")
        md.append(files_table(folders))
        # blueprints that use it
        used = []
        for bp in BLUEPRINTS:
            blob = json.dumps(bp["bom"])
            if any(fo in blob for fo in folders):
                used.append(bp)
        if used:
            md += ["", "## Used in blueprints", ""]
            md += [f"* [{bp['n']}. {bp['title']}](../../blueprints/{bp['slug']}.md)" for bp in used]
        write(f"parts/{fam['section']}/{fam['slug']}.md", "\n".join(md))

    # catalog index
    md = ["# Parts Catalog", "",
          "Every component family in the v1.4 Ultimate library, grouped the way the download is. "
          "Each page has plate previews from the supplied 3MFs, sizes, variants, assembly notes and the exact files.", ""]
    for sec in ("bases", "links", "payloads"):
        md += [f"## {SECTION_ICONS[sec]} {SECTION_TITLES[sec]}", "", "| Family | Tier | What it's for |", "|---|---|---|"]
        for fam in [f for f in FAMILIES if f["section"] == sec]:
            md.append(f"| [{fam['title']}]({sec}/{fam['slug']}.md) | {tier_badge(fam['tier'])} | {fam['summary']} |")
        md.append("")
    md += ["## The tool", "",
           "`0. Start Here/LINK A LINK - TOOL.STL` (67.6 mm Ø, 12.7 mm thick) is a printed wrench for the threaded nuts and screw heads. "
           "It gives you the last bit of torque on a joint without chewing up the nut. Print one first."]
    write("parts/index.md", "\n".join(md))


# ------------------------------------------------------------------ blueprints
def bom_table(bp):
    rows = ["| Key | Qty | File · folder |", "|---|---|---|"]
    for key, items in bp["bom"]:
        k = f'<span class="callout-key">{key}</span>' if len(key) == 1 else f"**{key}**"
        first = True
        for qty, fname, folder in items:
            rows.append(f'| {k if first else ""} | {qty} | `{fname}`<br><span class="folder">{folder}</span> |')
            first = False
    return "\n".join(rows)


def build_blueprints():
    cards = []
    for bp in BLUEPRINTS:
        svg, dx, h = blueprint_svg(bp)
        joints = sum(q for key, items in bp["bom"] if key.startswith("Joints") for q, f, _ in items if "Screw" in f)
        md = [f"# {bp['n']}. {bp['title']}", "", f"*{bp['tagline']}*", "",
              '<div class="spec">',
              f'<div><b>Payload</b><span>{bp["payload"]}</span></div>',
              f'<div><b>Tier</b><span>{bp["tier"]}</span></div>',
              f'<div><b>Difficulty</b><span>{bp["difficulty"]}</span></div>',
              f'<div><b>Material</b><span>{bp["material"]}</span></div>',
              f'<div><b>Reach · Height</b><span>≈ {abs(dx):.0f} mm · ≈ {h:.0f} mm</span></div>',
              f'<div><b>Link joints</b><span>{joints} hardware sets</span></div>',
              "</div>", "",
              svg, "",
              "<small>Side view, to scale from link pitch lengths. Reach is measured from the first pivot; "
              "height from the mounting surface. Numbers are geometric estimates.</small>", "",
              "## Key", ""]
        md += [f'<span class="callout-key">{k}</span> {v}  ' for k, v in bp["callouts"]]
        md += ["", "## Print list", "", bom_table(bp), "",
               f"**Print profile:** {bp['profile']}", "",
               "## Buy", ""]
        md += [f"* {b}" for b in bp["buy"]]
        md += ["", "## Assemble", ""]
        md += [f"{i}. {s}" for i, s in enumerate(bp["steps"], 1)]
        md += ["", "!!! tip \"Tips\""]
        md += [f"    * {t}" for t in bp["tips"]]
        md += ["", "## Variations", ""]
        md += [f"* {v}" for v in bp["variants"]]
        write(f"blueprints/{bp['slug']}.md", "\n".join(md))
        cards.append((bp, svg))

    md = ["---", "hide:", "  - toc", "---", "", "# Blueprints", "",
          "Complete, printable configurations: the setups from the product page plus a few more, "
          "each with a scale side-view, a full print list with folder paths, bought hardware, and assembly order.", "",
          "!!! info \"How to read a blueprint\"",
          "    **Orange letters** in the drawing match the **Key** and **Print list**. Gray bars are Standard Links, "
          "lighter bars are Modular Link bodies, **orange bars** are Payload Links. Circles are toothed joints; each one needs a link hardware set.",
          "", '<div class="grid cards" markdown>', ""]
    for bp, svg in cards:
        md += [f"-   **[{bp['n']}. {bp['title']}]({bp['slug']}.md)**", "", "    ---", "",
               f"    {svg}", "",
               f"    {bp['payload']}  ", f"    *{bp['difficulty']} · {bp['tier']}*", ""]
    md += ["</div>", "", "Want something else? Use [Design your own](design-your-own.md)."]
    write("blueprints/index.md", "\n".join(md))


# ------------------------------------------------------------------ reference
def build_reference():
    md = ["# File Index", "",
          "All 192 STL files in the v1.4 library with their **measured** bounding boxes (as oriented in the file, i.e. as printed). "
          "Useful for checking bed fit and for spotting variants.", "",
          "!!! note",
          "    `2. Links/.../Modular Link/HARDWARE/` and `.../Standard Links/HARDWARE/` contain identical copies of the link hardware.", ""]
    cur = None
    for path, dim in DIMS.items():
        folder, fname = os.path.split(path)
        if folder != cur:
            md += ["", f"### `{folder}/`", "", "| File | X × Y × Z (mm) |", "|---|---|"]
            cur = folder
        md.append(f"| `{fname}` | {dim} |")
    write("reference/file-index.md", "\n".join(md))

    # print plates
    md = ["# Print Plates", "",
          "Every plate in every supplied 3MF project, with its preview and contents. Open the 3MF in Bambu Studio or OrcaSlicer and print a plate as-is.", ""]
    for t in THREEMF:
        sup = "all parts" if t["supports_global"] else (", ".join(f"`{s}`" for s in t["supports_parts"]) or "none")
        md += [f"## {os.path.basename(t['path'])[:-4]}", "",
               f"`{t['path']}`  ",
               f"**Profile:** {t['profile']} · {t['layer']} mm · {t['walls']} walls · {t['infill']} infill · **Supports:** {sup}", "",
               '<div class="plates">']
        for p in t["plates"]:
            parts = ", ".join(f"{q}× {n.replace('.STL', '')}" if q > 1 else n.replace('.STL', '') for n, q in p["parts"].items())
            md.append(f'<figure><img src="../assets/renders/{p["img"]}.webp" alt="{p["name"]}" loading="lazy">'
                      f'<figcaption>{p["n"]}. {p["name"]}<small>{parts}</small></figcaption></figure>')
        md += ["</div>", ""]
    write("reference/print-plates.md", "\n".join(md))


def build_templates():
    t = open(os.path.join(GEN, "templates", "how-it-works.md")).read()
    write("guide/how-it-works.md", t.replace("{{JOINT_SVG}}", joint_anatomy_svg().replace("\n", "")))
    rows = ["| 3MF project | Plates | Layer | Walls | Infill | Supports |", "|---|---|---|---|---|---|"]
    for x in THREEMF:
        sup = "all" if x["supports_global"] else (", ".join(s.replace(".STL", "") for s in x["supports_parts"]) or "—")
        rows.append(f"| `{os.path.basename(x['path'])}` | {len(x['plates'])} | {x['layer']} | {x['walls']} | {x['infill']} | {sup} |")
    rows.append("")
    rows.append("See every plate with previews on [Print Plates](../reference/print-plates.md).")
    # engineering notes
    masses = json.load(open(os.path.join(GEN, "masses.json")))
    rows_m = ["| Part | PLA+ · 4 walls · 20 % | PETG · 6 walls · 40 % |", "|---|---|---|"]
    names = [("Standard Link 125", "link125"), ("Standard Link 200", "link200"), ("Standard Link 275", "link275"),
             ("Payload Link 50", "pl50"), ("Swivel Payload Link (all parts)", "swivel"),
             ("Modular Link ends (2 joints + braces + washers)", "modends"), ("Modular Link body 200", "body200"),
             ("3-Way Branch Link", "branch3"), ("4-Way Branch Link", "branch4"), ("Link hardware set (screw + washer + nut)", "hw"),
             ("Weighted Base Large (empty)", "wb_L"), ("Round Base 200", "round200")]
    for label, k in names:
        rows_m.append(f"| {label} | {masses['pla'][k]:.0f} g | {masses['petg'][k]:.0f} g |")
    t = open(os.path.join(GEN, "templates", "engineering.md")).read()
    t = t.replace("{{RAIL_SVG}}", open(os.path.join(GEN, "templates", "rail-svg.html")).read().replace("\n", "").strip())
    t = t.replace("{{MASS_TABLE}}", "\n".join(rows_m))
    write("reference/engineering.md", t)
    t = open(os.path.join(GEN, "templates", "printing.md")).read()
    write("guide/printing.md", t.replace("{{PROFILE_TABLE}}", "\n".join(rows)))


def build_nav():
    fam = lambda sec: "\n".join(f"          - parts/{sec}/{f['slug']}.md" for f in FAMILIES if f["section"] == sec)
    bps = "\n".join(f"      - blueprints/{bp['slug']}.md" for bp in BLUEPRINTS)
    nav = f"""nav:
  - Home: index.md
  - Guide:
      - guide/index.md
      - guide/how-it-works.md
      - guide/printing.md
      - guide/materials.md
      - guide/hardware.md
      - guide/assembly.md
  - Blueprints:
      - blueprints/index.md
{bps}
      - blueprints/design-your-own.md
      - blueprints/load-calculator.md
  - Parts:
      - parts/index.md
      - Base Mounts:
{fam('bases')}
      - Links:
{fam('links')}
      - Payload Mounts:
{fam('payloads')}
  - Reference:
      - reference/engineering.md
      - reference/community.md
      - reference/kickstarter.md
      - reference/file-index.md
      - reference/print-plates.md
      - reference/update-log.md
      - reference/about.md
"""
    y = open(os.path.join(ROOT, "mkdocs.yml")).read()
    y = y.split("nav:")[0].rstrip() + "\n\n" + nav
    open(os.path.join(ROOT, "mkdocs.yml"), "w").write(y)


if __name__ == "__main__":
    build_parts()
    build_blueprints()
    build_reference()
    build_templates()
    build_nav()
    print("generated pages OK")
