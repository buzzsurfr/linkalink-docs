# How It Works

## Three layers

| Layer | Job | Examples |
|---|---|---|
| **Base Mount** | Anchors the arm and provides the first rosette | C-Clamps, Desk Bases, Fixed Rotating Base, Wall, Weighted, Cup Holder, Rail |
| **Links** | Reach and angles; every end is a toothed rosette | Standard Links, Modular Link, Branch Links, Payload Links |
| **Payload Mount** | Holds the device; fixes to a Payload Link with a small screw + washer | VESA, 1/4-20, Baby Pin, Phone, MagSafe, Mic, Laptop, Clamps |

## Anatomy of a joint

Every link-to-link joint is the same: two **toothed rosettes** pressed face-to-face by a printed **T-head screw**, a **cone washer** and a **threaded nut**.
Each rosette has **36 teeth**, so a joint locks in **10° steps**. Once the joint is clamped, the teeth mesh and the angle can't slip.

* The **nut is keyed**: its three tabs drop into a Y-shaped keyway in the rosette's underside, so it can't spin.
* The **washer is keyed to the screw** (flats in its bore), so it turns with the screw.
* **You tighten by turning the T-head** (it's a built-in wing), with the tool for the last bit. To re-pose, back the screw off half a turn, lift the teeth out of mesh, rotate, and re-tighten.

More detail and measured drawings: [Engineering Notes](../reference/engineering.md).

<svg class="bp" viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Joint anatomy"><defs><pattern id="grid2" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" class="gridln"/></pattern></defs><rect width="760" height="260" fill="url(#grid2)" class="bpbg"/><line x1="40" y1="130" x2="720" y2="130" class="dim" stroke-dasharray="6 6"/><!-- screw --><rect x="60" y="92" width="16" height="76" rx="3" class="base"/><rect x="76" y="118" width="120" height="24" rx="4" class="base"/><path d="M 100 118 l 6 24 M 116 118 l 6 24 M 132 118 l 6 24 M 148 118 l 6 24 M 164 118 l 6 24 M 180 118 l 6 24" class="thread"/><text x="120" y="200" class="lbl" text-anchor="middle">T-head screw</text><text x="120" y="216" class="lbl small" text-anchor="middle">turn this to tighten</text><!-- washer --><path d="M 236 100 L 262 82 L 262 178 L 236 160 Z" class="base"/><text x="250" y="215" class="lbl" text-anchor="middle">cone washer</text><text x="250" y="231" class="lbl small" text-anchor="middle">keyed to the screw</text><!-- link A --><rect x="300" y="72" width="34" height="116" rx="8" class="lnk-fill"/><path d="M 334 78 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6" class="teeth"/><text x="318" y="60" class="lbl" text-anchor="middle">link end "2" (●●)</text><!-- link B --><rect x="392" y="72" width="34" height="116" rx="8" class="lnk-fill"/><path d="M 392 78 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6 l -8 6 l 8 6" class="teeth"/><text x="410" y="228" class="lbl" text-anchor="middle">link end "1" (●)</text><text x="364" y="30" class="lbl strong" text-anchor="middle">teeth mesh → locks angle</text><!-- nut --><path d="M 470 96 L 500 84 L 530 84 L 530 176 L 500 176 L 470 164 Z" class="base"/><text x="500" y="215" class="lbl" text-anchor="middle">threaded nut</text><text x="500" y="231" class="lbl small" text-anchor="middle">tabs lock it in the keyway</text><!-- tool --><circle cx="640" cy="130" r="48" class="base" fill-opacity=".35"/><circle cx="640" cy="130" r="18" class="bpbg-fill"/><text x="640" y="205" class="lbl" text-anchor="middle">Link-A-Link tool</text><text x="640" y="222" class="lbl small" text-anchor="middle">(tightening aid)</text></svg>

| Printed part | File | Size |
|---|---|---|
| Screw | `Link Hardware - Screw.STL` | 41.9 mm long (printed lying down) |
| Cone washer | `Link Hardware - Washer.STL` | 38.1 mm Ø |
| Threaded nut | `Link Hardware - Threaded Nut.STL` (or `- No Brand`) | 38.1 mm Ø |
| Tool | `0. Start Here/LINK A LINK - TOOL.STL` | 67.6 mm Ø |

Link rosettes are 55.9 mm across on every part (links, base joints, branch links, payload links), so any link rosette mates with any other, as long as you follow the 1-meets-2 rule. (Smaller accessory pivots, like the mic mount's second joint or the T-Claw arms, use their own smaller hardware.)

!!! tip "Why printed hardware works"
    The screw is printed **lying down** so its layers run along the thread, not across it. Upright printed screws snap at a layer line. Print the hardware in the orientation supplied.

## The one rule: 1 meets 2

![Rosette underside: keyway and indicator dots](../assets/eng/rosette-pocket.png){ width="340" align=right .hero-img }

Each link end carries **one or two indicator holes** inside its underside pocket (right). They mark the two tooth variants:

* **● → ●●** ✔
* **● → ●** ✘  **●● → ●●** ✘

The same idea is used everywhere a part has two “handed” versions (`- 1` / `- 2`, *1 Circle* / *2 Circles*, *1 Dots* / *2 Dots*).

<div style="clear:both"></div>

## Counting hardware

```
link hardware sets = number of rosette-to-rosette joints
```

For a straight arm: **base → N links → payload link** has **N + 1** joints.
Each branch output you use adds one more. Base-to-base-joint screws and payload-to-payload-link screws are **separate, smaller parts** that come with the base or payload.

| Build | Joints (= link hardware sets) |
|---|---|
| Clamp → 2 links → payload link | 3 |
| Clamp → 3 links → payload link | 4 |
| Base → link → 3-Way Branch → (link → payload link) + (payload link) | 5 |

## Reach, height and why arms droop

Link names give the **pitch along the link** (`LINK - 200mm` = 200 mm; the part itself is 255.9 mm long). The rosettes are also offset 30.5 mm sideways, so the true pivot-to-pivot is slightly longer (202.3 mm for a 200). Add the pitches along the chain to get the arm's maximum reach.

What each joint has to resist is **torque**. That's everything beyond the joint, *including the arm's own links and hardware*, each times its horizontal distance to the joint:

```
torque at a joint = Σ (mass beyond the joint × horizontal distance)
```

A 500 g camera held 300 mm out is 0.15 kg·m at the base joint, plus roughly 0.03–0.05 kg·m for the links holding it there. The same camera 600 mm out more than doubles it. The [Load Calculator](../blueprints/load-calculator.md) does the sum for you. So:

* The **first joint** (at the base) carries the most. Tighten it hardest and build it strongest.
* **Vertical** links are nearly free; **horizontal** links are where the torque comes from.
* To hold more, shorten the reach before you add infill.
* PLA **creeps** under constant load, so a pose that holds today can sag over weeks. Use PETG for anything that sits cantilevered all day.

!!! warning "Official limit"
    The product page states the system is “intended for items weighing less than 10 lbs” (≈ 4.5 kg), with results depending on arm length, mounting method, print quality and material. It is “not designed to replace heavy-duty metal boom arms.”

## Tiers

The product sells **Standard** and **Ultimate** libraries. Pages in this guide are tagged <span class="tier std">Standard</span> or <span class="tier ult">Ultimate</span> based on the product page's lists. Items the page doesn't list are untagged. If you own Ultimate you have everything here.
