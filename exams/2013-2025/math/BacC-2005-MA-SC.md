---
title: Baccalauréat Série C - Mathématiques
year: 2005
session: Session Complémentaire
subject: Mathématiques
series: C
duration: 4 heures
coefficients: 9 & 6
type: Examen
---

# Exercice 1 (4 points)

Dans l'ensemble des nombres complexes, on considère l'équation (E) d'inconnue $z$ :
$$z^2 - 2z + 2 = 0$$
où $c$ est un paramètre réel appartenant à $[0, 2\pi]$. On note $z_1$ et $z_2$ ces deux solutions. \hfill (1 pt)

1. a) Résoudre l'équation (E). \hfill (0,5 pt)
   b) Discuter suivant les valeurs du paramètre $c$, le module et un argument de $z_1$ et de $z_2$. \hfill (0,5 pt)

2. On considère le plan complexe muni d'un repère orthonormé et soient $M_1$ et $M_2$ les points d'affixes respectives $z_1$ et $z_2$.
   a) Montrer que lorsque $c$ décrit $[0, 2\pi]$, les points $M_1$ et $M_2$ décrivent un cercle de centre $A(1,0)$ dont on déterminera le rayon, et que la droite $(M_1M_2)$ passe par un point fixe que l'on déterminera. \hfill (1 pt)
   b) Représenter $M_1$ et $M_2$ sur le plan complexe dans le cas où $c = \frac{\pi}{2}$. \hfill (0,5 pt)

3. Pour tout entier naturel $n$ tel que $n \geq 2$, on considère l'équation $(E_n)$ d'inconnue complexe $z$ :
$$z^n - 2z^{n-1} + 2 = 0$$
où $c$ est un paramètre réel appartenant à $[0, 2\pi]$.
   a) Déterminer les nombres $z_k$ solutions de l'équation $(E_n)$. \hfill (0,25 pt)
   b) Montrer que $z_k + 2\overline{z_k} = n$. \hfill (0,25 pt)
   c) Montrer que les points $M_k$ d'affixes $z_k$ appartiennent au cercle $\mathcal{C}$. \hfill (0,25 pt)
   d) On pose $S_n = M_1M_2 + M_2M_3 + \cdots + M_{n-1}M_n$. Calculer $S_n$ en fonction de $c$ et $n$, puis montrer que $\lim\limits_{n \to +\infty} \frac{S_n}{n} = 2m$ et interpréter cette limite. \hfill (0,25 pt)

# Exercice 2 (5 points)

Dans le plan orienté, on considère un triangle direct $ABC$ rectangle et isocèle en $A$. Les points $I$, $J$ et $K$ sont les milieux respectifs de $[BC]$, $[AC]$ et $[AB]$. Le point $D$ est l'image du point $K$ par la réflexion d'axe $(AC)$.

1. a) Faire une figure illustrant les données précédentes que l'on complétera au fur et à mesure. \hfill (0,75 pt)
   b) Soit $r$ la rotation de centre $A$ et d'angle $\alpha$ telle que $r(B) = J$. En déduire que $(BJ)$ et $(CD)$ sont perpendiculaires. \hfill (1 pt)
   c) Soit $s$ la similitude directe de centre $A$, d'angle $\alpha$ et de rapport $k = \sqrt{2}$, déterminer $s(B)$ et $s(C)$. En déduire que $(BC)$ et $(DJ)$ sont perpendiculaires. \hfill (1 pt)
   d) Déduire de ce qui précède que $J$ est l'orthocentre du triangle $BCD$. \hfill (0,5 pt)

2. Soit $F$ le point d'intersection des droites $(BJ)$ et $(CD)$. Montrer que les points $A$, $D$, $F$ et $J$ sont cocycliques et que les points $A$, $B$, $C$, $F$ le sont aussi. \hfill (0,25 pt)

3. On considère le cercle circonscrit au triangle $ABC$. Pour tout point $M$ du plan, on pose $N(M) = M'$. Déterminer le lieu géométrique du point $M'$ lorsque $M$ décrit le cercle $\mathcal{C}$. \hfill (0,5 pt)

4. Pour tout point $M$ du plan distinct de $A$, on désigne par $N$ le milieu du segment $[AM]$.
   a) Calculer $\overrightarrow{AN}$ et montrer que l'angle $(\overrightarrow{AM}, \overrightarrow{AN})$ est une mesure constante lorsque $M$ varie. \hfill (0,25 pt)
   b) Vérifier que $\cos \alpha = \frac{2}{5}$. \hfill (0,25 pt)
   c) En déduire que le point $N$ est l'image du point $M$ par une similitude directe que l'on caractérisera. \hfill (0,25 pt)
   d) Déterminer et construire, sur la figure précédente, le lieu $\mathcal{L}$ de $N$ lorsque $M$ décrit le cercle $\mathcal{C}$. \hfill (0,25 pt)

