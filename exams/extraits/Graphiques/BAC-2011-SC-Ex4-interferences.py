#!/usr/bin/env python3
"""
BAC 2011 SC - Exercice 4: Interferences
Interfrange i vs distance D
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

a = 2e-3
lambda_wl = 0.72e-6

D = np.linspace(1, 3, 500)
i_calc = lambda_wl * D / a

D1 = 1.5
i1 = 0.54e-3
D2 = 2.0
i2 = 0.72e-3

ax.plot(D * 1000, i_calc * 1000, "b-", linewidth=2, label=r"$i = \frac{\lambda D}{a}$")

ax.plot(D1 * 1000, i1 * 1000, "ro", markersize=10, label=r"$(D_1, i_1)$")
ax.plot(D2 * 1000, i2 * 1000, "go", markersize=10, label=r"$(D_2, i_2)$")

ax.axhline(y=0.72, color="gray", linestyle="--", linewidth=1, alpha=0.7)
ax.axvline(x=2000, color="gray", linestyle=":", linewidth=1, alpha=0.5)

ax.set_xlabel(r"$D \text{ (mm)}$", fontsize=14)
ax.set_ylabel(r"$i \text{ (mm)}$", fontsize=14)
ax.set_title(r"BAC 2011 SC - Exercice 4: Interférences", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=12)
ax.set_xlim(1000, 3000)
ax.set_ylim(0, 1.2)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2011-SC-Ex4-interferences.png",
    dpi=150,
)
print("Saved: BAC-2011-SC-Ex4-interferences.png")
plt.close()
