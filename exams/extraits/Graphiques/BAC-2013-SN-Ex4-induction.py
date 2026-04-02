#!/usr/bin/env python3
"""
BAC 2013 SN - Exercice 4: Induction
B and e vs time (piecewise linear)
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

t = np.array([0, 2, 4, 6, 8, 10, 12])
B = np.array([0.5, 0.5, 1.0, 1.0, 0.5, 0.5, 0.5]) * 1e-3
e = np.array([0, 0, -0.5, 0, 0.5, 0, 0]) * 1e-3

ax.plot(t, B * 1000, "b-o", linewidth=2, markersize=8, label=r"$B \text{ (mT)}$")
ax.plot(t, e * 1000, "r-s", linewidth=2, markersize=8, label=r"$e \text{ (mV)}$")

ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.5)

ax.set_xlabel(r"$t \text{ (s)}$", fontsize=14)
ax.set_ylabel(r"$\text{Valeur}$", fontsize=14)
ax.set_title(r"BAC 2013 SN - Exercice 4: Induction", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=12)
ax.set_xlim(0, 12)
ax.set_ylim(-1, 1.5)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2013-SN-Ex4-induction.png",
    dpi=150,
)
print("Saved: BAC-2013-SN-Ex4-induction.png")
plt.close()
