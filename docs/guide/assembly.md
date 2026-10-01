# Assembly & Tuning

## General order

1. **Mount the base first** (clamp it, screw it down, or fill it) and fit its **Base Link Joint**.
2. **Work outward.** Add one link at a time, following **● → ●●**. Leave each joint finger-loose.
3. **Add the Payload Link**, then the **payload mount**, then the device.
4. **Pose the arm with the device on it.** It's much easier to find the balance point with the real weight attached.
5. **Tighten from the base outward.** Finger-tight first, then the last bit with the **Link-A-Link Tool**.
6. **Clip the cables** last, leaving a small loop at every joint.

## Making a joint

```
T-head screw → cone washer → rosette → rosette → threaded nut
```

1. Drop the **nut** into the underside pocket of one rosette so its three tabs sit in the Y-keyway (it can't turn now).
2. Put the **cone washer** on the screw (the flats in its bore line up with the screw's flats) and pass the screw through the other rosette.
3. Bring the teeth together (**● to ●●**) and **turn the T-head** to tighten. Finish with the tool on the T-head.

* Teeth must face teeth. If the two rosettes sit flat without meshing, you've paired ● with ● or ●● with ●●. Flip or swap.
* Joints index in **10° steps** (36 teeth). You can't split the difference, so use a Swivel or Ball Joint for fine aim.
* Tighten until the teeth are fully seated. You'll feel it click into mesh and stop rotating.

!!! tip "Re-posing"
    Back the **screw** off about half a turn, lift the teeth out of mesh, rotate a tooth or more, re-seat and tighten again. You don't need to take the joint apart.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Nut won't thread / binds | Over-extrusion, elephant's foot on the screw | Calibrate flow; chamfer the screw tip; add a touch of dry lubricant |
| Nut spins instead of tightening | Tabs not seated in the Y-keyway | Rotate the nut until the three tabs drop into the keyway |
| C-Clamp cracks at the inner curve | Over-tightened (reported in PETG) | Snug is enough; use the Round Pad to spread load |
| 1/4-20 thread strips or snaps | Printed 1/4-20 bolt | Use a **metal** 1/4-20 bolt in the 1/4-20 Mount |
| Nut threads but strips | Under-extrusion, or 2-wall prints | Calibrate flow; print hardware with 4 walls |
| Joint slips under load | Not tightened to full mesh; torque too high for the reach | Tighten with the tool; shorten horizontal reach; move load over the base |
| Arm sags over days | PLA creep | Reprint the first joint's links + hardware in PETG |
| Screw snaps at the head | Printed upright / scaled | Print hardware as supplied (lying flat), never rescale |
| Rosettes won't mesh at all | ● to ● or ●● to ●● | Swap for the other end / the other variant (1 ↔ 2) |
| Clamp walks on the desk | Wrong opening size | Use the smallest C-Clamp opening that fits; fit the Round Pad |
| Cable clip too loose / cracks | Flow / tolerance | Try the next clip size (15–18 mm) |
| Base tips over | Footprint too small for the reach | Weighted Base (Large), Foot Base pointed at the load, or a clamp |

## Safety

* Keep total payload **under 10 lb / 4.5 kg** (official guidance), and much lower at long reach.
* Don't put anything valuable **over** a fragile surface on an untested arm. Load-test it over a bed or couch first.
* Vehicle mounts: ASA/ABS, never where an airbag deploys, never blocking your view.
