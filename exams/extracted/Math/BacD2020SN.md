---
tags: [bac, mauritania, 2020, math, series-D, examen]
---

# BAC 2020 - Série D (Sciences Naturelles)
## Éuvre de Mathématiques - Session Normale

*Source: BacD2020SN.txt*

---

## Exercice 1 (3 points) - Suites Numériques

**Énoncé:**

On considère les deux suites $(u_n)$ et $(v_n)$ définies pour tout entier naturel non nul $n$ par :

$$u_n = \frac{n}{2^n + n} \quad \text{et} \quad v_n = \left(\frac{1}{3}\right)^n$$

Pour tout entier naturel $n \geq 1$ on donne :

$$x_n = \frac{1}{u_n} \quad \text{et} \quad y_n = \ln(v_n)$$

### Questions à choix multiple

Pour chacune des six questions suivantes, une seule des réponses proposées est correcte.

| N° | Question | Réponse A | Réponse B | Réponse C | Points |
|----|----------|-----------|-----------|-----------|--------|
| 1 | La valeur de $x_5$ est | $6$ | $11$ | $16$ | 0,5pt |
| 2 | La limite de la suite $(u_n)$ est | $0$ | $\frac{1}{2}$ | $1$ | 0,5pt |
| 3 | La suite $(v_n)$ est | Croissante | Décroissante | Non monotone | 0,5pt |
| 4 | La suite $(x_n)$ est | Arithmétique | Géométrique | Convergente | 0,5pt |
| 5 | Le terme général de la suite $(y_n)$ est | $y_n = \frac{1}{3} \ln n$ | $y_n = -n \ln 3$ | $y_n = n \ln 3$ | 0,5pt |
| 6 | La somme $v_1 + v_2 + \cdots + v_n$ est égale à | $\frac{1}{2}\left(1 - \left(\frac{1}{3}\right)^{n+1}\right)$ | $\frac{1}{2}\left(1 - \left(\frac{1}{3}\right)^n\right)$ | $\frac{1}{2}\left(1 - \left(\frac{1}{3}\right)^{n-1}\right)$ | 0,5pt |

---

## Exercice 2 (6 points) - Nombres Complexes

### Partie 1

Pour tout complexe $z$ on pose : $P(z) = z^3 - (7 + 7i)z^2 + (-2 + 30i)z + 32 - 16i$

a) Calculer $P(2i)$

b) Déterminer les nombres complexes $a$ et $b$ tels que pour tout $z$, on a :
$$P(z) = (z - 2i)(z^2 + az + b)$$

c) Résoudre, dans l'ensemble des nombres complexes $\mathbb{C}$, l'équation $P(z) = 0$

### Partie 2

Dans le plan complexe muni d'un repère orthonormé direct $(O; \vec{u}, \vec{v})$. On considère les points $A$, $B$ et $C$ d'affixes respectives : $z_A = 3 + i$, $z_B = 2i$ et $z_C = 4 + 4i$.

a) Placer les points $A$, $B$ et $C$ dans le repère $(O; \vec{u}, \vec{v})$

b) Déterminer la nature du triangle $ABC$

c) Déterminer l'affixe $z_D$ du point $D$ tel que $ABDC$ soit un parallélogramme. Placer $D$.

### Partie 3

Pour tout nombre complexe $z \neq 3 + i$, on pose :
$$f(z) = \frac{z - 2i}{z - 4 - 4i}$$

a) Vérifier que $f(z_D) = -i$ et interpréter graphiquement.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ du plan d'affixe $z$ tels que $f(z) = 1$

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ du plan d'affixe $z$ tels que $|f(z) - 1| = 2$

### Partie 4

On pose $z_0 = f(6)$ et pour tout entier naturel $n$ on note $z_n = z_0^n$

a) Écrire $z_0$ sous forme algébrique, puis vérifier que $z_0 = 2e^{i\frac{\pi}{4}}$

b) Déterminer la plus petite valeur de l'entier naturel $n$ telle que $z_n \geq 2020$

