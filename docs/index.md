---
title: Link-A-Link Field Guide
hide:
  - navigation
  - toc
---

# Link-A-Link Field Guide

**Link-A-Link** is a 3D-printable modular boom-arm system from *3D Printing Builds*. You print a **base**, chain together **links**, and finish with a **payload mount**. Every joint is a pair of toothed rosettes clamped by a printed screw and nut.

This guide covers the Ultimate STL library (v1.4). It replaces the `.txt` readmes with searchable docs, a parts catalog with plate previews, and **ten build blueprints** that show exactly what to print for the setups the product page only shows in photos.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Start here**

    ---

    What to print first, and the one rule you can't break (● meets ●●).

    [:octicons-arrow-right-24: Getting started](guide/index.md)

-   :material-cog-outline:{ .lg .middle } **How it works**

    ---

    Anatomy of a joint, end markings, counting hardware, and why arms droop.

    [:octicons-arrow-right-24: System anatomy](guide/how-it-works.md)

-   :material-printer-3d-nozzle:{ .lg .middle } **Print it right**

    ---

    Settings from the official guide *and* from the supplied 3MF projects, per-part supports, and materials.

    [:octicons-arrow-right-24: Printing](guide/printing.md)

-   :material-floor-plan:{ .lg .middle } **Blueprints**

    ---

    Ten complete builds: laptop riser, mic boom, overhead rig, creator rig, monitors, car mount and more.

    [:octicons-arrow-right-24: Browse blueprints](blueprints/index.md)

-   :material-view-grid-outline:{ .lg .middle } **Parts catalog**

    ---

    Every base, link and payload, with sizes, plate previews and what hardware it needs.

    [:octicons-arrow-right-24: Catalog](parts/index.md)

-   :material-file-find-outline:{ .lg .middle } **File index**

    ---

    All 192 STLs and 25 3MFs, with measured dimensions and folder paths.

    [:octicons-arrow-right-24: Reference](reference/file-index.md)

-   :material-calculator-variant-outline:{ .lg .middle } **Load calculator**

    ---

    Torque at every joint, including the arm's own weight, plus a tip-over check for free-standing bases.

    [:octicons-arrow-right-24: Calculate](blueprints/load-calculator.md)

-   :material-ruler-square-compass:{ .lg .middle } **Engineering notes**

    ---

    What the STLs reveal: 36-tooth joints, why ● meets ●●, keyed hardware, the rail profile, part masses.

    [:octicons-arrow-right-24: Teardown](reference/engineering.md)

-   :material-account-group-outline:{ .lg .middle } **Community**

    ---

    Discord, Kickstarter history, Community Builds, and what's still coming.

    [:octicons-arrow-right-24: Links](reference/community.md)

</div>

## The system in one picture

<div class="flow">
  <div><b>1 · Base Mount</b><span>C-Clamp · desk base · fixed rotating · wall · weighted · cup holder · rail</span></div>
  <i>→</i>
  <div><b>2 · Links</b><span>standard · modular · branch · cable clips</span></div>
  <i>→</i>
  <div class="acc"><b>Payload Link</b><span>fixed · swivel · ball joint</span></div>
  <i>→</i>
  <div><b>3 · Payload Mount</b><span>VESA · 1/4-20 · baby pin · phone · MagSafe · mic · laptop · clamps</span></div>
</div>

The library's folders follow the same order: `1. Base Mounts`, `2. Links`, `3. Payload Mounts`, plus `0. Start Here` (readmes + the assembly **tool**).

!!! info "Unofficial guide"
    This is a personal, community-style reference assembled from the files in the download, the official readmes and the public product page. Anything the files don't state outright is marked **Inferred**. See [About this guide](reference/about.md).
