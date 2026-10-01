---
title: Load Calculator
---

# Load Calculator

Describe your arm link by link. The calculator works out the **torque at every joint**, including the weight of the printed arm itself, and checks whether a free-standing base will tip.

<div id="lal-calc"><p><em>Loading calculator… (needs JavaScript)</em></p></div>

## What it assumes

* **Link masses** are estimated from the STL volumes and surface areas: a shell of *walls × 0.42 mm* plus the infill percentage for the core, at 1.24 g/cm³ (PLA+) or 1.27 g/cm³ (PETG). Every joint adds one printed hardware set (about 18–21 g).
* **Standard Link pitch** is the true rosette-to-rosette distance. A `LINK - 200mm` is 202.3 mm because its rosettes sit 30.5 mm apart sideways ([Engineering notes](../reference/engineering.md#links-are-cranked)).
* **Modular Link** length is body + ≈100 mm (estimated).
* **Payload** is the device *plus* its payload mount (a 1/4-20 mount is ≈ 17 g, VESA plates 60–90 g). Its centre of mass is placed the given distance beyond the end of the payload link.
* **Ballast cavities** in the Weighted Bases are estimated at ≈ 0.3 / 0.75 / 1.3 litres (S / M / L). Sand ≈ 1.5 g/cm³, steel BBs ≈ 4.5 g/cm³.
* The **verdict bands** are this guide's conservative guidance, not test data. The creator's only published test is “a standard 3-link setup supported 10+ lbs”, with no reach or material given.

!!! tip "Reading the result"
    Look at the **base pivot** row first; it's always the worst. If the arm's own weight is a big share there (say 30 %+), a shorter or lighter chain will buy you more than extra infill will.
