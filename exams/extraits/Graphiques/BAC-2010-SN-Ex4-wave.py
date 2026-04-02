#!/usr/bin/env python3
"""
BAC 2010 SN - Exercice 4: Wave on a string
Sinusoidal wave at t = 0.05s
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

N = 50
a = 0.005
C = 5
lambda_wave = C / N

x = np.linspace(0, 0.5, 500)
t = 0.05

y = a * np.cos(2 * np.pi * N * t - 2 * np.pi * x / lambda_wave)

ax.plot(x * 100, y * 100, "b-", linewidth=2, label=r"$t = 0{,}05 \text{ s}$")

ax.set_xlabel(r"$x \text{ (cm)}$", fontsize=14)
ax.set_ylabel(r"$y \text{ (cm)}$", fontsize=14)
ax.set_title(r"BAC 2010 SN - Exercice 4: Onde sur une corde", fontsize=16)

ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=12)
ax.set_xlim(0, 50)
ax.set_ylim(-1, 1)

plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2010-SN-Ex4-wave.png",
    dpi=150,
)
print("Saved: BAC-2010-SN-Ex4-wave.png")
plt.close()
