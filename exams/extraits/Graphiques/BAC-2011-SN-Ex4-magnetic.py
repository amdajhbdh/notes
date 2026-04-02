#!/usr/bin/env python3
"""
BAC 2011 SN - Exercice 4: Particle in magnetic field
Circular trajectory
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))

theta = np.linspace(0, 2 * np.pi, 500)
R = 0.177

x = R * np.sin(theta)
y = R * (1 - np.cos(theta))

ax.plot(x * 100, y * 100, "b-", linewidth=2)

a = 0.05
ax.plot([0, a * 100 * 2], [0, 0], "k-", linewidth=4)

ax.plot(0, 0, "ro", markersize=10, label=r"$O$")
ax.plot(a * 100 * 2, 0, "go", markersize=10, label=r"$A$")
ax.plot(0, a * 100, "bo", markersize=10, label=r"$D$")

ax.annotate(r"$O$", xy=(0, 0), xytext=(-10, -10), fontsize=14)
ax.annotate(r"$A$", xy=(a * 100 * 2, 0), xytext=(12, -10), fontsize=14)
ax.annotate(r"$D$", xy=(0, a * 100), xytext=(-20, 20), fontsize=14)

ax.set_xlabel(r"$x \text{ (cm)}$", fontsize=14)
ax.set_ylabel(r"$y \text{ (cm)}$", fontsize=14)
ax.set_title(r"BAC 2011 SN - Exercice 4: Particule chargée dans B", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=12)
ax.set_xlim(-5, 25)
ax.setylim(-5, 20)
ax.set_aspect("equal")

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2011-SN-Ex4-magnetic.png",
    dpi=150,
)
print("Saved: BAC-2011-SN-Ex4-magnetic.png")
plt.close()
