#!/usr/bin/env python3
"""
BAC 2021 D - Exercice 2: Plan complexe - Points A, B, C, D et ensembles
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect("equal")

# Define points from 2021
A = -1j  # z_A = -i
B = -1 + 2j  # z_B = -1 + 2i
C = 2 + 3j  # z_C = 2 + 3i
D = 3  # z_D = 3

# Plot points
ax.plot(A.real, A.imag, "ro", markersize=10)
ax.plot(B.real, B.imag, "bo", markersize=10)
ax.plot(C.real, C.imag, "go", markersize=10)
ax.plot(D.real, D.imag, "mo", markersize=10)

# Labels
ax.annotate(
    "A(-i)",
    xy=(A.real, A.imag),
    xytext=(A.real - 0.4, A.imag - 0.3),
    fontsize=11,
    color="red",
)
ax.annotate(
    "B(-1+2i)",
    xy=(B.real, B.imag),
    xytext=(B.real - 0.8, B.imag + 0.2),
    fontsize=11,
    color="blue",
)
ax.annotate(
    "C(2+3i)",
    xy=(C.real, C.imag),
    xytext=(C.real + 0.2, C.imag + 0.2),
    fontsize=11,
    color="green",
)
ax.annotate(
    "D(3)",
    xy=(D.real, D.imag),
    xytext=(D.real + 0.2, D.imag - 0.3),
    fontsize=11,
    color="purple",
)

# Draw quadrilateral ABCD
ax.plot(
    [A.real, B.real, C.real, D.real, A.real],
    [A.imag, B.imag, C.imag, D.imag, A.imag],
    "purple",
    linewidth=1.5,
)

# Ensemble Gamma1: |f(z)| = 1 -> cercle de centre C, rayon 1
theta = np.linspace(0, 2 * np.pi, 100)
(circle,) = ax.plot(
    C.real + np.cos(theta),
    C.imag + np.sin(theta),
    "orange",
    linewidth=1.5,
    label=r"$\Gamma_1$: $|f(z)|=1$",
)

# Axes
ax.axhline(y=0, color="black", linewidth=0.8)
ax.axvline(x=0, color="black", linewidth=0.8)

ax.set_xlabel(r"$\Re(z)$", fontsize=14)
ax.set_ylabel(r"$\Im(z)$", fontsize=14)
ax.set_title(r"BAC 2021 D - Exercice 2: Plan complexe", fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=10)

ax.set_xlim(-3, 5)
ax.set_ylim(-2, 5)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2021-D-Ex2.png",
    dpi=150,
)
print("Saved: BAC-2021-D-Ex2.png")
plt.close()
