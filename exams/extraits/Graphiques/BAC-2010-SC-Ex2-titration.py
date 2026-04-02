#!/usr/bin/env python3
"""
BAC 2010 SC - Exercice 2: pH titration curve
pH = f(V_b) for weak acid titration
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

V_b = np.array([0, 5, 10, 13, 22, 24, 28, 29, 31, 34, 36])
pH = np.array([2.4, 3.4, 3.6, 3.7, 4.0, 4.3, 5.0, 5.5, 10.9, 11.4, 11.5])

ax.plot(V_b, pH, "b-o", linewidth=2, markersize=8)

ax.axhline(y=7, color="gray", linestyle="--", linewidth=1, alpha=0.7)
ax.axvline(x=30, color="red", linestyle=":", linewidth=1, alpha=0.5)

ax.annotate(r"$V_E = 30 \text{ mL}$", xy=(30, 5), xytext=(25, 6), fontsize=12)
ax.annotate(r"$pK_a = 3{,}8$", xy=(13, 3.7), xytext=(15, 4.5), fontsize=12)

ax.set_xlabel(r"$V_b \text{ (mL)}$", fontsize=14)
ax.set_ylabel(r"$pH$", fontsize=14)
ax.set_title(r"BAC 2010 SC - Exercice 2: $pH = f(V_b)$", fontsize=16)

ax.grid(True, alpha=0.3)
ax.set_xlim(0, 40)
ax.set_ylim(2, 12)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2010-SC-Ex2-titration.png",
    dpi=150,
)
print("Saved: BAC-2010-SC-Ex2-titration.png")
plt.close()
