#!/usr/bin/env python3
"""
BAC 2012 SN - Exercice 1: Kinetics of Mg + 2H3O+ reaction
[Mg2+] vs t at different temperatures
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

t = np.array([0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10])
Mg_30 = np.array([0, 1, 1.8, 2.5, 2.8, 3, 3, 3, 3, 3]) * 1e-2
Mg_20 = np.array([0, 0.5, 0.9, 1.5, 2, 2.3, 2.5, 2.7, 2.8, 2.9]) * 1e-2

t_fine = np.linspace(0, 10, 200)

from scipy.interpolate import interp1d

f_30 = interp1d(t, Mg_30, kind="cubic")
f_20 = interp1d(t, Mg_20, kind="cubic")

ax.plot(
    t,
    Mg_30 * 100,
    "b-o",
    linewidth=2,
    markersize=8,
    label=r"$\theta_1 = 30^\circ\text{C}$",
)
ax.plot(
    t,
    Mg_20 * 100,
    "r-s",
    linewidth=2,
    markersize=8,
    label=r"$\theta_2 = 20^\circ\text{C}$",
)

ax.axhline(y=3, color="gray", linestyle="--", linewidth=1, alpha=0.7)

ax.set_xlabel(r"$t \text{ (min)}$", fontsize=14)
ax.set_ylabel(r"$10^2 [Mg^{2+}] \text{ (mol/L)}$", fontsize=14)
ax.set_title(r"BAC 2012 SN - Exercice 1: Cinétique chimique", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=12)
ax.set_xlim(0, 11)
ax.set_ylim(0, 3.5)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2012-SN-Ex1-kinetics.png",
    dpi=150,
)
print("Saved: BAC-2012-SN-Ex1-kinetics.png")
plt.close()
