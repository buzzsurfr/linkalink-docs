# Materials

The library's readme says the designer printed most prototypes in **PLA+** “with excellent results”, and advises *when in doubt, start with PLA+*.
The **Kickstarter campaign** leans stronger: it recommends **PETG or ABS** for most setups, keeps **PLA for light-duty** setups, and suggests **PA612-CF** (carbon-fibre nylon) for heavy payloads and long arms ([Kickstarter Notes](../reference/kickstarter.md)).
This guide splits the difference: PLA+ for light desk builds, PETG as soon as something is cantilevered all day. Pick by where the arm lives and how long it holds a load.

| | **PLA+** | **PETG** | **ASA / ABS** | **TPU** |
|---|---|---|---|---|
| Best for | Phones, tablets, webcams, mics, lights, most desk builds | Heavier payloads, long horizontal reach, workshop, warm rooms | Cars, outdoors, direct sun, high heat | Spring Clamp jaw inserts only |
| Stiffness | ★★★ | ★★☆ | ★★☆ | n/a |
| Creep under constant load | Noticeable over weeks | Low | Low | n/a |
| Heat | Softens ~55–60 °C | ~75–80 °C | ~95–100 °C | n/a |
| UV | Poor | Fair | **ASA excellent** | n/a |
| Ease of printing | Easiest | Easy | Enclosure recommended | Slow, direct drive preferred |

## Quick picks

* **Desk arm, light payload:** PLA+, library defaults.
* **Laptop, monitors, overhead camera:** PETG; 5–8 walls, 30–50 % infill (the official heavy-payload settings).
* **Car cup-holder mount:** ASA or ABS. A closed car in summer will soften PLA and can sag PETG.
* **Near a soldering iron or a stove:** PETG as a minimum.

!!! tip "Mix materials"
    You don't have to print a whole arm in one filament. A common split: **PETG** for the base, first link and the hardware on the first joint (they take the most torque), and **PLA+** for everything further out.

Official purchase links for these filaments are in `0. Start Here/3. Link-A-Link - FILAMENT.txt`.
