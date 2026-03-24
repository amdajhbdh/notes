# 📝 Résolution Détaillée : Exercice 12 (Carré & Similitude)

> [!question] Énoncé (Résumé)
> Soit un carré direct $ABCD$ de centre $I$. $J, K, L$ milieux de $[AB], [CD], [DA]$.
> On étudie la similitude directe $s$ telle que $s(A) = I$ et $s(B) = K$.

---

## 🧩 Partie A : Approche Géométrique

### 1. Détermination du rapport $k$ et de l'angle $\theta$
- **Le rapport $k$** : 
  $k = \frac{IK}{AB}$. 
  Dans un carré de côté $c$, $AB = c$ et $IK = c/2$ (car $I$ est le centre et $K$ le milieu du côté opposé).
  Donc $k = \frac{c/2}{c} = \frac{1}{2}$.
- **L'angle $\theta$** : 
  C'est l'angle $(\vec{AB}, \vec{IK})$. 
  $\vec{AB}$ est horizontal vers la droite. $\vec{IK}$ est vertical vers le haut (dans un carré direct).
  Donc $\theta \equiv \frac{\pi}{2} \pmod{2\pi}$.

### 2. Construction du centre $\Omega$
Le centre $\Omega$ est l'intersection des cercles $\Gamma_1$ (diamètre $[AI]$) et $\Gamma_2$ (diamètre $[BK]$).
*Justification :* Comme l'angle est $\pi/2$, le triangle $A\Omega I$ est rectangle en $\Omega$, donc $\Omega$ est sur le cercle de diamètre $[AI]$. Idem pour $B\Omega K$.

---

## 🔢 Partie B : Approche Analytique (Complexes)

On pose $A(0,0)$, $B(10,0)$, $C(10,10)$ et $D(0,10)$.
Milieux : $I(5,5)$, $J(5,0)$, $K(5,10)$, $L(0,5)$.

### 1. Écriture complexe de $s$
La forme est $z' = az + b$.
- $s(A) = I \implies b = 5 + 5i$.
- $s(B) = K \implies a(10) + (5+5i) = 5 + 10i$
  $10a = 5i \implies a = \frac{1}{2}i$.

**L'équation est :** $\boxed{z' = \frac{1}{2}iz + 5 + 5i}$

### 2. Éléments caractéristiques (Vérification)
- **Rapport** : $k = |a| = |i/2| = 1/2$. (Cohérent avec la Partie A).
- **Angle** : $\theta = \arg(a) = \arg(i/2) = \pi/2$. (Cohérent).
- **Centre $\Omega$** : On résout $z = \frac{1}{2}iz + 5 + 5i$
  $z(1 - \frac{1}{2}i) = 5 + 5i$
  $z = \frac{10 + 10i}{2 - i} = \frac{(10 + 10i)(2 + i)}{5} = \frac{20 + 10i + 20i - 10}{5} = \frac{10 + 30i}{5} = 2 + 6i$.
  $\boxed{\Omega(2, 6)}$

---

## 💡 Ce qu'il faut retenir pour le BAC
1. Toujours identifier les images de deux points pour trouver $a$ et $b$.
2. Le centre $\Omega$ est le seul point invariant ($f(\Omega) = \Omega$).
3. Utiliser les milieux pour simplifier les coordonnées.

---
*Lien vers : [[Synthese-Transformations]] | [[Transformations-Master.canvas]]*
