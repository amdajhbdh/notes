import numpy as np
import matplotlib.pyplot as plt

# Constants
E = 10.0  # Volts
R = 100.0 # Ohms
t = np.linspace(0, 0.05, 1000)
output_dir = "01-Concepts/Physics/Dipole-RL/assets/"

# 1. Comparison of Tau (Effect of L)
plt.figure(figsize=(10, 6))
for L, color in zip([0.2, 0.5, 1.5], ['blue', 'red', 'green']):
    tau = L / R
    i = (E/R) * (1 - np.exp(-t/tau))
    plt.plot(t, i, label=f'L = {L}H (τ = {tau*1000:.1f}ms)', color=color)

plt.title("Influence de l'inductance L sur l'établissement du courant", fontsize=14)
plt.xlabel("Temps (s)")
plt.ylabel("Intensité i(t) (A)")
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.savefig(f"{output_dir}comparaison_tau.png")
plt.close()

# 2. Power and Energy during Charging
L_fixed = 0.5
tau_fixed = L_fixed / R
i_fixed = (E/R) * (1 - np.exp(-t/tau_fixed))
u_L_fixed = E * np.exp(-t/tau_fixed)

p_L = u_L_fixed * i_fixed # Power absorbed by inductor
energy = 0.5 * L_fixed * i_fixed**2 # Energy stored

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Temps (s)')
ax1.set_ylabel('Puissance P_L (W)', color=color)
ax1.plot(t, p_L, color=color, label='Puissance instantanée P_L(t)')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Énergie E_m (J)', color=color)
ax2.plot(t, energy, color=color, linestyle='--', label='Énergie emmagasinée E_m(t)')
ax2.tick_params(axis='y', labelcolor=color)

plt.title("Bilan Énergétique lors de la Charge", fontsize=14)
fig.tight_layout()
plt.grid(True, alpha=0.3)
plt.savefig(f"{output_dir}bilan_energetique.png")
plt.close()
