#!/usr/bin/env python3
"""
BAC 2025 D - Exercice 2: Plan complexe - Points A, B, C
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Set equal aspect ratio
ax.set_aspect("equal")

# Define points
A = 1 - 1j  # z_A = 1 - i
B = 2 + 2j  # z_B = 2 + 2i
C = -1 + 3j  # z_C = -1 + 3i

# Plot points
ax.plot(A.real, A.imag, "ro", markersize=10, label="A")
ax.plot(B.real, B.imag, "bo", markersize=10, label="B")
ax.plot(C.real, C.imag, "go", markersize=10, label="C")

# Add labels
ax.annotate(
    "A(1-i)",
    xy=(A.real, A.imag),
    xytext=(A.real + 0.2, A.imag - 0.3),
    fontsize=12,
    color="red",
)
ax.annotate(
    "B(2+2i)",
    xy=(B.real, B.imag),
    xytext=(B.real + 0.2, B.imag + 0.2),
    fontsize=12,
    color="blue",
)
ax.annotate(
    "C(-1+3i)",
    xy=(C.real, C.imag),
    xytext=(C.real - 0.8, C.imag + 0.2),
    fontsize=12,
    color="green",
)

# Draw triangle
triangle = plt.Polygon(
    [(A.real, A.imag), (B.real, B.imag), (C.real, C.imag)],
    fill=False,
    edgecolor="purple",
    linewidth=2,
)
ax.add_patch(triangle)

# Axes
ax.axhline(y=0, color="black", linewidth=0.8)
ax.axvline(x=0, color="black", linewidth=0.8)

# Labels
ax.set_xlabel(r"$\Re(z)$", fontsize=14)
ax.set_ylabel(r"$\Im(z)$", fontsize=14)
ax.set_title(r"BAC 2025 D - Exercice 2: Plan complexe", fontsize=16)

# Grid
ax.grid(True, alpha=0.3)

# Legend
ax.legend(loc="upper right", fontsize=12)

# Set limits
ax.set_xlim(-3, 4)
ax.set_ylim(-2, 4)

# Save
plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2025-D-Ex2.png",
    dpi=150,
)
print("Saved: BAC-2025-D-Ex2.png")
plt.close()
