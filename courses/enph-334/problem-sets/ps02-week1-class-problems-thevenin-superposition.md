---
course: enph-334
type: problem-set
date: 2026-09-08
tags: [week1, class-problems, thevenin-equivalent, superposition, phasors, rc-circuit, storey-6-24]
source: ENPH334_ClsProb_Wk1.pdf
---

# ENPH 334 / PHYS 334 — Class Problems, Week 1

> **A separate stream from [`ps01`](ps01-week1-problems-dc-fundamentals.md).** This course issues
> two different problem documents per week — "Week N Problems" and "Class Problems, Week N" — and
> they cover different material. This is the in-class set, worked in the **Tuesday 11:30 tutorial
> in MACDON 1**. Solutions beside it as
> [`ps02-week1-class-problems-thevenin-superposition-solutions.md`](ps02-week1-class-problems-thevenin-superposition-solutions.md).
>
> 🖼 **The circuits did not convert** — they are vector drawings. Component values below were read
> off the PDF's text layer and are reliable, but the **topology is only in
> `ps02-week1-class-problems-thevenin-superposition.pdf`**, which you need open to work Q1 and Q2.

## 1. Thévenin equivalent

Find the **Thévenin equivalent circuit between points (A, B)**, with $R_4$ **removed**.

$$V_1 = 8\ \text{V}, \quad R_1 = 6\ \Omega, \quad R_2 = 4\ \Omega, \quad R_3 = 2\ \Omega, \quad R_4 = 3\ \Omega$$

## 2. Superposition

Use **superposition** to find the **voltage across $R_2$** and the **current through $R_1$**.

$$V_1 = 5\ \text{V}, \quad V_2 = 3\ \text{V}, \quad R_1 = 6\ \Omega, \quad R_2 = 6\ \Omega, \quad R_3 = 3\ \Omega$$

## 3. Phasor diagram — [Storey Exercise 6.24]

A sinusoidal voltage of **12 V at 500 Hz** is applied across a **series combination of a 5 kΩ
resistor and a 100 nF capacitor**.

Use a **phasor diagram** to determine the **current through the combination**, and the **phase
angle between this current and the applied voltage**.

> 🔑 Same $R = 5\ \text{k}\Omega$, $C = 100\ \text{nF}$ pair as the RC low-pass simulated in
> [Lab A0](../labs/lab-a0-ltspice-simulation.md) — there you found $f_c \approx 318$ Hz from
> $f_c = 1/(2\pi RC)$; here you evaluate the same network by hand at 500 Hz, just above that corner.
> Worth doing both and checking they agree.

> The exercise number is from **Storey, *Electronics: A Systems Approach*, 6th ed.**, the course's
> recommended text.
