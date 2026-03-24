#!/usr/bin/env python3
"""
BAC 2024 D - Exercice 4: Plan complexe - Points A, B, C, I
"""

import numpy as np
import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Set equal aspect ratio
ax.set_aspect("equal")

# Define points
A = 3j  # z_A = 3i
B = 1  # z_B = 1
C = 4 + 1j  # z_C = 4 + i
I = 2 + 2j  # z_I = 2 + 2i (milieu de AC)

# Plot points
ax.plot(A.real, A.imag, "ro", markersize=10, label="A")
ax.plot(B.real, B.imag, "bo", markersize=10, label="B")
ax.plot(C.real, C.imag, "go", markersize=10, label="C")
ax.plot(I.real, I.imag, "mo", markersize=10, label="I")

# Add labels
ax.annotate(
    "A(3i)",
    xy=(A.real, A.imag),
    xytext=(A.real - 0.5, A.imag + 0.3),
    fontsize=12,
    color="red",
)
ax.annotate(
    "B(1)",
    xy=(B.real, B.imag),
    xytext=(B.real + 0.2, B.imag - 0.3),
    fontsize=12,
    color="blue",
)
ax.annotate(
    "C(4+i)",
    xy=(C.real, C.imag),
    xytext=(C.real + 0.2, C.imag + 0.2),
    fontsize=12,
    color="green",
)
ax.annotate(
    "I(2+2i)",
    xy=(I.real, I.imag),
    xytext=(I.real + 0.2, I.imag + 0.2),
    fontsize=12,
    color="purple",
)

# Draw segments
ax.plot([A.real, C.real], [A.imag, C.imag], "gray", linewidth=1, linestyle="--")
ax.plot([B.real, I.real], [B.imag, I.imag], "blue", linewidth=1.5)

# Axes
ax.axhline(y=0, color="black", linewidth=0.8)
ax.axvline(x=0, color="black", linewidth=0.8)

# Labels
ax.set_xlabel(r"$\Re(z)$", fontsize=14)
ax.set_ylabel(r"$\Im(z)$", fontsize=14)
ax.set_title(
    r"BAC 2024 D - Exercice 4: Plan complexe (z_I = $2\sqrt{2}e^{i\pi/4}$)", fontsize=16
)

# Grid
ax.grid(True, alpha=0.3)

# Legend
ax.legend(loc="upper right", fontsize=12)

# Set limits
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)

# Save
plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2024-D-Ex4.png",
    dpi=150,
)
print("Saved: BAC-2024-D-Ex4.png")
plt.close()
