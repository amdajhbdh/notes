---
title: Baccalauréat Série C - Mathématiques
year: 2006
session: Session Complémentaire
subject: Mathématiques
series: C
duration: 4 heures
coefficients: 9 & 6
type: Examen
---

# Exercice 1 (5 points)

Le plan complexe est muni d'un repère direct. Soit $a$ un réel strictement positif, $A$ le point de coordonnées $(a;0)$, et $(D)$ la droite d'équation $x = -a$.

Pour chaque valeur du paramètre $t \in \mathbb{R}_+^*$, on note $s_t$ l'application du plan complexe dans lui-même qui à tout point $M$ d'affixe $z$ associe le point $M_t$ d'affixe $z_t$ tel que :
$$z_t = f(t)(\cos t + i\sin t)z$$
où $f(t)$ est une fonction réelle strictement positive.

1. a) Quelle est la nature de l'application $s_t$ ? Donner ses éléments caractéristiques.
   b) Donner les équations analytiques qui définissent $s_t$ et $s_t^{-1}$ par rapport à un repère orthonormé direct $(\vec{i},\vec{j})$.

2. Dans cette question, on pose $f(t) = 1$ pour tout $t \in \mathbb{R}$.
   a) Montrer que si $M \notin (D)$ alors $\forall t \in \mathbb{R}$, le triangle $OMM_t$ est rectangle en $O$.
   b) Le point $M$ étant fixe, quel est le lieu décrit par $M_t$ lorsque $t$ décrit $\mathbb{R}$ ?
   c) Montrer que l'image de la droite $(D)$ par $s_t$ est une droite. On donnera une équation cartésienne dépendant seulement de $a$ et de $\tan(t)$.

3. Dans cette question, on suppose toujours que $f(t) = \cos t$ mais avec $A = (5;0)$.
   a) Donner une mesure de l'angle $\angle BAC$.
   b) Soit $H$ le point d'intersection des droites $(AM)$ et $(A_{-t}M_t)$. Montrer que les points $O$, $H_t$, $A$ et $A_{-t}$ sont cocycliques.
   c) Montrer que les points $O$, $H_t$, $M$ et $M_t$ sont cocycliques. Quelle est la projection orthogonale de $O$ sur $(AM)$ ?
   d) Soit $(D_t)$ l'image de la droite $(D)$ par $s_t$. Montrer que lorsque $t$ varie, $(D_t)$ passe par un point fixe.

# Exercice 2 (4 points)

On considère, dans l'ensemble des nombres complexes, l'équation suivante :
$$z^3 - 3z^2 + 4 = 0$$
où $m$ est un entier supérieur ou égal à $2$.

1. a) Déterminer les solutions $z_1$ et $z_2$ de l'équation $z^2 - 2z + 2 = 0$ telles que $\operatorname{Re}(z_1) < 0$ et écrire sous forme trigonométrique les solutions $z_1$ et $z_2$ de l'équation $z^3 - 3z^2 + 4 = 0$.
   b) Posons $u = z_1 + z_2$. Montrer que pour tout $p \in \mathbb{N}$, $(u)^p + (\overline{u})^p = 2^{p+1}\cos\left(\frac{p\pi}{3}\right)$ où $\overline{u}$ est le conjugué de $u$.
   c) On considère l'application $f$ définie sur l'ensemble des nombres complexes par :
$$f(z) = z^3 - 3z^2 + 4$$
   d) Résoudre, dans l'ensemble des nombres complexes, l'équation $f(z) = 0$.

# Problème

## Partie A

Soit $f$ la fonction numérique définie par :
$$f(x) = \begin{cases}
x & \text{si } |x| \leq 1 \\
\frac{1}{x} & \text{si } |x| > 1
\end{cases}$$

1. a) Déterminer l'ensemble $D$ de définition de $f$.
   b) Montrer que $f$ est impaire.
   c) Dresser le tableau de variations de $f$.
   d) Tracer la courbe représentative $(C)$ de $f$ dans un repère orthonormé.

2. Montrer que $f$ réalise une bijection de $D$ sur $\mathbb{R}$.

3. b) Soit $g$ la réciproque de $f$. Montrer que pour tout réel $x$, $g(x) = \operatorname{sign}(x) \cdot \max(|x|, 1)$.
   c) Tracer la courbe représentative de $g$ dans le repère orthonormé.

4. Déterminer l'ensemble du plan compris entre les deux courbes $(C)$ et $(C')$ et situé dans le premier quadrant.

## Partie B

Pour tout entier naturel $m$ et pour tout réel $x > 0$, on pose :
$$u_m(x) = \ln(x^m + 1)$$

1. Justifier l'existence de $V_n \in \mathbb{N}^*$ et $x > 0$ telles que $u_{V_n}(x) \geq n$.
2. b) Calculer $u'_m(x)$.
   c) Montrer que si $x > 1$ alors $u'_m(x) < \frac{m}{x}$.
3. c) Montrer que si $x \in (0,1)$ alors la suite $(u_m(x))$ est convergente et calculer sa limite.
4. d) Vérifier que si $x \in \mathbb{R}$ alors $u'_m(x) = \frac{mx^{m-1}}{x^m + 1}$.
   e) Déduire alors que si $x > 1$ alors $\lim\limits_{m \to +\infty} u_m(x) = +\infty$.

## Partie C

Soit $h$ la fonction numérique définie par :
$$h(x) = \ln(x) + \ln(f(x))$$
où $f$ est la fonction définie dans la partie A.

1. a) Justifier que pour tout $x \in \mathbb{R}\setminus\{-1,0,1\}$, $h(x)$ est définie.
   b) Montrer que $h$ est dérivable sur son ensemble de définition.
   c) En déduire que $h'(x) = \frac{1}{x} + f'(x)$.

2. b) Montrer que $h$ est convexesur $]1,+\infty[$.
   c) Tracer la courbe représentative de $h$ dans un nouveau repère orthonormé.

3. d) Montrer que si $k \in \mathbb{N}^*$ alors $\sum_{i=1}^k \ln(i) \leq \ln(k!)$.
   e) Montrer que si $n \in \mathbb{N}^*$ alors $\ln(n!) < \ln((n+2)!)$.
   f) Montrer que la suite $u_n = \ln(n!)$ est convergente.
   g) Montrer que la suite $u_n = \ln(n!)$ est convergente.

---

*Fin de l'exercice*