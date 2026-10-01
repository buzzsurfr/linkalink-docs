# Getting Started

The official readme's advice is simple: *print one C-Clamp, a few links, the link hardware and one payload mount, then start building*. This page turns that into a checklist.

## Your first build (≈ 1 evening of printing)

This is [Blueprint 1: Starter Webcam / Phone Arm](../blueprints/starter-webcam-arm.md).

- [ ] **Calibrate flow rate** on your printer first. It matters more than any other setting for how well the threads and teeth fit. See [Printing](printing.md#flow-rate-calibration).
- [ ] Print **1× Fixed C-Clamp** in the opening size that fits your desk (`1. Base Mounts/Clamp Mounts/Fixed C-Clamp Mount/`, one plate per size in the 3MF).
- [ ] Print **2× Standard Links**: a 200 mm and a 150 mm (`2. Links/1. Locking Links/2. Standard Links/`).
- [ ] Print **3× link hardware sets**: screw + washer + threaded nut (plate 1 of *Standard Links Collection.3mf* prints two sets; print it twice).
- [ ] Print **1× Payload Link 50 mm** (1 Circle *or* 2 Circles, see below).
- [ ] Print **1× 1/4-20 Mount** and grab a 1/4-20 bolt, **or** print the Phone Mount / Small Tensioned Clamp for a phone.
- [ ] Print the **Link-A-Link Tool** (`0. Start Here/LINK A LINK - TOOL.STL`). It helps you get the last bit of torque on the nuts.

## The one rule: ● meets ●●

Every link has a **one-hole** end and a **two-hole** end. The holes are only markers, but they tell you which rosette faces which way.

!!! success "Always"
    **Single-dot end → Double-dot end.** “1 connects to 2. 2 connects to 1.”

!!! failure "Never"
    ● to ●, or ●● to ●●. The teeth won't face each other and the joint won't lock.

The same marking shows up on other parts: Payload Links come as **1 Circle / 2 Circles**, Swivel bodies as **- 1 / - 2**, Microphone Mount bases as **1 Dots / 2 Dots**, and Modular Link ends as **Teethed Joint - 1 / - 2**. Pick the variant that satisfies the rule with whatever it connects to.

## Then what?

1. Read [How it works](how-it-works.md) (5 minutes) so you understand joints, hardware counts and load.
2. Pick a [Blueprint](../blueprints/index.md) close to what you want.
3. Swap parts using the [Parts catalog](../parts/index.md).
4. Pick your material per build: [Materials](materials.md).
