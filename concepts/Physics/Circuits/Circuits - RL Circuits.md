# Circuits - RL Circuits

> Comportement transitoire dans les circuits résistif-inductifs

## 1. Configuration de Base

Un circuit RL comprend :
- Une **résistance** $R$ (Ω)
- Une **inductance** $L$ (H)
- Une source continue $E$ (V)
- Un interrupteur avec deux positions :
  - **Position ①** : Connexion à la source (charge)
  - **Position ②** : Boucle fermée (décharge)

## 2. Phase de Charge

### Équation Différentielle

$$L \frac{di}{dt} + Ri = E$$

### Solution

$$i(t) = \frac{E}{R} \left(1 - e^{-t/\tau}\right)$$

$$u_R(t) = E \left(1 - e^{-t/\tau}\right) \quad u_L(t) = E e^{-t/\tau}$$

### Courbe Caractéristique
![RL Charge Curve](images/rl-charge-graph.png)

- **Temps initial** ($t=0$) : $i=0$, $u_L=E$
- **Régime permanent** ($t \to \infty$) : $i=E/R$, $u_L=0$
- **Constante de temps** : $\tau = L/R$

## 3. Phase de Décharge

### Solution

$$i(t) = \frac{E}{R} e^{-t/\tau}$$

$$u_R(t) = E e^{-t/\tau} \quad u_L(t) = -E e^{-t/\tau}$$

### Courbe Caractéristique
![RL Discharge Curve](images/rl-discharge-graph.png)

- **Temps initial** ($t=0$) : $i=E/R$
- **Régime permanent** ($t \to \infty$) : $i=0$

## 4. Constante de Temps $\tau$

$$\tau = \frac{L}{R}$$

| Méthode                  | Description                                 |
|--------------------------|---------------------------------------------|
| **Tangente**             | Intersection avec asymptote à $t=\tau$      |
| **Point à point**        | $t$ où $i = 0.632 \times i_{\text{final}}$ |
| **Durée transitoire**    | $\Delta t \approx 5\tau$                 |

## 5. Ressources Éducatives

### Vidéos

- [Circuit RL - Explication détaillée (FR)](https://www.youtube.com/watch?v=4XxQ4x1dJ8k)
- [RL Transients Explained (EN)](https://www.youtube.com/watch?v=5B7kF1c0q7Q)

### Simulations

- [PhET Simulation - Circuit Construction Kit (EN)](https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html)
- [Simulation Interactif Circuit RL (FR)](https://www.feynmanlectures.caltech.edu/simulations.html)

## 6. Liens Utiles

- [Cours complet sur les circuits RL (EN)](https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/inductors-and-rl-time-constants/)
- [Fiche Méthode - Circuit RL (FR)](https://www.physique-chimie.fr/circuit-rl/)

## 7. Application Pratique

- **Bobines d'allumage** : Utilisent l'induction pour générer des hautes tensions
- **Protections contre surtensions** : Absorbent l'énergie stockée dans $L$
- **Relais électromagnétiques** : Temps de réponse contrôlé par $\tau$

## 8. Documentation Technique

| Concept          | Formules                                      | Application Pratique             |
|------------------|-----------------------------------------------|----------------------------------|
| **Charge**       | $i(t) = I_0(1 - e^{-t/\tau})$              | Démarrage de moteurs           |
| **Décharge**     | $i(t) = I_0 e^{-t/\tau}$                   | Génération d'étincelles        |
| **Temps de charge** | $t_{\text{charge}} \approx 5\tau$      | Calcul du délai de sécurité    |

## 9. Exemples Numériques

**Exemple 1 : Calcul de $\tau$**
- $L = 50 \text{ mH}$, $R = 200 \Omega$ → $\tau = \frac{50 \times 10^{-3}}{200} = 0.25 \text{ ms}$
- Après $0.25 \text{ ms}$ : $i = 63.2\%$ de la valeur finale

**Exemple 2 : Tension maximale**
- $E = 12 \text{ V}$, $R = 100 \Omega$ → $i_{max} = 0.12 \text{ A}$
- $u_L(0) = 12 \text{ V}$, $u_R(0) = 0 \text{ V}$

## 10. Comparaison RL vs RC

| Caractéristique | Circuit RL                      | Circuit RC                      |
|-----------------|-----------------------------------|-----------------------------------|
| **Élément**     | Inductance $L$                 | Capacité $C$                   |
| **Constante**   | $\tau = L/R$                 | $\tau = RC$                   |
| **Charge**      | $i(t) = I_0(1 - e^{-t/\tau})$ | $u(t) = U_0(1 - e^{-t/\tau})$ |
| **Décharge**    | $i(t) = I_0 e^{-t/\tau}$     | $u(t) = U_0 e^{-t/\tau}$     |

## 11. Ressources Complémentaires

### Cours Académiques
- [École Polytechnique - Électromagnétisme (FR)](https://www.polytechnique.edu/fr/cours-electromagnetisme)
- [MIT OpenCourseWare - Circuits (EN)](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)

### Génération de Courbes
Exécutez ce script pour générer les graphes :
```python
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
E = 12; R = 1000; L = 0.1; tau = L/R

t = np.linspace(0, 5*tau, 1000)

# Charge
i_charge = (E/R)*(1 - np.exp(-t/tau))
plt.figure(figsize=(8,5))
plt.plot(t, i_charge, 'b-', label='$i(t)$')
plt.axvline(x=tau, color='r', linestyle='--', alpha=0.7)
plt.title('Charge du Circuit RL ($\\tau = {:.1f}$ ms)'.format(tau*1000))
plt.xlabel('Temps (s)'); plt.ylabel('Intensité (A)')
plt.grid(True); plt.legend()
plt.savefig('images/rl-charge-graph.png', dpi=300)

# Décharge
i_discharge = (E/R)*np.exp(-t/tau)
plt.figure(figsize=(8,5))
plt.plot(t, i_discharge, 'b-', label='$i(t)$')
plt.axvline(x=tau, color='r', linestyle='--', alpha=0.7)
plt.title('Décharge du Circuit RL ($\\tau = {:.1f}$ ms)'.format(tau*1000))
plt.xlabel('Temps (s)'); plt.ylabel('Intensité (A)')
plt.grid(True); plt.legend()
plt.savefig('images/rl-discharge-graph.png', dpi=300)
```

## 12. Glossaire Bilingue

| Français                     | English                      |
|------------------------------|------------------------------|
| Régime transitoire           | Transient regime             |
| Constante de temps           | Time constant                |
| Bobine d'inductance          | Inductor coil                |
| Démarrage progressif         | Gradual startup              |