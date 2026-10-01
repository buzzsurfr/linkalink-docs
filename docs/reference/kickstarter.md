---
title: Kickstarter Notes
---

# Kickstarter Notes

The [Kickstarter campaign](https://www.kickstarter.com/projects/3dprintingbuilds/link-a-link-a-3d-printable-modular-boom-arm-system) (15 Apr – 15 May 2026) became the unofficial record of the project: specs, creator answers and backer tips that aren't in the library. This page pulls out what's useful, as of late September 2026.

## At a glance

| | |
|---|---|
| Funded | $156,600 from 2,469 backers (goal $1,000; funded in 5 minutes) |
| Files delivered | 5 June 2026 (v1.0/v1.1), via Kickstarter's digital delivery |
| Now hosted at | 3dprintingbuilds.com › Dashboard › Pro Builds (moved with v1.4, 21 Sep 2026) |
| Updates promised | Future updates to *this version* of Link-A-Link are included for backers |

## Specs & claims not in the readmes

* **Load test:** “a standard 3-link setup supported 10+ lbs without issues.” Reach and material weren't given. In the comments the creator adds: think “under 10–15 lbs max”, and “keep the arm reasonably short and everything tightened down.”
* **Not a metal-arm replacement:** asked about a 19 lb monitor, the creator pointed to light-to-medium payloads (“cameras, lights, portable monitors”).
* **Materials:** the campaign recommends **PETG or ABS** for most setups, **PLA** for light duty, and **PA612-CF** (carbon-fibre nylon) for heavy payloads and long arms. The library's readme leads with PLA+ instead. The creator's later view is that ASA or CF grades bring heat resistance and stiffness, not higher load ratings.
* **Print settings (campaign):** PETG/ABS/CF, 20 %+ infill, **4+ walls**, 0.3 mm layers. That matches the readme, not the 3MF profiles. See [Printing](../guide/printing.md).
* **Bed size:** designed to fit a 256 × 256 mm plate.
* **Tensioned grips:** “All it takes is two rubber bands.” The Large clamp was shown with a 13″ iPad Pro, Medium with an iPad Mini in a heavy case, Small with an iPhone 15. Each clamp expands a few inches in width.
* **Laptop mount:** tested with a 13″ Surface Book and a 16″ MacBook Pro. The cup-holder laptop/tablet setup is for **parked use only**.
* **Branching:** the campaign describes branches “at 45° and 90°”. The v1.4 Branch Links measure as 90° side stubs ([Engineering Notes](engineering.md#links-are-cranked)).

## Stretch goals: status

| Stretch goal | Announced | In the v1.4 library? |
|---|---|---|
| Laptop Holder | Update #3–4 | ✔ Laptop Mount + Tensioned Laptop Mount |
| Tensioned Grip Bundle | Update #3, #5 | ✔ Tensioned Clamps S/M/L, T-Claw |
| Weighted Mount Bundle | Update #6 | ✔ Small / Medium / Large |
| Car Mount Bundle | Update #3, #8 | ◐ Cup Holder Mount ✔ · **headrest mount ✘** · adaptive “twist-to-fit” cup holder (future) ✘ |
| Rail System | Update #4, #10 | ✔ |
| Quick Release System (wall / payload) | Unlocked by Update #6 | **✘ not yet** |
| Friction-based arm system | Being unlocked in Update #6 | **✘ not yet** (backers still asking) |
| Light bulb / light socket mount | Mentioned in comments | ✘ |
| “Templates” for the teethed connection points, for designing your own attachments | Creator reply in comments | ✘ not in v1.4 |
| Full instruction manual | Promised from launch | ✘ still in development (this guide fills the gap) |

The creator also mentioned experimenting with **an O-ring in the joint** to add friction and control.

## Answers from the comments

* **No STEP files.** STL only, “for this campaign”. Remixers get meshes; see [Engineering Notes](engineering.md) for measured dimensions.
* **1/4-20 mount:** use a **metal** 1/4-20 bolt. A printed one can snap off inside your camera.
* **C-Clamp cracking:** a backer's PETG C-clamp cracked at the inside curve after hard tightening. Snug is enough; the Round Pad spreads the load.
* **Round Pad on the Rotating C-Clamp:** it's only packaged with the fixed clamp, but both clamps use the same screw, so it fits.
* **2020 / 10-series extrusion mount:** requested and not provided. See the [rail notes](engineering.md#can-i-buy-an-aluminium-rail-instead) for a way to combine the printed rail with 2020.
* **Mic mount:** designed for standard threaded microphones.
* **Swivelling base on a free-standing stand:** a backer noted that only the Fixed Rotating Base takes the rotating (flange-less) base joint; the Round/Foot/Weighted bases use a fixed joint. No official answer yet.
* **Access problems:** complete the Kickstarter Pledge Manager first. After v1.4 everything is on 3dprintingbuilds.com (Kickstarter email → *Forgot Password*).

## Update timeline

| # | Date | Title / gist |
|---|---|---|
| 1 | 15 Apr | Live, funded in 5 minutes |
| 2 | 16 Apr | Why Kickstarter (one-time price, future updates included) |
| 3 | 17 Apr | First stretch goals; vote: quick release vs friction arm |
| 4 | 24 Apr | Laptop holder unlocked |
| 5 | 29 Apr | Tensioned Grip Bundle (two rubber bands) |
| 6 | 3 May | Weighted Mount Bundle; Quick Release unlocked; Friction System next |
| 7 | 9 May | How the creator uses it daily (laptop, speakers, mic, lights, cameras, couch tablet) |
| 8 | 12 May | Car Mount Bundle: cup holder + modular tensioned laptop holder |
| 9 | 14 May | Last 24 hours |
| 10 | 15 May | Funded; Rail System in testing |
| 11 | 1 Jun | Delivery date, Discord, hardware & filament guide |
| 12 | 5 Jun | Files ready; manual still in development; Discord is the support channel |
| 13 | 12 Jun | File access help (Pledge Manager, Pay Over Time) |
| 14 | 21 Sep | **v1.4** (Baby Pin, Ball Joint Link), move to 3dprintingbuilds.com, **Community Builds** |
