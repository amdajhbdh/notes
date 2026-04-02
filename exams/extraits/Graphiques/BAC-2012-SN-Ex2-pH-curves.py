#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# BAC 2012 SN - Exercice 2: Courbes de dosage pH = f(V)
# Courbe 1: Base forte (NaOH) - pH commence haut, équivalence à pH=7
# Courbe 2: Base faible (NH3) - pH commence haut, équivalence à pH<7

# Base forte: pH = -log(C*V/(V0+V)) avant équivalence, puis pH monte vite
V_acid = np.linspace(0, 20, 200)
C_base = 0.01  # mol/L
V_base = 10e-3  # L
C_acid = 0.01  # mol/L

# Simulation approximative des courbes de dosage
# Base forte (courbe 1)
V_eq1 = 8  # mL
pH_strong = []
for V in V_acid:
    if V < V_eq1:
        # Avant équivalence
        pH = 14 + np.log10(C_base * V_base / (V_base + V / 1000))
    else:
        # Après équivalence
        pH = -np.log10(C_acid * (V / 1000 - V_base) / (V_base + V / 1000))
    pH_strong.append(pH)

# Base faible (courbe 2)
V_eq2 = 10  # mL
pKa = 9.2
pH_weak = []
for V in V_acid:
    if V < V_eq2:
        # Avant équivalence - approximation avec Henderson
        ratio = V / (V_eq2 - V)
        if ratio > 0:
            pH = pKa + np.log10(ratio)
        else:
            pH = 14
    elif V == V_eq2:
        pH = 7  # Simplifié
    else:
        # Après équivalence
        pH = -np.log10(C_acid * (V / 1000 - V_base) / (V_base + V / 1000))
    pH_weak.append(min(max(pH, 0), 14))

plt.figure(figsize=(10, 6))
plt.plot(V_acid, pH_strong, "b-", linewidth=2, label=r"Base forte $B_1$")
plt.plot(V_acid, pH_weak, "r-", linewidth=2, label=r"Base faible $B_2$")
plt.axhline(y=7, color="gray", linestyle="--", alpha=0.5, label="pH = 7")
plt.axvline(x=8, color="blue", linestyle=":", alpha=0.5)
plt.axvline(x=10, color="red", linestyle=":", alpha=0.5)
plt.xlabel(r"Volume d\'acide ajouté $V$ (mL)", fontsize=12)
plt.ylabel("pH", fontsize=12)
plt.title(r"BAC 2012 SN - Ex2: Courbes de dosage acido-basique", fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 20)
plt.ylim(0, 14)
plt.tight_layout()
plt.savefig("BAC-2012-SN-Ex2-pH-curves.png", dpi=150)
plt.close()