# Problème (11 points)

## Partie A

Pour tout entier naturel non nul $n$ et pour tout réel $x$, on pose :
$$S_n(x) = 1 - x + x^2 - x^3 + \cdots + (-1)^n x^n$$

1. a) Donner une primitive de la fonction $S_n$ sur $\mathbb{R}$. \hfill (1 pt)
   b) Démontrer que pour tout $x \neq -1$ et $n \geq 2$ :
$$S_n(x) = \frac{1 - (-x)^{n+1}}{1+x}$$ \hfill (0,5 pt)
   c) En déduire que :
$$\lim\limits_{x \to -1^+} S_n(x) = +\infty \quad \text{et} \quad \lim\limits_{x \to -1^-} S_n(x) = -\infty$$ \hfill (0,5 pt)
   d) En utilisant les résultats précédents, démontrer que :
$$\lim\limits_{x \to +\infty} S_n(x) = \begin{cases}
+\infty & \text{si } n \text{ est pair} \\
-\infty & \text{si } n \text{ est impair}
\end{cases}$$ \hfill (0,5 pt)

## Partie B

On considère la fonction numérique $f$ définie par :
$$f(x) = \begin{cases}
x^2 \sin\left(\frac{1}{x}\right) & \text{si } x \neq 0 \\
0 & \text{si } x = 0
\end{cases}$$

1. a) Montrer que $f$ est continue au point d'abscisse $x = 0$. \hfill (0,5 pt)
   b) Montrer que $f$ est dérivable en $x = 0$ puis calculer $f'(0)$. \hfill (0,5 pt)
2. Soit la fonction numérique $u$ définie par : $u(x) = x^2 + 1$.
   a) Étudier les variations de $u$ et montrer que : $\forall x \in \mathbb{R}, u(x) > 0$. \hfill (1 pt)
   b) Vérifier que: $\forall x \in \mathbb{R}, f(x) \leq u(x)$. \hfill (0,5 pt)
   c) Dresser le tableau de variation de $f$. \hfill (0,5 pt)

## Partie C

On considère la fonction numérique $g$ définie par :
$$g(x) = \frac{1}{1+x^2}$$

1. Montrer que $g$ est définie sur $\mathbb{R}$. \hfill (0,25 pt)
   b) Étudier la continuité et la dérivabilité de $g$ sur $\mathbb{R}$. \hfill (0,5 pt)
   c) Calculer $g'(x)$ puis vérifier que $g$ est décroissante sur $[0, +\infty[$. \hfill (0,5 pt)
   d) Du tableau de variation de $f$, déduire celui de $g$. \hfill (0,5 pt)
   e) Construire la courbe $(C_g)$ représentant $g$ dans un repère orthonormé. \hfill (0,25 pt)

2. On considère la transformation $T$ du plan dans lui-même qui associe à tout point $M(x,y)$ le point $M'(x',y')$ tel que :
$$\begin{cases}
x' = -x \\
y' = y + 2
\end{cases}$$

   a) Déterminer l'expression de $h(x)$ où $h$ est la fonction numérique dont la courbe représentative est $T(C_g)$, et vérifier que $h(x) = g(-x-1)$. \hfill (0,5 pt)
   b) Du tableau de variation de $g$ déduire celui de $h$. \hfill (0,5 pt)
   c) Vérifier que $T$ est la réflexion d'axe $x = -1$ et déduire la construction de $(C')$ et de $(C_g)$ dans le repère précédent. \hfill (0,5 pt)

3. Pour tout entier naturel $m > 2$, on pose $U_m = \int_0^m g(x) dx$ et $V_m = \int_m^{m+1} g(x) dx$.
   a) Montrer que pour tout $n \geq 2$: $g(n) < \frac{1}{n} < h(n)$, en déduire que $U_n < \ln(n+1) < V_n$. \hfill (0,5 pt)
   b) Montrer que pour tout $n > 2$: $U_n + V_n = \ln\left(\frac{(n+1)^2}{n^2+1}\right)$. \hfill (0,25 pt)
   c) Montrer que les suites $(U_n)$ et $(V_n)$ sont adjacentes. \hfill (0,25 pt)

---

*Fin de l'exercice*