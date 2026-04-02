import numpy as np
import matplotlib.pyplot as plt

# Constants
E = 10.0  # EMF in Volts
R = 100.0 # Resistance in Ohms
L = 0.5   # Inductance in Henrys
tau = L / R
I_max = E / R
t = np.linspace(0, 5 * tau, 500)

# Directory
output_dir = "01-Concepts/Physics/Dipole-RL/assets/"

# 1. Charging: Current i(t)
plt.figure(figsize=(8, 6))
i_charge = I_max * (1 - np.exp(-t / tau))
plt.plot(t, i_charge, label=r'$i(t) = \frac{E}{R}(1 - e^{-t/\tau})$', color='blue', linewidth=2)
plt.axhline(I_max, color='green', linestyle='--', label=r'$I_{max} = E/R$')
# Tangent at t=0: y = (I_max/tau) * t
tangent = (I_max / tau) * t
plt.plot(t[t <= 1.2*tau], tangent[t <= 1.2*tau], color='red', linestyle='--', label='Tangente à t=0')
plt.axvline(tau, color='orange', linestyle='--', label=r'$\tau = L/R$')
plt.plot(tau, 0.632 * I_max, 'ro')
plt.text(tau, 0.632 * I_max, r' $0.63 I_{max}$', verticalalignment='bottom')

plt.title("Établissement du courant (Charge)", fontsize=14)
plt.xlabel("Temps (s)", fontsize=12)
plt.ylabel("Intensité i(t) (A)", fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig(f"{output_dir}charge_intensite.png")
plt.close()

# 2. Charging: Voltages u_R(t) and u_L(t)
plt.figure(figsize=(8, 6))
u_R_charge = R * i_charge
u_L_charge = E * np.exp(-t / tau)
plt.plot(t, u_R_charge, label=r'$u_R(t)$', color='blue')
plt.plot(t, u_L_charge, label=r'$u_L(t)$', color='red')
plt.axhline(E, color='green', linestyle='--', label='E')
plt.axvline(tau, color='orange', linestyle='--')

plt.title("Tensions lors de la charge", fontsize=14)
plt.xlabel("Temps (s)", fontsize=12)
plt.ylabel("Tension (V)", fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig(f"{output_dir}charge_tensions.png")
plt.close()

# 3. Discharging: Current i(t)
plt.figure(figsize=(8, 6))
i_discharge = I_max * np.exp(-t / tau)
plt.plot(t, i_discharge, label=r'$i(t) = I_0 e^{-t/\tau}$', color='blue', linewidth=2)
# Tangent at t=0: y = I_max - (I_max/tau) * t
tangent_dis = I_max - (I_max / tau) * t
plt.plot(t[t <= 1.2*tau], tangent_dis[t <= 1.2*tau], color='red', linestyle='--', label='Tangente à t=0')
plt.axvline(tau, color='orange', linestyle='--', label=r'$\tau = L/R$')
plt.plot(tau, 0.368 * I_max, 'ro')
plt.text(tau, 0.368 * I_max, r' $0.37 I_{0}$', verticalalignment='bottom')

plt.title("Rupture du courant (Décharge)", fontsize=14)
plt.xlabel("Temps (s)", fontsize=12)
plt.ylabel("Intensité i(t) (A)", fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig(f"{output_dir}decharge_intensite.png")
plt.close()

# 4. Discharging: Voltages u_R(t) and u_L(t)
plt.figure(figsize=(8, 6))
u_R_discharge = R * i_discharge
u_L_discharge = -R * i_discharge # u_L + u_R = 0 => u_L = -u_R
plt.plot(t, u_R_discharge, label=r'$u_R(t)$', color='blue')
plt.plot(t, u_L_discharge, label=r'$u_L(t)$', color='red')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(tau, color='orange', linestyle='--')

plt.title("Tensions lors de la décharge", fontsize=14)
plt.xlabel("Temps (s)", fontsize=12)
plt.ylabel("Tension (V)", fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig(f"{output_dir}decharge_tensions.png")
plt.close()
