# 🎯 Leçon Magistrale : Le Dipôle RL (Format BAC Excellence)

> [!abstract] Sommaire
> 1. **Introduction Physique** : Bobines et Auto-induction.
> 2. **Réponse à un Échelon de Tension** (Charge).
> 3. **Analyse de la Constante de Temps $\tau$** (Analyse Dimensionnelle).
> 4. **Rupture du Courant** (Décharge & Roue Libre).
> 5. **Bilan Énergétique** (Énergie Magnétique).
> 6. **Aspects Expérimentaux** (Oscilloscopie).

---

## 1. Fondements Physiques : La Bobine et l'Auto-induction

Une bobine est un composant inductif qui s'oppose à toute variation de l'intensité du courant qui la traverse. Ce phénomène est régi par la **Loi de Lenz**.

> [!theory] Loi de Lenz (Auto-induction)
> La variation du flux magnétique à travers les spires de la bobine induit une force électromotrice (f.e.m) qui tend, par ses effets, à s'opposer à la cause qui lui a donné naissance (la variation du courant).
> 
> **Relation fondamentale :**
> $$u_L(t) = L \cdot \frac{di(t)}{dt} + r \cdot i(t)$$
> - $L$ : Inductance (en Henry $H$).
> - $r$ : Résistance interne (en Ohm $\Omega$).
> - Si $r \approx 0$ (bobine idéale) : $u_L = L \cdot \frac{di}{dt}$.

---

## 2. Établissement du Courant (Réponse à un Échelon $E$)

Le circuit est composé d'un générateur de tension $E$, d'une résistance $R$ et d'une bobine $(L, r)$ en série. L'interrupteur est fermé à $t=0$.

### 2.1 Équation Différentielle
Loi d'additivité des tensions (Loi des mailles) :
$$u_L + u_R = E \implies L \cdot \frac{di}{dt} + r \cdot i + R \cdot i = E$$

En posant $R_{total} = R + r$, on obtient :
$$L \cdot \frac{di}{dt} + R_{total} \cdot i = E$$

En divisant par $R_{total}$ :
$$\frac{L}{R_{total}} \cdot \frac{di}{dt} + i = \frac{E}{R_{total}}$$

> [!formula] Constante de Temps $\tau$
> On pose $\tau = \frac{L}{R_{total}}$. L'équation différentielle s'écrit alors :
> $$\tau \cdot \frac{di}{dt} + i = I_0 \quad \text{avec } I_0 = \frac{E}{R_{total}}$$

### 2.2 Solution et Vérification
La solution de cette équation est :
$$\boxed{i(t) = I_0 \cdot \left( 1 - e^{-\frac{t}{\tau}} \right)}$$

> [!success] Vérification de la solution
> - À $t=0$ : $i(0) = I_0(1 - e^0) = 0$. (Continuité du courant).
> - Pour $t \to \infty$ : $i(\infty) = I_0(1 - 0) = I_0$. (Régime permanent).
> - Dérivée : $\frac{di}{dt} = I_0 \cdot \frac{1}{\tau} \cdot e^{-t/\tau}$.
> - Substitution : $\tau \cdot (I_0/\tau \cdot e^{-t/\tau}) + I_0(1 - e^{-t/\tau}) = I_0 \cdot e^{-t/\tau} + I_0 - I_0 \cdot e^{-t/\tau} = I_0$. (Vérifié).

---

## 3. Analyse Dimensionnelle de $\tau$

> [!theory] Démontrer que $[\tau] = T$
> 1. D'après la Loi d'Ohm : $U = R \cdot I \implies [R] = \frac{[U]}{[I]}$.
> 2. D'après la relation bobine : $u_L = L \cdot \frac{di}{dt} \implies [L] = [U] \cdot \frac{[T]}{[I]}$.
> 3. Calcul de $[\tau] = \frac{[L]}{[R]}$ :
> $$[\tau] = \frac{[U] \cdot [T] / [I]}{[U] / [I]} = [T]$$
> La constante $\tau$ est bien homogène à un temps.

---

## 4. Rupture du Courant et Diode de Roue Libre

Lorsque l'on ouvre brusquement l'interrupteur dans un circuit RL sans précaution, une **surtension** importante apparaît ($L \cdot di/dt$ très grand), créant un arc électrique (étincelle de rupture) qui peut endommager le matériel.

> [!danger] Protection par Diode de Roue Libre
> Pour protéger le circuit, on branche une diode en parallèle avec la bobine.
> - **En charge** : La diode est bloquée (elle ne laisse pas passer le courant).
> - **À l'ouverture** : La bobine devient un générateur. La diode devient passante (roue libre) et permet au courant de circuler dans une boucle fermée jusqu'à dissipation complète de l'énergie.
> 
> **Équation de décharge (régime libre) :**
> $$\tau \cdot \frac{di}{dt} + i = 0 \implies i(t) = I_0 \cdot e^{-\frac{t}{\tau}}$$

---

## 5. Bilan Énergétique

La bobine emmagasine de l'énergie sous forme magnétique. Elle ne peut pas absorber ou libérer cette énergie instantanément, ce qui explique la continuité de l'intensité $i(t)$.

> [!formula] Énergie Magnétique
> $$E_m(t) = \frac{1}{2} \cdot L \cdot i(t)^2$$
> - $E_m$ en Joule ($J$).
> - $L$ en Henry ($H$).
> - $i$ en Ampère ($A$).

En régime permanent ($i = I_0$) :
$$E_{m\_max} = \frac{1}{2} \cdot L \cdot \left( \frac{E}{R_{total}} \right)^2$$

---

## 6. Aspects Expérimentaux (Oscilloscopie)

Pour visualiser $i(t)$, on visualise en réalité $u_R(t)$ car $u_R = R \cdot i$.
- **Voie 1 (Y1)** : Visualise la tension aux bornes du dipôle RL ($E$).
- **Voie 2 (Y2)** : Visualise la tension aux bornes de la résistance ($u_R$).
- **Inversion** : Si la résistance est "sous" la bobine par rapport à la masse, il faut parfois inverser le signal (bouton "INV") pour observer $i(t)$ positivement.

> [!practice] Fiche de Révision Flash
> - **$\tau = L/R$** : Constante de temps (63% de charge).
> - **Continuité** : $i(0^-) = i(0^+)$.
> - **Lissage** : La bobine lisse le courant.
> - **Comportement final** : Fil conducteur (si $r=0$).

---
*Généré pour le Vault de Préparation BAC Excellence 2026*
