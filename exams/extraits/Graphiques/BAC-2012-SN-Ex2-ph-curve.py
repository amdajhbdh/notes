#!/usr/bin/env python3
"""
BAC 2012 SN - Exercice 2: pH = f(V) Titration curves
Strong base (B1) and weak base (B2)
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

V_acid = np.linspace(0, 20, 500)

C_base_strong = 0.01
C_acid = 0.01
V_base = 10


def pH_strong(V):
    if V == 0:
        return 12
    V_total = V_base + V
    n_OH_initial = C_base_strong * V_base
    n_H3O_added = C_acid * V

    if V < 8:
        pOH = -np.log10(n_OH_initial / V_total)
        return 14 - pOH
    elif V == 8:
        return 7
    else:
        excess = n_H3O_added - n_OH_initial
        return -np.log10(excess / V_total * 1000)


def pH_weak(V):
    pKa = 9.2
    if V == 0:
        return 12.5
    V_total = V_base + V

    if V < 10:
        ratio = V / (10 - V)
        if ratio > 0:
            pH = pKa + np.log10(ratio)
            return max(pH, 3)
        else:
            return 3
    elif V == 10:
        return (pKa + 14) / 2
    else:
        excess = C_acid * V - C_base_strong * V_base
        if excess > 0:
            pH = -np.log10(excess / V_total)
            return min(max(pH, 3), 12)
        else:
            return 12


pH1 = np.array([pH_strong(v) if v != 0 else 12 for v in V_acid])
pH2 = np.array([pH_weak(v) if v != 0 else 12.5 for v in V_acid])

ax.plot(V_acid, pH1, "b-", linewidth=2, label=r"$(1): B_1 \text{ (forte)}$")
ax.plot(V_acid, pH2, "r-", linewidth=2, label=r"$(2): B_2 \text{ (faible)}$")

ax.axhline(y=7, color="gray", linestyle="--", linewidth=1, alpha=0.7)
ax.axvline(x=8, color="blue", linestyle=":", linewidth=1, alpha=0.5)
ax.axvline(x=10, color="red", linestyle=":", linewidth=1, alpha=0.5)

ax.set_xlabel(r"$V \text{ (mL)}$", fontsize=14)
ax.set_ylabel(r"$pH$", fontsize=14)
ax.set_title(r"BAC 2012 SN - Exercice 2: $pH = f(V)$", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=12)
ax.set_xlim(0, 20)
ax.set_ylim(2, 14)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2012-SN-Ex2-ph-curve.png",
    dpi=150,
)
print("Saved: BAC-2012-SN-Ex2-ph-curve.png")
plt.close()
