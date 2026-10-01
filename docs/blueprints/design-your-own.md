# Design Your Own

A blueprint is just four decisions: **payload → base → reach → material**. Work through them in that order.

## 1 · Payload

| Payload | Mount |
|---|---|
| Monitor / portable display | [VESA 75 / 100](../parts/payloads/vesa.md) |
| Camera, webcam, light, tripod accessory | [1/4-20 Mount](../parts/payloads/quarter-twenty.md) |
| Stand-mount light, grip head | [Baby Pin](../parts/payloads/baby-pin.md) |
| Phone | [Phone Mount](../parts/payloads/phone-mount.md), [MagSafe](../parts/payloads/magsafe.md), [Small Tensioned Clamp](../parts/payloads/tensioned-clamps.md) |
| Tablet | [Medium / Large Tensioned Clamp](../parts/payloads/tensioned-clamps.md), [T-Claw](../parts/payloads/t-claw.md) |
| Microphone | [Microphone Mount](../parts/payloads/microphone.md) |
| Laptop | [Laptop Mount / Tensioned Laptop Mount](../parts/payloads/laptop.md) |
| PCB, cable, reflector, fabric | [Spring Clamp](../parts/payloads/spring-clamp.md) |

## 2 · Base

| Situation | Base |
|---|---|
| Can screw into a **wall** | [Fixed Wall Mount](../parts/bases/wall-mount.md) |
| Several arms along a **bench or long desk** | [Rail System](../parts/bases/rail-system.md) |
| Can screw into the **desk surface** | [Fixed Rotating Base](../parts/bases/fixed-rotating-base.md) |
| No drilling, but there's a **desk edge** | [Rotating / Fixed C-Clamp](../parts/bases/c-clamps.md) |
| In a **car** | [Cup Holder Mount](../parts/bases/cup-holder.md) |
| No edge, no drilling, **free-standing** | [Weighted Base](../parts/bases/weighted-base.md) (or [Round / Foot Base](../parts/bases/desk-bases.md) for light loads) |

Clamps and screw-down bases hold the most torque. Free-standing bases only hold as much as their footprint and weight allow.

## 3 · Reach

1. Measure from where the base will sit to where the device must end up, both **horizontally** and **vertically**.
2. Choose links whose pivot-to-pivot lengths add up to a bit more than the straight-line distance. Joints need slack to bend.
3. Prefer **two medium links** to one long one: more ways to pose it, less torque at each joint.
4. Put vertical height in the **first** link and horizontal reach **later** in the chain.

**Standard Link pitches:** 125 · 150 · 175 · 200 · 225 · 250 · 275 · (300) mm
**Payload Links:** 50 · 75 · 100 mm, or Swivel
**Modular Link:** body 60–300 mm in 20 mm steps (+ ≈ 100 mm for the end joints, estimated)

## 4 · Check the torque

**Two numbers get you close: the payload's weight and how far it sticks out horizontally.** But the arm has weight too, and every joint has to hold everything beyond it, links and hardware included.

```
torque at a joint = Σ (each mass beyond that joint × its horizontal distance from the joint)
```

* The **payload** acts at its centre of mass: the end of the payload link plus however far the device's own centre sits beyond that (a laptop's is ~150 mm past the tray screw).
* Each **link** acts at its midpoint with its own mass. A `LINK - 200mm` weighs roughly **110 g** in PLA+ at 4 walls / 20 %, or **~165 g** in PETG at 6 walls / 40 %.
* Each **joint's hardware** (screw + washer + nut) adds ~20 g at that joint.

Worked example: [Blueprint 1](starter-webcam-arm.md), with a 300 g webcam + mount about 290 mm out.

| Contribution at the base pivot | Mass | Horizontal arm | kg·m |
|---|---|---|---|
| Payload | 300 g | ~0.29 m | 0.088 |
| Link 200 (rising at 72°) | 110 g | ~0.03 m | 0.003 |
| Link 150 (level) | 89 g | ~0.14 m | 0.012 |
| Payload link + 3 hardware sets | 90 g | (various) | 0.014 |
| **Total** | | | **≈ 0.12** (arm ≈ 25 %) |

So for light payloads the arm is a real share of the load, often a quarter or more. For heavy payloads it matters less. **Use the [Load Calculator](load-calculator.md)**: it does this for any chain and checks tip-over for free-standing bases.

| Torque at the base pivot | Guidance |
|---|---|
| < 0.15 kg·m | PLA+, library defaults |
| 0.15–0.35 kg·m | PETG, 4–6 walls, 25–40 %, tighten well |
| 0.35–0.6 kg·m | PETG/ASA, 5–8 walls, 30–50 %, clamp or screw-down base |
| > 0.6 kg·m | Shorten the reach or rethink. You're into metal-arm territory |

!!! question "These bands are guidance, not test data"
    The creator's published data point is that “a standard 3-link setup supported 10+ lbs”, with no reach or material given. In the comments the creator also says to think “under 10–15 lbs max” and to “keep the arm reasonably short”. The bands above are deliberately conservative. Load-test your own prints over something soft.

## 5 · Count parts

* **Link hardware sets** = rosette-to-rosette joints (see [How it works](../guide/how-it-works.md#counting-hardware)).
* **Payload screw + washer**: 1, from the payload's folder.
* **Base screw + washer** (+ set screw on rotating bases): from the base's folder.
* **Cable clips**: about 1 per 100–150 mm of cable.

## Blank worksheet

Copy this into your notes:

```text
Build name:
Payload / weight:                 Mount:
Base:                             Opening/size:
Chain (base → payload):  [base] → ___mm → ___mm → ___mm → [payload link ___] → [mount]
Reach (horizontal): ___ mm        Height: ___ mm
Torque ≈ ___ kg × ___ m = ___ kg·m
Material / walls / infill:
Link hardware sets: ___           Bought hardware:
```
