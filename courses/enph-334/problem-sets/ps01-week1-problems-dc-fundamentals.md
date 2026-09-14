---
course: enph-334
type: problem-set
date: 2026-09-08
tags: [week1, ohms-law, voltage-divider, kirchhoff-current-law, thevenin-equivalent, superposition, phasors, rc-circuit, time-constant, complex-numbers, power-rating]
source: Wk1_Problems.pdf
---

# ENPH 334 / PHYS 334 — Week 1 Problems

> **Practice set for week 1** (week of 7 Sep 2026): review of basics, KCL/KVL, Thévenin, capacitors,
> phasors, complex AC circuits. Not submitted — this course has no graded homework; the marks are
> quizzes, labs and the final. Solutions are filed beside this note as
> [`ps01-week1-problems-dc-fundamentals-solutions.md`](ps01-week1-problems-dc-fundamentals-solutions.md).
>
> 🖼 **The circuit diagrams did NOT survive conversion — you need the PDF for every question.**
> Every circuit in this set is drawn as **vector graphics**, which `pdf_to_md.py` cannot extract and
> this environment cannot rasterise. Questions 1–4 say "for the circuit shown on the left" and the
> circuit is the whole question, so **open `ps01-week1-problems-dc-fundamentals.pdf` beside this
> note** to work them. Component values recovered from the PDF's text layer are given below where
> they could be read; they are not a substitute for seeing the topology.

## 1. Ohm's law

For the circuit shown, determine the values of the **voltage $V_1$** and the **resistor $R_1$**.

*From the solution: a series chain with $R_T = 12\ \text{k}\Omega$, $R_2 = 4\ \text{k}\Omega$,
$R_3 = 6\ \text{k}\Omega$, carrying $6\ \text{mA}$.*

## 2. Voltage divider rule

For the circuit shown, determine the **voltages at points 'a' and 'b'**. Determine also the
**current drawn from the battery**.

*From the solution: a $120\ \text{V}$ source, a ladder of $R_1 = 10$, $R_2 = 20$,
$R_3 = 30\ \text{k}\Omega$ with loads $R_{L1}$, $R_{L2} = 20$, $R_{L3} = 20\ \text{k}\Omega$.*

## 3. Kirchhoff's current law

For the circuit shown, determine the values of the resistors **$R_1$, $R_2$ and $R_3$**.

> **Can 2 W resistors be used in the design?**

*From the solution: branch currents of 50 mA, 20 mA and 10 mA, with 72 V and 12 V nodes.*

## 4. Thévenin, superposition

For the circuit shown, find the **Thévenin equivalent circuit between points 'a' and 'b'**.

Component values, read off the PDF's text layer:

$$R_1 = 0.8\ \text{k}\Omega, \quad R_2 = 4\ \text{k}\Omega, \quad R_3 = 6\ \text{k}\Omega, \quad R_4 = 1.4\ \text{k}\Omega$$
$$E_1 = 6\ \text{V}, \qquad E_2 = 10\ \text{V}$$

with $R_4$ in series on the way out to terminal 'a'.

## 5. AC circuits

A series R–C circuit driven by

$$e = 20\sin(\omega t)\ \text{V}, \qquad f = 1\ \text{kHz} \qquad [\,\omega = 2\pi f\ \text{rad/s}\,]$$

**(a)** Determine $Z_T$.
**(b)** Find the circuit current, $i$.
**(c)** Calculate $V_R$ and $V_C$.
**(d)** Draw the **phasor diagram** for $e$, $V_R$, $V_C$.

*From the solution: $R = 470\ \Omega$ and $C = 100\ \text{nF}$ (which is what gives
$X_C = 1591.6\ \Omega$ at 1 kHz).*

## 6. The R–C circuit

An R–C circuit has $R = 10\ \text{k}\Omega$, $C = 0.1\ \mu\text{F}$, and $V_b = 5\ \text{V}$.

**(a)** Calculate the **time constant**.
**(b)** Calculate the voltage across the capacitor at $t = 0.5\tau$.
**(c)** After the capacitor is fully charged, the input side of the circuit is disconnected from the
battery and connected to ground (**switch position 2** in the diagram in the Week 1 notes).
Calculate the **capacitor current after 0.2 ms**.

> 📝 Part (c) refers to "the diagram in the Week 1 notes" — Prof. Shastri's week 1 slides, which are
> **not yet filed in this repo**. The switch simply grounds the input so the capacitor discharges
> through $R$; the solution treats it as a plain RC discharge.

## 7. Complex numbers

Determine the value of the expression in the form $A + jB$:

$$\frac{(6 + j5)(10 - j6)}{(4 - j3)(5 + j5)}$$

> Note the electronics convention: **$j$, not $i$**, for $\sqrt{-1}$ — $i$ is reserved for current.
> The Lab A1 manual makes the same point explicitly.

---

## Connections

- Questions 1–4 are pure week-1 lecture material (KCL/KVL, Thévenin) and feed directly into
  [Lab A1](../labs/lab-a1-resistors-capacitors-diodes.md), where you build and measure a Thévenin
  equivalent on the bench.
- Questions 5–7 are the phasor/complex-impedance thread that week 2 picks up (Bode plots, dB) and
  that Lab A0 already simulated — see [`../labs/lab-a0-ltspice-simulation.md`](../labs/lab-a0-ltspice-simulation.md),
  whose RC low-pass uses the same $R = 5\ \text{k}\Omega$, $C = 100\ \text{nF}$ pairing as
  [`ps02`](ps02-week1-class-problems-thevenin-superposition.md) Q3.
- **Quiz 1 is Tue 29 Sep** and quizzes are **open-book, open-notes** — these worked solutions are
  exactly what you are allowed to bring.
