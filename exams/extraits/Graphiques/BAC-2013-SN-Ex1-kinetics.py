#!/usr/bin/env python3
"""
BAC 2013 SN - Exercice 1: Redox kinetics
[I2] vs t for I- + H2O2 reaction
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

t = np.array([0, 2, 5, 7.5, 10, 12.5, 15, 20, 25, 30])
I2 = np.array([0, 1.5, 4, 6, 7.5, 9, 10, 11, 11, 11]) * 1e-3

ax.plot(t, I2 * 1000, "b-o", linewidth=2, markersize=8, label=r"$[I_2] \times 10^3$")

ax.axhline(y=11, color="gray", linestyle="--", linewidth=1, alpha=0.7)
ax.axvline(
    x=7,
    color="red",
    linestyle=":",
    linewidth=1,
    alpha=0.5,
    label=r"$t_{1/2}=7 \text{ min}$",
)

ax.set_xlabel(r"$t \text{ (min)}$", fontsize=14)
ax.set_ylabel(r"$10^3 [I_2] \text{ (mol/L)}$", fontsize=14)
ax.set_title(r"BAC 2013 SN - Exercice 1: Cinétique redox", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=12)
ax.set_xlim(0, 35)
ax.set_ylim(0, 12)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2013-SN-Ex1-kinetics.png",
    dpi=150,
)
print("Saved: BAC-2013-SN-Ex1-kinetics.png")
plt.close()
