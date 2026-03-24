#!/usr/bin/env python3
"""
BAC 2025 D - Exercice 3: Courbe de f(x) = (e^x - x - 2)e^(-x)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))

# Generate x values
x = np.linspace(-5, 3, 1000)


# Function f(x) = (e^x - x - 2)*e^(-x) = 1 - (x+2)/e^x
def f(x):
    return (np.exp(x) - x - 2) * np.exp(-x)


# Calculate y values
y = f(x)

# Plot function
ax.plot(x, y, "b-", linewidth=2, label=r"$\Gamma: f(x) = (e^x - x - 2)e^{-x}$")

# Asymptote y = 1
ax.axhline(y=1, color="red", linestyle="--", linewidth=1.5, label=r"$D: y = 1$")

# Mark zeros (alpha and beta)
# f(x) = 0 when e^x - x - 2 = 0 => x = -2 is a root
# Second root is approximately 1.15
ax.plot(-2, 0, "ro", markersize=8)
ax.annotate(r"$\beta = -2$", xy=(-2, 0), xytext=(-2.5, 0.5), fontsize=12, color="red")

ax.plot(1.15, 0, "ro", markersize=8)
ax.annotate(
    r"$\alpha \approx 1.15$", xy=(1.15, 0), xytext=(0.8, 0.5), fontsize=12, color="red"
)

# Mark maximum at x = -1
ax.plot(-1, 1 / np.e, "go", markersize=8)
ax.annotate(
    r"$(-1, \frac{1}{e})$",
    xy=(-1, 1 / np.e),
    xytext=(-1.5, 1.5),
    fontsize=12,
    color="green",
)

# Axes
ax.axhline(y=0, color="black", linewidth=0.5)
ax.axvline(x=0, color="black", linewidth=0.5)

# Labels
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$y$", fontsize=14)
ax.set_title(r"BAC 2025 D - Exercice 3: $f(x) = (e^x - x - 2)e^{-x}$", fontsize=16)

# Grid
ax.grid(True, alpha=0.3)

# Legend
ax.legend(loc="upper left", fontsize=12)

# Set limits
ax.set_xlim(-5, 3)
ax.set_ylim(-3, 4)

# Save
plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2025-D-Ex3.png",
    dpi=150,
)
print("Saved: BAC-2025-D-Ex3.png")
plt.close()