c) Vérifier que le point d'affixe $z_{2020}$ appartient à l'axe des abscisses.

---

## Exercice 3 (4 points) - Analyse (Fonction exponentielle)

Soit $f$ la fonction définie sur $\mathbb{R}$ par : $f(x) = x - 2 + e^{-x}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O; \vec{i}, \vec{j})$.

### Partie 1

a) Justifier que $\lim_{x \to +\infty} f(x) = +\infty$ et $\lim_{x \to +\infty} (f(x) - (x - 2)) = 0$

b) En déduire que la droite $(\Delta)$ d'équation $y = x - 2$ est asymptote à la courbe $(C)$ puis étudier leur position relative.

### Partie 2

a) Montrer que $f(x) = \frac{xe^x - 2e^x + 1}{e^x}$ et que $\frac{f(x)}{x} = 1 - \frac{2}{x} + \frac{1}{xe^x}$

b) En déduire que $\lim_{x \to -\infty} f(x) = +\infty$ et que $\lim_{x \to -\infty} \frac{f(x)}{x} = -\infty$. Interpréter graphiquement.

### Partie 3

Justifier que $f'(x) = 1 - e^{-x}$ et dresser le tableau de variation de $f$.

### Partie 4

a) Montrer que l'équation $f(x) = 0$ admet deux solutions $\alpha$ et $\beta$ avec $\beta < \alpha$ puis vérifier que $1,8 < \alpha < 1,9$

b) Justifier que $f'(\alpha) = \alpha - 1$

### Partie 5

Construire la courbe $(C)$ et son asymptote $(\Delta)$ dans le repère $(O; \vec{i}, \vec{j})$.

---

## Exercice 4 (7 points) - Analyse (Fonction logarithme)

Soit $f$ la fonction définie sur $[0, +\infty[$ par :

$$
\begin{cases}
f(x) = x - x \ln x & \forall x > 0 \\
f(0) = 0
\end{cases}
$$

et soit $(\Gamma)$ sa courbe représentative dans un repère orthonormé $(O; \vec{i}, \vec{j})$.

### Partie 1

a) Calculer $\lim_{x \to 0^+} f(x)$ et en déduire que $f$ est continue en $0^+$

b) Calculer $\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0}$ et interpréter graphiquement.

c) Montrer que $\lim_{x \to +\infty} f(x) = -\infty$ et que $\lim_{x \to +\infty} \frac{f(x)}{x} = -\infty$ puis interpréter graphiquement.

### Partie 2

Calculer $f'(x)$ et dresser le tableau de variation de $f$.

### Partie 3

a) Déterminer les points d'intersection de la courbe $(\Gamma)$ avec l'axe des abscisses.

b) Donner une équation de la tangente $(T)$ à $(\Gamma)$ au point d'abscisse $e$.

### Partie 4

Soit $g$ la restriction de $f$ sur l'intervalle $I = [1, +\infty[$.

a) Montrer que $g$ est une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que $(g^{-1})'(0) = -1$ où $g^{-1}$ est la réciproque de $g$.

c) Construire $(T)$, $(\Gamma)$ et $(\Gamma')$ dans le repère $(O; \vec{i}, \vec{j})$, $(\Gamma')$ étant la courbe représentative de $g^{-1}$.

d) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $2x - x \ln x = m$

### Partie 5

a) Utiliser une intégration par parties pour calculer l'intégrale $A = \int_1^e x \ln x \, dx$

b) En déduire l'aire du domaine plan délimité par la courbe $(\Gamma)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = e$.

---

## Concepts Clés Testés

| Concept | Exercice | Points |
|---------|----------|--------|
| Suites numériques | Ex1 | 3 pts |
| Nombres complexes | Ex2 | 6 pts |
| Fonction exponentielle et asymptotes | Ex3 | 4 pts |
| Fonction logarithme et bijection | Ex4 | 7 pts |

---

*Année: 2020*
*Série: D (Sciences Naturelles)*
*Session: Normale*
*Coefficient: 6*
*Durée: 4h*
