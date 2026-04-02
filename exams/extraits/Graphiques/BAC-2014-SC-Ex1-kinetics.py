#!/usr/bin/env python3
"""
BAC 2014 SC - Exercice 1: Kinetics of redox reaction
[I-] vs t for S2O8^2- + 2I- reaction
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

t = np.array([0, 10, 20, 30, 40, 50, 60])
I_minus = np.array([8, 6.5, 5.2, 4.2, 3.5, 3, 3]) * 1e-2

ax.plot(
    t, I_minus * 100, "b-o", linewidth=2, markersize=8, label=r"$[I^-] \times 10^2$"
)

ax.axhline(y=3, color="gray", linestyle="--", linewidth=1, alpha=0.7)

ax.set_xlabel(r"$t \text{ (min)}$", fontsize=14)
ax.set_ylabel(r"$10^2 [I^-] \text{ (mol/L)}$", fontsize=14)
ax.set_title(r"BAC 2014 SC - Exercice 1: Cinétique redox", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=12)
ax.set_xlim(0, 70)
ax.set_ylim(0, 9)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2014-SC-Ex1-kinetics.png",
    dpi=150,
)
print("Saved: BAC-2014-SC-Ex1-kinetics.png")
plt.close()
