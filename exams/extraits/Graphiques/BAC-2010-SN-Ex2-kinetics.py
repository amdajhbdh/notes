#!/usr/bin/env python3
"""
BAC 2010 SN - Exercice 2: Esterification kinetics
Mixture M1 (without catalyst) and M2 (with catalyst)
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

t = np.array([0, 5, 10, 20, 30, 40, 50, 60])
n_a_M1 = np.array([1.0, 0.84, 0.74, 0.64, 0.58, 0.54, 0.52, 0.50])
n_a_M2 = np.array([1.0, 0.53, 0.37, 0.35, 0.34, 0.34, 0.34, 0.34])

n_e_M1 = 1.0 - n_a_M1
n_e_M2 = 1.0 - n_a_M2

ax.plot(
    t,
    n_e_M1,
    "b-o",
    linewidth=2,
    markersize=8,
    label=r"$M_1 \text{ (sans cataliseur)}$",
)
ax.plot(
    t,
    n_e_M2,
    "r-s",
    linewidth=2,
    markersize=8,
    label=r"$M_2 \text{ (avec cataliseur)}$",
)

ax.axhline(y=1.0, color="gray", linestyle="--", linewidth=1, alpha=0.7)
ax.axhline(y=0.66, color="gray", linestyle=":", linewidth=1, alpha=0.5)

ax.set_xlabel(r"$t \text{ (min)}$", fontsize=14)
ax.set_ylabel(r"$n_e \text{ (mol)}$", fontsize=14)
ax.set_title(r"BAC 2010 SN - Exercice 2: Cinétique d'estérification", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=12)
ax.set_xlim(0, 65)
ax.set_ylim(0, 1.1)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2010-SN-Ex2-kinetics.png",
    dpi=150,
)
print("Saved: BAC-2010-SN-Ex2-kinetics.png")
plt.close()
