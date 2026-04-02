#!/usr/bin/env python3
"""
BAC 2014 SN - Exercice 2: Esterification kinetics
n_ester vs t
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

t_data = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
n_ester_data = np.array([0, 0.04, 0.065, 0.085, 0.10, 0.11, 0.115, 0.12, 0.12])

ax.plot(
    t_data, n_ester_data, "b-o", linewidth=2, markersize=8, label=r"$n_{\text{ester}}$"
)

ax.axhline(y=0.12, color="gray", linestyle="--", linewidth=1, alpha=0.7)

ax.set_xlabel(r"$t \text{ (min)}$", fontsize=14)
ax.set_ylabel(r"$n_{\text{ester}} \text{ (mol)}$", fontsize=14)
ax.set_title(r"BAC 2014 SN - Exercice 2: Cinétique d'estérification", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=12)
ax.set_xlim(0, 90)
ax.set_ylim(0, 0.15)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2014-SN-Ex2-esterification.png",
    dpi=150,
)
print("Saved: BAC-2014-SN-Ex2-esterification.png")
plt.close()
