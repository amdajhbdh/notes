#!/usr/bin/env python3
"""
BAC 2024 D - Exercice 3: Courbe de f(x) = x - 3 + (1/2)e^x
"""

import numpy as np
import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))

# Generate x values
x = np.linspace(-4, 4, 1000)


# Function f(x) = x - 3 + 0.5*e^x
def f(x):
    return x - 3 + 0.5 * np.exp(x)


# Calculate y values
y = f(x)

# Plot function
ax.plot(x, y, "b-", linewidth=2, label=r"$\Gamma: f(x) = x - 3 + \frac{1}{2}e^x$")

# Asymptote oblique D: y = x - 3
x_asymp = np.linspace(-4, 5, 100)
y_asymp = x_asymp - 3
ax.plot(x_asymp, y_asymp, "r--", linewidth=1.5, label=r"$D: y = x - 3$")

# Mark alpha (solution of f(x)=0)
ax.plot(1.25, 0, "ro", markersize=8)
ax.annotate(
    r"$\alpha \approx 1.25$", xy=(1.25, 0), xytext=(0.8, 0.8), fontsize=12, color="red"
)

# Axes
ax.axhline(y=0, color="black", linewidth=0.5)
ax.axvline(x=0, color="black", linewidth=0.5)

# Labels
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$y$", fontsize=14)
ax.set_title(r"BAC 2024 D - Exercice 3: $f(x) = x - 3 + \frac{1}{2}e^x$", fontsize=16)

# Grid
ax.grid(True, alpha=0.3)

# Legend
ax.legend(loc="upper left", fontsize=12)

# Set limits
ax.set_xlim(-4, 5)
ax.set_ylim(-5, 10)

# Save
plt.tight_layout()
plt.savefig(
    "/home/med/Documents/bac/notes/04-Exams/BAC-Extraits/Graphiques/BAC-2024-D-Ex3.png",
    dpi=150,
)
print("Saved: BAC-2024-D-Ex3.png")
plt.close()
