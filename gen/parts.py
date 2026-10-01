"""Parts catalog data. Each family becomes one page under docs/parts/<section>/<slug>.md"""

STD = "std"
ULT = "ult"

FAMILIES = [
    # ============================ BASES ============================
    dict(section="bases", slug="c-clamps", title="C-Clamp Mounts", tier=STD,
         folder=["1. Base Mounts/Clamp Mounts/Fixed C-Clamp Mount/", "1. Base Mounts/Clamp Mounts/Rotating C-Clamp Mount/"],
         summary="Clamp an arm to a desk, shelf or workbench edge without drilling. Two styles, five opening sizes each.",
         body="""
## Fixed vs Rotating

| | **Fixed C-Clamp** | **Rotating C-Clamp** |
|---|---|---|
| Arm rotation at the base | None (the first joint's rosette is part of the clamp) | Base Link Joint spins in the clamp body; a printed **Set Screw** locks it |
| Parts per build | Base, 60 mm Screw, Round Pad | Base, 60 mm Screw, Base Link Joint, Set Screw |
| Best for | Arms that stay put: webcam, starter arm | Arms you swing away: mic boom, laptop, overhead rig |
| Footprint | 151–191 × 82.5 mm, 38 mm tall | 102–142 × 95 mm, 76 mm tall |

## Pick the opening size

The number in the filename is the **clamp opening**, i.e. the maximum thickness of the surface it grips.

| Your desk / shelf thickness | Print |
|---|---|
| up to ~40 mm | `Base 40mm` |
| 40–50 mm | `Base 50mm` |
| 50–60 mm | `Base 60mm` |
| 60–70 mm | `Base 70mm` |
| 70–80 mm | `Base 80mm` |

!!! tip "Pick the smallest opening that fits"
    The 60 mm clamp screw has a limited throw. The smallest opening that fits leaves the most thread for clamping and keeps the lever arm short.

!!! warning "Filename quirk"
    Inside the Fixed C-Clamp 3MF the objects are labelled `Base 40cm … 80cm`. They are the same **mm** parts as the STLs.

## Assembly

1. Thread the **Screw 60mm** up through the bottom jaw. On the Fixed clamp, press the **Round Pad** onto its tip so it doesn't mark the desk.
2. Slide the clamp onto the desk edge and tighten by hand.
3. *Rotating clamp only:* drop the **Base Link Joint** into the top of the clamp body, turn it to the direction you want, then tighten the **Set Screw** to lock it (or leave it loose for a free-swinging base).
4. Attach your first link to the clamp's rosette with one link hardware set.

!!! tip "Round Pad on the Rotating clamp"
    The Round Pad is only packaged with the Fixed clamp, but both clamps use an identical 60 mm screw, so print a pad for the Rotating clamp too. And don't crank it: a backer's PETG clamp cracked at the inner curve from over-tightening.
""",
         plates=[("desk-fixed-c-clamp-collection-40-80mm__p3", "Fixed C-Clamp: 40 mm opening", "Base + 60 mm screw + round pad"),
                 ("desk-fixed-c-clamp-collection-40-80mm__p1", "Fixed C-Clamp: 80 mm opening", "one plate per size (5)"),
                 ("rotating-c-clamp-collection-40-80mm__p1", "Rotating C-Clamp: 40 mm", "Base + screw + link joint + set screw"),
                 ("rotating-c-clamp-collection-40-80mm__p5", "Rotating C-Clamp: 80 mm", "one plate per size (5)")],
         threemf=["Desk Fixed C-Clamp Collection (40-80mm).3mf", "Rotating C-Clamp Collection (40-80mm).3mf"],
         buy="Nothing.",
         ),
    dict(section="bases", slug="desk-bases", title="Desk Bases (Round & Foot)", tier=STD,
         folder=["1. Base Mounts/Desk Mounts/"],
         summary="Free-standing footprints for light payloads, or screw-down bases for a permanent install. No clamp required.",
         body="""
## What's in the folder

| Part | Sizes | Notes |
|---|---|---|
| **Round Base** | 180 / 200 / 220 / 240 mm Ø | Disc footprint, 37.6 mm tall |
| **Foot Base** | 200 / 220 / 240 mm | Fan/teardrop footprint. Point the long side **under the payload** |
| **Desk Mount - Base Link Joint** | 1 | The rosette joint that stands on the base |
| **Desk Mount - Screw / Washer** | 1 each | Fixes the Link Joint to the base from below |

Both footprints share the same Link Joint, screw and washer (plate 8 of the collection 3MF).

## Choosing a footprint

* **Round** when the arm will be rotated in all directions.
* **Foot** when the arm always leans one way (tablet over a desk, a light off to one side). The long lobe goes under the load.
* Bigger is more stable. These bases work by footprint alone, so for anything past a phone or webcam, look at the **Weighted Base** or a clamp.

## Assembly

1. Put the washer on the screw, pass it up through the underside of the base, and thread it into the Base Link Joint.
2. Snug it with the tool; the joint should not spin on the base.
3. Add rubber feet or a strip of non-slip mat under the base if it walks on the desk.
""",
         plates=[("base-mount-desk-base-collection__p1", "Foot Base: 200 mm", ""),
                 ("base-mount-desk-base-collection__p4", "Round Base: 180 mm", ""),
                 ("base-mount-desk-base-collection__p7", "Round Base: 240 mm", ""),
                 ("base-mount-desk-base-collection__p8", "Link Joint & Hardware", "shared by all desk bases")],
         threemf=["Base Mount - Desk Base Collection.3mf"],
         buy="Optional: rubber feet / non-slip pad.",
         ),
    dict(section="bases", slug="fixed-rotating-base", title="Fixed Rotating Base", tier=ULT,
         folder=["1. Base Mounts/Desk Mounts/Fixed Rotating Base/"],
         summary="A compact screw-down socket. The link joint rotates in it and a set screw locks it. The strongest desk-surface mount in the library.",
         body="""
![Fixed Rotating Base parts](../../assets/renders/fixed-rotating-base__p1.webp){ width="300" align=right .hero-img }

Added in **v1.3**. The base is a 70.7 mm Ø cone that you screw to the desk surface (three countersunk holes).
The **Base Link Joint** sits in the cup and rotates freely until you tighten the side **Set Screw**.

**Parts:** Base, Base Link Joint, Set Screw (plate 1) + Desk Mount Screw & Washer (plate 2: the same ones used by the Desk Bases).

## Assembly

1. Seat the **Base Link Joint** in the cup of the Base.
2. From underneath, pass the Desk Mount **Screw** through its cone **Washer** and up into the Link Joint. It holds the joint captive. Tighten until the joint turns smoothly without wobble. (Do this **before** the base goes on the desk: the screw head sits on the underside.)
3. Screw the Base to the desk with 3 wood screws.
4. Thread in the side **Set Screw** to lock rotation when needed.

!!! note "Print profile"
    The supplied 3MF for this part uses Bambu's *0.28 mm Extra Draft* profile (2 walls, 15 % infill). For a base that carries a whole arm, bump it to the general guide: **4+ walls, 20 %+ infill**.

<div style="clear:both"></div>
""",
         plates=[("fixed-rotating-base__p1", "Fixed Rotating Desk Mount", "Link joint, base, set screw"),
                 ("fixed-rotating-base__p2", "Hardware", "Desk Mount screw + washer")],
         threemf=["Fixed Rotating Base.3mf"],
         buy="3× wood screws (countersunk), length to suit your desktop.",
         ),
    dict(section="bases", slug="wall-mount", title="Fixed Wall Mount", tier=ULT,
         folder=["1. Base Mounts/Wall Mounts/Fixed Wall Mount/"],
         summary="Anchor an arm to a wall, cabinet side or stud, with a printable drilling template.",
         body="""
**Parts:** Fixed Base, Base Link Joint, Screw, Washer, and a 1.3 mm **Hole Pattern Template**.

## Install

1. Print the **Hole Pattern Template** (its own plate, takes minutes).
2. Tape it to the wall, check it with a level, and mark the holes.
3. Drill and fit anchors suitable for the wall (drywall anchors, masonry plugs, or straight into a stud).
4. Screw the **Fixed Base** to the wall.
5. Fix the **Base Link Joint** to the base with the Screw + Washer.

!!! warning "Walls carry lever arms, not just weight"
    A 400 g tablet 350 mm from the wall pulls on the top screws much harder than its weight suggests. Hit a stud if you can; otherwise use anchors rated well above the payload.
""",
         plates=[("fixed-wall-mount__p1", "Hole Pattern Template", "print first"),
                 ("fixed-wall-mount__p2", "Wall Mount Assembly", "Base, link joint, screw, washer")],
         threemf=["Fixed Wall Mount.3mf"],
         buy="Wall anchors + screws (see [Hardware](../../guide/hardware.md#wall-anchors)).",
         ),
    dict(section="bases", slug="weighted-base", title="Weighted Bases", tier=ULT,
         folder=["1. Base Mounts/Weighted Bases/"],
         summary="Hollow bases you fill with ballast. Free-standing stability for bigger arms, with no clamp and no holes.",
         body="""
| Size | Footprint | Height |
|---|---|---|
| Small | 125 mm | 63.5 mm |
| Medium | 175 mm | 63.5 mm |
| Large | 225 mm | 63.5 mm |

**Shared parts (plate 4):** Base Link Joint, Screw, Washer, **Plug**.

## Filling

1. Print the base (3 walls / 20 % is fine; the ballast does the work).
2. Fill through the plug hole with **dry sand, steel shot, BBs or lead-free fishing weights**. Tap the base to settle it and top up.
3. Close the hole with the printed **Plug** (a dab of glue makes it permanent).
4. Fix the Base Link Joint with the Screw + Washer.

## How much ballast?

Cavity volumes estimated from cross-sections of the STLs (see [Engineering Notes](../../reference/engineering.md#mass-of-printed-parts)):

| Base | Cavity ≈ | Dry sand ≈ | Steel BBs / shot ≈ |
|---|---|---|---|
| Small 125 | 0.3 L | 0.45 kg | 1.4 kg |
| Medium 175 | 0.75 L | 1.1 kg | 3.4 kg |
| Large 225 | 1.3 L | 2.0 kg | 5.9 kg |

The campaign suggests “sand, steel BBs, etc.” The fill hole is on the side wall and appears threaded for the printed Plug.

!!! tip "How big?"
    Rule of thumb: the base's radius should be at least ⅓ of the arm's horizontal reach, and heavier is always better.
    Small → phone/webcam; Medium → mic, light; Large → tablet arm, creator rig. The [Load Calculator](../../blueprints/load-calculator.md) runs a tip-over check.
""",
         plates=[("weighted-base__p1", "Weighted Base: 125 mm", ""), ("weighted-base__p2", "Weighted Base: 175 mm", ""),
                 ("weighted-base__p3", "Weighted Base: 225 mm", ""), ("weighted-base__p4", "Link Joint & Hardware", "joint, screw, washer, plug")],
         threemf=["Weighted Base.3mf"],
         buy="Ballast: sand, steel shot or BBs.",
         ),
    dict(section="bases", slug="cup-holder", title="Cup Holder Mount", tier=ULT,
         folder=["1. Base Mounts/Vehicle Mounts/Cup Holder Mount/"],
         summary="A plug that drops into a car (or desk-organizer) cup holder and gives you a link joint on top.",
         body="""
| Print | Fits a cup holder about |
|---|---|
| `Base 80mm` | 80 mm Ø |
| `Base 85mm` | 85 mm Ø |
| `Base 90mm` | 90 mm Ø |
| `Base 95mm` | 95 mm Ø |

Each 3MF plate is a complete kit: Base, Base Link Joint, Screw, Washer.

Measure the cup holder's inside diameter **near the top** and print the size that equals it or sits just under. If it rattles, add a wrap of felt tape.
v1.1 fixed this part's STL print orientation, so print it the way it's supplied.

!!! danger "Car interiors get hot"
    A car parked in the sun can go well past 60 °C inside, and PLA+ softens around there. Print vehicle parts in **ASA/ABS** (best) or **PETG** (minimum). See [Materials](../../guide/materials.md).
""",
         plates=[("cup-holder-mount__p1", "Cup Holder: 80 mm", "base, joint, screw, washer"), ("cup-holder-mount__p4", "Cup Holder: 95 mm", "")],
         threemf=["Cup Holder Mount.3mf"],
         buy="Optional felt tape.",
         ),
    dict(section="bases", slug="rail-system", title="Rail System", tier=ULT,
         folder=["1. Base Mounts/Rail System Mount/"],
         summary="A screw-down track that one or more arms slide along. Great for workbenches and long desks.",
         body="""
**Parts**

| Part | Qty | Role |
|---|---|---|
| Rail 200mm | as many as you need (3 per plate) | Butt them end-to-end for longer tracks |
| Base Link Joint | 1 per arm | Slides along the rail freely |
| Locking Base Link Joint | 1 per arm | Slides, then locks in place with its own Screw + Washer |

## Install

1. Print rails and screw them to the surface **flange-up** (the counterbored side faces you; the narrow stem sits on the surface), in a straight line, ends butted tight. The holes take M4 / #8 screws at 80 mm pitch.
2. Slide on the link joints from the open end, one per arm.
3. For arms that must not move, use the **Locking** joint and tighten its screw.

## Profile & aluminium options

The rail is a **1″ × 0.45″ inverted T**: a 25.4 × 5.08 mm flange on a 15.24 mm stem. It isn't an industry-standard profile, so you can't buy a drop-in aluminium rail. You can make one from a **1″ × 3/16″ flat bar on a 1/2″ × 1/4″ spacer bar**, or **bolt the printed rails onto 2020 extrusion** (the holes land on a 20 mm grid). Dimensioned drawing and details: [Engineering Notes: rail profile](../../reference/engineering.md#the-rail-profile).
""",
         plates=[("rail-system__p1", "Rails 200 mm ×3", ""), ("rail-system__p2", "Rail Link Joint", "free-sliding"),
                 ("rail-system__p3", "Rail Locking Link Joint", "+ screw & washer")],
         threemf=["Rail System.3mf"],
         buy="Countersunk wood screws for the rails.",
         ),

    # ============================ LINKS ============================
    dict(section="links", slug="standard-links", title="Standard Links", tier=STD,
         folder=["2. Links/1. Locking Links/2. Standard Links/"],
         summary="The backbone of every build: one-piece links with a toothed rosette at each end, in eight lengths.",
         body="""
## Lengths

The number in the filename is the **pitch along the link**. The rosettes also sit 30.5 mm apart sideways, so the true pivot-to-pivot is a little longer (e.g. 202.3 mm for the 200; see [Engineering Notes](../../reference/engineering.md#links-are-cranked)). The printed part is 55.9 mm longer overall than the pitch (one rosette diameter).

| File | Pivot-to-pivot | Overall length | On a 256 × 256 mm bed |
|---|---|---|---|
| `LINK - 125mm` | 125 mm | 180.9 mm | ✔ |
| `LINK - 150mm` | 150 mm | 205.9 mm | ✔ |
| `LINK - 175mm` | 175 mm | 230.9 mm | ✔ |
| `LINK - 200mm` | 200 mm | 255.9 mm | ✔ diagonal (as placed in the 3MF) |
| `LINK - 225mm` | 225 mm | 280.9 mm | ✔ diagonal (as placed in the 3MF) |
| `LINK - 250mm` | 250 mm | 305.9 mm | ✔ diagonal (as placed in the 3MF) |
| `LINK - 275mm` | 275 mm | 330.9 mm | ✔ diagonal, just (as placed in the 3MF) |
| `LINK - 300mm` | 300 mm | 355.9 mm | ✘ needs a larger bed; not in the 3MF |

All links are 86.4 mm wide (the crank) and 38.1 mm tall as printed.

!!! note "300 mm link"
    `LINK - 300mm.STL` is in the folder but has no plate in *Standard Links Collection.3mf* (plates stop at 275 mm, the longest that fits a 256 mm bed diagonally). On a larger printer, import the STL on its own; otherwise use a 275 mm link or a [Modular Link](modular-link.md).

## Ends: ● and ●●

Each link has a **single-dot** end and a **double-dot** end (the dots are small holes inside the underside pocket). Always join **● to ●●**. The two ends' 36-tooth rings are clocked half a tooth apart, which is why the rule matters. See [How joints work](../../guide/how-it-works.md#the-one-rule-1-meets-2).

## Hardware

Every joint between two rosettes takes **one link hardware set**: `Link Hardware - Screw`, `- Washer`, `- Threaded Nut` (or `Threaded Nut - No Brand` if you prefer it without the logo). The collection's plate 1 prints two sets.
""",
         plates=[("standard-links-collection__p1", "Link Hardware ×2 sets", "screw, cone washer, threaded nut"),
                 ("standard-links-collection__p2", "LINK: 125 mm", ""), ("standard-links-collection__p5", "LINK: 200 mm", ""),
                 ("standard-links-collection__p8", "LINK: 275 mm", "")],
         threemf=["Standard Links Collection.3mf"],
         buy="Nothing. All joint hardware is printed.",
         ),
    dict(section="links", slug="payload-links", title="Payload Links (Fixed & Swivel)", tier=STD,
         folder=["2. Links/1. Locking Links/3. Payload Links/Payload Link - Fixed/", "2. Links/1. Locking Links/3. Payload Links/Payload Link - Swivel/"],
         summary="The last link in the chain: a rosette on one end, a payload interface on the other.",
         body="""
Every payload mount (VESA, 1/4-20, MagSafe, clamps…) fixes to a **Payload Link** with its own small Screw + Washer.

## Fixed Payload Links

| File | Reach | Variant |
|---|---|---|
| `PAYLOAD LINK - 50mm - 1` / `- 2` | 50 mm | 1 = “1 Circle”, 2 = “2 Circles” |
| `PAYLOAD LINK - 75mm - 1` / `- 2` | 75 mm | |
| `PAYLOAD LINK - 100mm - 1` / `- 2` | 100 mm | |

**Which variant?** The 3MF names them *1 Circle* and *2 Circles*: the end marking on the rosette. Pick the one that follows the ● / ●● rule with the link end you're attaching to (if the last link's free end is ●, use the 2-circle version, and vice versa).

## Swivel Payload Link

Adds a rotation axis just behind the payload, so you can turn portrait ↔ landscape or pan a camera **without loosening an arm joint**.

| Part | Qty |
|---|---|
| Swivel Body - 1 **or** - 2 (circles, as above) | 1 |
| Swivel Insert | 1 |
| Swivel - Screw / Washer / Nut | 1 each |

The swivel's own screw, washer and nut are smaller than the link hardware and are **not** interchangeable with it.
""",
         plates=[("standard-links-collection__p9", "Fixed Payload Links: 1 Circle", "50 / 75 / 100 mm"),
                 ("standard-links-collection__p10", "Fixed Payload Links: 2 Circles", "50 / 75 / 100 mm"),
                 ("standard-links-collection__p11", "Swivel: 1 Circle", "body + insert"),
                 ("standard-links-collection__p13", "Swivel Hardware", "screw, washer, nut")],
         threemf=["Standard Links Collection.3mf (plates 9–13)"],
         buy="Nothing.",
         ),
    dict(section="links", slug="branch-links", title="Branch Links", tier=STD,
         folder=["2. Links/1. Locking Links/4. Branch Links/"],
         summary="Split one arm into two or three. The key to camera + light rigs and stacked monitors.",
         body="""
| File | Outputs | Size |
|---|---|---|
| `3-Way Branch Link - Top` | 1 in → 2 out | 233.7 × 134.1 mm |
| `3-Way Branch Link - Bottom` | 1 in → 2 out (mirrored) | 233.7 × 134.1 mm |
| `4-Way Branch Link` | 1 in → 3 out | 233.7 × 181.8 mm |

The long axis carries rosettes at both ends (~178 mm apart); the side stub(s) come off the middle.
**Top** and **Bottom** are mirror variants, so choose by which side you want the side branch on.

**End markings (measured):** one end of the main axis and **every side stub** is ●. Only the far end is ●●. So whatever you attach to a side stub must present its ●● end.

Each rosette you use needs its own link hardware set: a 3-way that's fully used = 3 sets.

!!! tip "Load balance"
    Branch rigs tip over sideways, not forwards. Put the heavier branch over the base, or counter it with the other branch.
""",
         plates=[("standard-links-collection__p15", "3-Way Branch: Top", ""), ("standard-links-collection__p16", "3-Way Branch: Bottom", ""),
                 ("standard-links-collection__p14", "4-Way Branch", "")],
         threemf=["Standard Links Collection.3mf (plates 14–16)"],
         buy="Nothing.",
         ),
    dict(section="links", slug="modular-link", title="Modular Link", tier=ULT,
         folder=["2. Links/1. Locking Links/1. Modular Link/"],
         summary="Build a link of any length from 60 to 300 mm (in 20 mm steps): two toothed end joints plus a straight body extrusion.",
         body="""
## Parts per Modular Link

| Part | Qty | Notes |
|---|---|---|
| Teethed Joint - 1 | 1 | End joint (single-dot type) |
| Teethed Joint - 2 | 1 | End joint (double-dot type) |
| Link Body - *N*mm | 1 | 60, 80, 100 … 300 mm (11 lengths) |
| Locking Brace | 2 | Lock the body into the end joints |
| Screw Washer / Nut Washer | 1 each | Oblong washers for the joint hardware |

Plus link hardware sets for the joints at each end (the folder has its own `HARDWARE/` copy, identical to the Standard Links hardware).

## Why use it

* Lengths the Standard Links don't have (e.g. 60, 80, 100 mm stubs, or 240 mm).
* Long reaches printed as short parts: the body prints standing/flat and fits small beds.
* Parts are separable: change the reach later by swapping only the body.

!!! question "Effective length (estimate)"
    The library doesn't state the pivot-to-pivot length of an assembled Modular Link. From the part geometry it's roughly **body length + ~100 mm**. Measure your first assembly and note it here.

## Assembly (from the product render)

1. Slide the body into each Teethed Joint.
2. Fit the Locking Braces to lock the body in both joints.
3. Connect the joint rosettes to neighbouring links as usual (● ↔ ●●), using the Screw Washer / Nut Washer where the render shows them.
""",
         plates=[("modular-link__p1", "Joint Components", "teethed joints, braces, washers"),
                 ("modular-link__p2", "Bodies 60–140 mm", ""), ("modular-link__p3", "Bodies 160–240 mm", ""),
                 ("modular-link__p7", "Modular Link Hardware", "2 link hardware sets")],
         threemf=["Modular Link.3mf"],
         buy="Nothing (the product render shows small screws at the braces; if your braces don't hold by themselves, use short M3 screws).",
         ),
    dict(section="links", slug="ball-joint-link", title="Ball Joint Link", tier=ULT,
         folder=["2. Links/1. Locking Links/3. Payload Links/Ball Joint Link/"],
         summary="A double-ball “RAM-style” arm for fast, free positioning of the payload. One knob locks both balls.",
         body="""
Added in **v1.4**. Printed at **0.20 mm** in the supplied 3MF (finer layers for smooth balls).

## Parts

| Part | Qty | Role |
|---|---|---|
| Clamp Top / Clamp Bottom | 1 each | The two socket plates that squeeze the balls |
| Link Ball Mount P1 + P2 | 1 each | Ball on the **arm** side (printed in two halves) |
| Payload Ball Mount P1 + P2 | 1 each | Ball on the **payload** side (two halves) |
| Ball Mount Wedge | 4 | Key the P1/P2 halves together |
| Set Screw / Washer / Nut | 1 each | Clamps the plates together, locking both balls |
| `Payload Attachments/Ball Joint - Phone Mount - Cover` | optional | A phone-mount cover for the ball-joint payload side |

## Assembly

1. Join each ball mount's **P1 + P2** halves with two **Wedges** (a drop of CA glue makes it permanent).
2. Sandwich both balls between **Clamp Top** and **Clamp Bottom**.
3. Pass the **Set Screw** through the centre, add Washer + Nut, and tighten until both balls lock.

!!! question "Inferred"
    The library doesn't document how the Link Ball Mount attaches to the arm. By its name and folder (*Payload Links*) it takes the place of a payload link. Test-fit against your last link before printing a full set.
""",
         plates=[("ball-joint-link__p1", "Clamps", "top + bottom"), ("ball-joint-link__p2", "Hardware", "ball mounts, wedges, screw, washer, nut")],
         threemf=["Ball Joint Link.3mf"],
         buy="Optional CA glue.",
         ),
    dict(section="links", slug="cable-management", title="Cable Management Clips", tier=None,
         folder=["2. Links/1. Locking Links/5. Cable Management/"],
         summary="Snap-on clips that hold USB, XLR and power cables along the links.",
         body="""
Added in **v1.2**. Four sizes: **15, 16, 17, 18 mm** (the clip's inner opening). They differ only in how tightly they grip.

!!! tip "Dial in your fit"
    Print one of each size (they take minutes) and keep whichever snaps on firmly without cracking. Your flow calibration decides this more than anything else. Then print a batch of that size.

Use 1 clip every ~100–150 mm of cable run, plus one on each side of a joint so the cable has a service loop to flex.
""",
         plates=[("cable-management-clips__p1", "Clip: 15 mm", ""), ("cable-management-clips__p4", "Clip: 18 mm", "")],
         threemf=["CABLE MANAGEMENT CLIPS.3mf"],
         buy="Nothing.",
         ),

    # ============================ PAYLOADS ============================
    dict(section="payloads", slug="vesa", title="VESA Mounts", tier=STD,
         folder=["3. Payload Mounts/VESA Mounts/"],
         summary="75 × 75 and 100 × 100 VESA plates for monitors, portable displays and anything with a VESA pattern.",
         body="""
| File | Pattern | Plate |
|---|---|---|
| `Vesa Mount - 75mm` | 75 × 75 mm | 101.6 mm square |
| `Vesa Mount - 100mm` | 100 × 100 mm | 127 mm square |
| `Vesa Mount - Screw` + `- Washer` | | Fix the plate to a Payload Link |

## Assembly

1. Bolt the plate to the monitor with **M4 screws + washers** (most monitors; check the screw length so it doesn't bottom out).
2. Fix the plate to a **Payload Link** with the printed Screw + Washer.
3. Hang the monitor on the arm, then tighten the arm joints.

!!! warning "Weight"
    Official guidance: the system is “intended for items weighing less than 10 lbs” (4.5 kg), less at long reach. Portable monitors are ideal; full-size desktop monitors belong on a metal arm. PETG/ASA, 5–8 walls, 30–50 % infill.
""",
         plates=[("vesa-mounts__p1", "VESA 75", ""), ("vesa-mounts__p2", "VESA 100", ""), ("vesa-mounts__p3", "Payload Connecting Hardware", "screw + washer")],
         threemf=["Vesa Mounts.3mf"], buy="M4 screws + washers (length per monitor).",
         ),
    dict(section="payloads", slug="quarter-twenty", title="1/4-20 Mount", tier=STD,
         folder=["3. Payload Mounts/1-4 20 Mount/"],
         summary="The universal camera thread. Webcams, cameras, lights, phone clamps and tripod accessories.",
         body="""
**Parts:** Base (50.8 mm disc), Screw Holder **P1 + P2** (two halves that capture a real 1/4-20 bolt).

The 1/4-20 screw was fixed in **v1.2**. Re-download if your copy is older.

## Assembly

1. Put a **1/4-20 bolt or thumb screw** head-down into one Screw Holder half, close it with the other half.
2. Seat the holder in the Base so the thread points up through it.
3. Fix the Base to a Payload Link (or Swivel Payload Link).

!!! note "Supports"
    The Base has **supports enabled** in the supplied 3MF (normal/auto). Keep them on.
""",
         plates=[("1-4-20-mount__p1", "1/4-20 Mount", "base + screw holder halves")],
         threemf=["1-4 20 Mount.3mf"], buy="1/4-20 bolt or thumb screw.",
         ),
    dict(section="payloads", slug="baby-pin", title="Baby Pin Mount", tier=ULT,
         folder=["3. Payload Mounts/Baby Pin Mount/"],
         summary="A printed 5/8″ baby pin (stud) for lighting gear, clamps and grip accessories.",
         body="""
Added in **v1.4**, printed at 0.20 mm in the supplied 3MF.

| Plate | Pin length |
|---|---|
| Baby Pin Mount - Small | Short (61 mm part) |
| Baby Pin Mount - Medium | Standard (69 mm) |
| Baby Pin Mount - Large | Long (81.5 mm) |

Each pin prints as **two halves (P1 + P2)** joined with **two Screw Wedges**, then threads into the shared **Base**.

Use it for LED panels, fresnels and grip heads that take a 5/8″ baby pin. Treat printed pins as light-duty: ≤ ~1 kg, short reach.
""",
         plates=[("baby-pin-mount__p1", "Baby Pin: Short", ""), ("baby-pin-mount__p2", "Baby Pin: Standard", ""), ("baby-pin-mount__p3", "Baby Pin: Long", "")],
         threemf=["Baby Pin Mount.3mf"], buy="Optional CA glue for the pin halves.",
         ),
    dict(section="payloads", slug="phone-mount", title="Phone Mount", tier=STD,
         folder=["3. Payload Mounts/Phone Mount/"],
         summary="A spring-arm phone holder with two arm styles: accessory shoe or heat-set insert.",
         body="""
**Parts (plate 1):** Base - Small, Cover, 2× **Arm - Small - Hotshoe**, 2× **Arm - Small - Heat Insert**.
**Plate 2:** Payload Mount Screw + Washer.

The plate prints both arm styles. Use **one pair**:

* **Hotshoe arms:** a cold-shoe on the arm for a small light or mic next to the phone.
* **Heat-Insert arms:** take a threaded heat-set insert (size not specified; measure the bore) for a screw-on accessory.

Fix the Base to a Payload Link with the Screw + Washer.
""",
         plates=[("phone-mount__p1", "Phone Holder: Small", "base, cover, both arm styles"), ("phone-mount__p2", "Payload Connecting Hardware", "")],
         threemf=["Phone Mount.3mf"], buy="Rubber bands; heat-set inserts if using the Heat-Insert arms.",
         ),
    dict(section="payloads", slug="magsafe", title="MagSafe Mounts", tier=STD,
         folder=["3. Payload Mounts/Magsafe Mounts/"],
         summary="A cup that holds a MagSafe puck/magnet ring so a MagSafe phone snaps on.",
         body="""
Two revisions: `magSafe Mount - New` (15.2 mm tall) and `- Old` (16.5 mm). Both are 63.5 mm Ø and use the same Screw + Washer.
Test-fit your puck or ring against **New** first.

Supports are **on** (normal/auto) for both in the supplied 3MF.

!!! note
    The mount holds a MagSafe charger or magnet ring. It is not magnetic on its own.
""",
         plates=[("magsafe-mounts__p1", "MagSafe: New", "+ screw & washer"), ("magsafe-mounts__p2", "MagSafe: Old", "")],
         threemf=["magSafe Mounts.3mf"], buy="MagSafe charger puck or MagSafe-compatible magnet ring.",
         ),
    dict(section="payloads", slug="microphone", title="Microphone Mount", tier=STD,
         folder=["3. Payload Mounts/Microphone Mount/"],
         summary="A dedicated two-pivot mic adapter that bolts straight onto a link end.",
         body="""
Added in **v1.3**, printed at 0.20 mm in the supplied 3MF.

| Part | Qty | Notes |
|---|---|---|
| Microphone Mount Base - **1 Dots** *or* **2 Dots** | 1 | Pick the one that mates with your last link end (● ↔ ●●) |
| Microphone Mount Screw - **Short / Standard / Long** | 1 | The mic-side arm; pick the length that clears your mic body |
| Microphone Mount - Link Screw / Washer / Nut | 1 each | Small hardware for the second pivot |

The Base's large rosette joins the link with a normal link hardware set; its small rosette joins the mic-side arm with the small Link Screw/Washer/Nut, which gives the mic its own tilt axis.

!!! question "Inferred"
    The library doesn't describe the mic interface. Check how the mic-side “Screw” part meets your mic's clip or shock-mount thread before committing.
""",
         plates=[("microphone-mount__p1", "Microphone Mount", "bases (1 & 2 dots), 3 arm lengths"), ("microphone-mount__p2", "Microphone Mount Hardware", "")],
         threemf=["Microphone Mount.3mf"], buy="Nothing.",
         ),
    dict(section="payloads", slug="laptop", title="Laptop Mounts", tier=ULT,
         folder=["3. Payload Mounts/Laptop Mount/", "3. Payload Mounts/Tensioned Laptop Mount/"],
         summary="An open tray with a front lip, or a rubber-band tensioned gripper. Both are laptop-sized.",
         body="""
## Laptop Mount (tray)

One-piece tray 177.8 × 228.2 mm with a front lip, plus Screw + Washer. **Supports on** in the supplied 3MF.
v1.1 fixed its print orientation. Tilt the tray back slightly on the arm so the laptop rests against the lip.

## Tensioned Laptop Mount

| Part | Qty |
|---|---|
| Base (228.6 mm square) | 1 |
| Cover | 1 |
| Arm - Heat Insert | 2 |
| Payload Mount Screw / Washer | 1 each |

The arms are pulled closed by rubber bands and grip the laptop's sides. **Supports on** for the whole 3MF.

!!! warning
    A 228 mm-square part needs a 256 mm bed. Laptops are the heaviest everyday payload, so keep the arm short and print in PETG.
""",
         plates=[("laptop-mount__p1", "Laptop Mount (tray)", "+ screw & washer"),
                 ("tensioned-laptop-mount__p1", "Tensioned Laptop: Base", ""),
                 ("tensioned-laptop-mount__p2", "Tensioned Laptop: Cover & Arms", "")],
         threemf=["Laptop Mount.3mf", "Tensioned Laptop Mount.3mf"], buy="Rubber bands (tensioned version); heat-set inserts for the arms.",
         ),
    dict(section="payloads", slug="tensioned-clamps", title="Tensioned Clamps (S / M / L)", tier=None,
         folder=["3. Payload Mounts/Tensioned Clamps/"],
         summary="Rubber-band sprung grippers in three widths: phones, phablets/small tablets, and tablets.",
         body="""
Added in **v1.2**.

| Size | Base length | Typical device |
|---|---|---|
| Small | 66 mm | Phone, remote, small camera |
| Medium | 127 mm | Large phone / mini tablet |
| Large | 228.6 mm | Tablet |

Each is Base + Cover + **2 Arms** + Screw + Washer. Supports are on for the **S** and **M** bases in the supplied 3MFs.
Rubber bands provide the clamping force, so add bands for a firmer grip.
""",
         plates=[("s-tensioned-clamp__p1", "Small Tensioned Clamp", ""), ("m-tensioned-clamp__p1", "Medium Tensioned Clamp", ""),
                 ("l-tensioned-clamp__p1", "Large Tensioned Clamp", ""), ("s-tensioned-clamp__p2", "Hardware", "screw + washer")],
         threemf=["S Tensioned Clamp.3mf", "M Tensioned Clamp.3mf", "L Tensioned Clamp.3mf"], buy="Rubber bands.",
         ),
    dict(section="payloads", slug="t-claw", title="Modular Tensioned Claw", tier=STD,
         folder=["3. Payload Mounts/Modular Tensioned Claw/"],
         summary="A claw with swappable 60 / 70 / 80 mm jaws on hinged joins. Grips irregular shapes that a flat clamp can't.",
         body="""
| Plate | Contents |
|---|---|
| Modular T-Claw | Base, Cover, Arm Join Left + Right (supports on for the Base) |
| 60 / 70 / 80 mm Claws | One Left + Right arm pair per plate. Print the size you need |
| T-Claw Hardware | 2× Arm Joint Screw / Washer / Nut |
| Payload Connecting Hardware | Payload Mount Screw + Washer |

The Arm Joins have toothed rosettes, so each claw arm can be locked at an angle with the Arm Joint hardware. Tension comes from rubber bands.
""",
         plates=[("modular-t-claw__p1", "T-Claw Core", "base, cover, arm joins"), ("modular-t-claw__p2", "60 mm Claws", ""),
                 ("modular-t-claw__p4", "80 mm Claws", ""), ("modular-t-claw__p5", "T-Claw Hardware", "")],
         threemf=["Modular T-Claw.3mf"], buy="Rubber bands.",
         ),
    dict(section="payloads", slug="spring-clamp", title="Spring Clamp", tier=None,
         folder=["3. Payload Mounts/Spring Clamp/"],
         summary="A clothes-peg style clamp with soft TPU jaws for PCBs, cables, fabric, reflectors and clip-on lights.",
         body="""
Added in **v1.2**.

| Plate | Contents | Material |
|---|---|---|
| Spring Clamp | Body | PLA+/PETG (**supports on** as supplied) |
| Hardware | Screw + Washer | PLA+/PETG |
| Spring Clamp Inserts - TPU | 2× Insert | **TPU** |

Press the TPU inserts into the jaws, then fix the body to a Payload Link.
""",
         plates=[("spring-clamp__p1", "Spring Clamp Body", ""), ("spring-clamp__p3", "TPU Inserts", "")],
         threemf=["Spring Clamp.3mf"], buy="TPU filament (small amount).",
         ),
]
