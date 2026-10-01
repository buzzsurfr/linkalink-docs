# Printing

## Two sources of settings

The library gives you settings in two places, and they don't quite agree:

| Setting | Official guide (`4. PRINTING SETTINGS.txt`) | Supplied 3MF projects (“0.28mm Link-A-Link Settings”) |
|---|---|---|
| Layer height | **0.30 mm** | **0.28 mm** (first layer 0.20) |
| Walls | **4+** | 3 |
| Infill | **20 %+** | 20 % grid |
| Top / bottom shells | — | 4 / 3 |
| Supports | — | Off, except on specific parts (below) |
| Plate / printer | — | Textured PEI · Bambu Lab P1S 0.4 mm |

**This guide's recommendation:** use the 3MF projects as they are (0.28 mm layers, part orientation, per-part supports) but **raise walls to 4** for anything structural: links, bases, branch links and payload links. Hardware (screws, nuts, washers) is fine at 3.

!!! info "Not on a Bambu printer?"
    The 3MFs open in Bambu Studio and OrcaSlicer. In PrusaSlicer, Cura etc., import the **STLs**. They're already in print orientation (v1.1 fixed the Cup Holder and Laptop Mount orientation) and use the settings above.

## Heavy payloads

From the official guide, for monitors, big cameras, heavy lights and large tablets:

* **PETG, ASA or ABS**
* **30–50 % infill**
* **5–8 wall loops**

More walls add more stiffness than more infill does. Walls first, then infill.

## Flow rate calibration

The official guide calls this **one of the most important settings** for Link-A-Link, because the threads and teeth are toleranced to fit.

| Flow too high | Flow too low |
|---|---|
| Parts oversize, tight tolerances, nuts won't thread | Parts undersize, loose joints, weaker parts |

Search *“How to calibrate flow rate on [your printer] using [your slicer]”* and do it once per filament.
Bambu Studio and OrcaSlicer both have a built-in **Calibration → Flow Rate** routine.

!!! tip "Quick fit test"
    Before printing a whole arm, print **one screw + one nut** and a **cable clip**. If the nut threads smoothly by hand and the 16 mm clip snaps onto a link, your calibration is good.

## Parts that need supports

Pulled from the per-object settings inside the supplied 3MFs. Everything else prints support-free as oriented.

| Part | Support type in 3MF |
|---|---|
| 1-4 20 Mount - Base | normal (auto) |
| Laptop Mount (tray) | tree (auto) |
| magSafe Mount - New / Old | normal (auto) |
| Modular T-Claw - Base | normal (auto) |
| M / S Tensioned Clamp - Base | normal (auto) |
| Spring Clamp (whole project) | normal (auto) |
| Tensioned Laptop Mount (whole project) | normal (auto) |

## Parts with a finer profile

These 3MFs were saved with **0.20 mm Standard** (2 walls, 15 %) instead of the Link-A-Link profile. Keep 0.20 mm for the finer detail, but add walls if the part carries load:

* Ball Joint Link (smooth balls matter)
* Baby Pin Mount
* Microphone Mount

The **Fixed Rotating Base** 3MF uses *0.28 mm Extra Draft* (2 walls, 15 %). Bump that one to 4 walls / 20 %+.

## Every 3MF project at a glance

| 3MF project | Plates | Layer | Walls | Infill | Supports |
|---|---|---|---|---|---|
| `Desk Fixed C-Clamp Collection (40-80mm).3mf` | 5 | 0.28 | 3 | 20% | — |
| `Rotating C-Clamp Collection (40-80mm).3mf` | 5 | 0.28 | 3 | 20% | — |
| `Base Mount - Desk Base Collection.3mf` | 8 | 0.28 | 3 | 20% | — |
| `Fixed Rotating Base.3mf` | 2 | 0.28 | 2 | 15% | — |
| `Rail System.3mf` | 3 | 0.28 | 3 | 20% | — |
| `Cup Holder Mount.3mf` | 4 | 0.28 | 3 | 20% | — |
| `Fixed Wall Mount.3mf` | 2 | 0.28 | 3 | 20% | — |
| `Weighted Base.3mf` | 4 | 0.28 | 3 | 20% | — |
| `Modular Link.3mf` | 7 | 0.28 | 3 | 20% | — |
| `Standard Links Collection.3mf` | 16 | 0.28 | 3 | 20% | — |
| `Ball Joint Link.3mf` | 2 | 0.2 | 2 | 15% | — |
| `CABLE MANAGEMENT CLIPS.3mf` | 4 | 0.28 | 3 | 20% | — |
| `1-4 20 Mount.3mf` | 1 | 0.28 | 3 | 20% | 1-4 20 Mount - Base |
| `Baby Pin Mount.3mf` | 3 | 0.2 | 2 | 15% | — |
| `Laptop Mount.3mf` | 1 | 0.28 | 3 | 20% | Laptop Mount |
| `magSafe Mounts.3mf` | 2 | 0.28 | 3 | 20% | magSafe Mount - New, magSafe Mount - Old |
| `Microphone Mount.3mf` | 2 | 0.2 | 2 | 15% | — |
| `Modular T-Claw.3mf` | 6 | 0.28 | 3 | 20% | Modular T-Claw - Base |
| `Phone Mount.3mf` | 2 | 0.28 | 3 | 20% | — |
| `Spring Clamp.3mf` | 3 | 0.28 | 3 | 20% | all |
| `L Tensioned Clamp.3mf` | 2 | 0.28 | 3 | 20% | — |
| `M Tensioned Clamp.3mf` | 2 | 0.28 | 3 | 20% | M Tensioned Clamp - Base |
| `S Tensioned Clamp.3mf` | 2 | 0.28 | 3 | 20% | S Tensioned Clamp - Base |
| `Tensioned Laptop Mount.3mf` | 3 | 0.28 | 3 | 20% | all |
| `Vesa Mounts.3mf` | 3 | 0.28 | 3 | 20% | — |

See every plate with previews on [Print Plates](../reference/print-plates.md).

## Bed size

Most parts fit a 256 × 256 mm bed. Watch these:

* **Standard Links 200–275 mm** (overall 256–331 mm) only fit diagonally. The 3MF plates already place them that way, so print from the 3MF or copy the rotation.
* **Standard Link 300 mm** (355.9 mm overall) does not fit a 256 mm bed at all, which is why it has no 3MF plate. Use a 275 mm link or a Modular Link instead.
* **Tensioned Laptop Mount - Base** and **Large Tensioned Clamp** parts are 228.6 mm.
* **Weighted Base - Large** is 229 × 227 mm; **Round Base 240** and **Foot Base 240** are 240 mm.
