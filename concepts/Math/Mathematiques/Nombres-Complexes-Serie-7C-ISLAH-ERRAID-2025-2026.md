---
title: Nombres Complexes - Série 7C (2025-2026)
date: 2025-2026
tags:
  - mathématiques
  - nombres-complexes
  - 7c
  - série
  - islah-erraid
aliases:
  - Complex Numbers 7C
---

# Nombres Complexes - Série 7C

**Établissement**: E.P ISLAH ERRAID  
**Année**: 2025-2026  
**Classe**: 7ème C

> [!info] Objectif
> Cette série d'exercices couvre les nombres complexes dans le plan complexe, les formes exponentielles, et les transformations géométriques.

---

## Exercice 1: Points sur cercles

Soit $U$ l'ensemble des nombres complexes de module 1: $U = \{z \in \mathbb{C} : |z| = 1\}$ et soit $U^* = U - \{1\}$.

Soit $P$ le plan complexe muni d'un repère orthonormé direct d'origine $O$.

### Questions

1. **Montrer** que quel que soit $u \in U$, le point $M$ d'affixe $z = 1 - u$ appartient au cercle de centre $A$ d'affixe $1$ et de rayon $r = 1$.

2. **Montrer** que quel que soit $u \in U$, le point $N$ d'affixe $z' = 1 - \frac{1}{u}$ appartient à la médiatrice de $[OA]$.

3. Soit $B$ le point d'affixe $b$ ($b \neq 0$). **Montrer** que le point $Q$ d'affixe $z'' = b(1-u)$ appartient au cercle de centre $B$ passant par $O$.

> [!tip] Méthode
> Pour montrer qu'un point appartient à un cercle, démontrer que la distance au centre est égale au rayon.

---

## Exercice 2: Symétrie et cercle

Soit $(C)$ le cercle de centre $A(1,0)$, de rayon $1$. Pour tout point $M$ distinct de $O$ du cercle $(C)$, on considère le point $M'$, symétrique de $M$ par rapport à $(x'Ox)$.

### Questions

1. **Expliquer** pourquoi l'affixe $z$ du point $M$ peut se mettre sous la forme $z = 1 + e^{i\theta}$ avec $\theta \in ]-\pi, \pi]$.

2. **Déterminer** l'affixe $z'$ de $M'$.

3. **Calculer** le quotient $\frac{z' - 1}{z - 1}$ en fonction de $\theta$.

4. **Déduire** les points $M$ de $(C)$ pour lesquels :
   - a) $AM'$ et $OM$ sont colinéaires
   - b) $AM'$ et $OM$ sont orthogonaux

---

## Exercice 3: Racines de l'unité

Soit $z = e^{i\frac{2\pi}{7}}$. On pose $S = z + z^2 + z^4$.

### Questions

1. **Calculer** $S + \bar{S}$ et $S \cdot \bar{S}$

2. **En déduire** que :
   $$\sin\frac{2\pi}{7} + \sin\frac{4\pi}{7} + \sin\frac{8\pi}{7} = \frac{\sqrt{7}}{2}$$
   $$\cos\frac{2\pi}{7} + \cos\frac{4\pi}{7} + \cos\frac{8\pi}{7} = -\frac{1}{2}$$

---

## Exercice 4: Équation du second degré

1. **Résoudre** dans $\mathbb{C}$ l'équation : $4z^2 - 2\sqrt{2}e^{i\alpha}z + e^{2i\alpha} = 0$, $\alpha \in [0, \pi]$.

2. **Mettre** les solutions sous forme exponentielle.

3. On munit le plan complexe d'un repère orthonormé direct $(O; \vec{u}, \vec{v})$.

   On désigne par $M_1$ et $M_2$ les points d'affixes :
   $$z_1 = e^{i\frac{\pi}{3}} \quad \text{et} \quad z_2 = \frac{3+i}{3-i}$$

   a) **Montrer** que $M_1$ et $M_2$ appartiennent à un même cercle dont on précisera le centre et le rayon.

   b) **Montrer** que $\left|\frac{z_2 - 1}{z_1 - 1}\right| = \sqrt{3}$

   c) **En déduire** que $OMM_1M_2$ est un triangle équilatéral.

4. a) **Montrer** que $(\vec{u}, \overrightarrow{OM_1}) = \frac{\pi}{3} \pmod{2\pi}$

   b) **Déterminer** $\alpha$ pour que la droite $(M_1M_2)$ soit parallèle à la droite d'équation $y = -x$

5. **Résoudre** dans $\mathbb{C}$ l'équation : $4z^4 - z^2(1+i) + z(2+i) = 0$

---

## Exercice 5: Polynôme et transformation

On considère le polynôme :
$$P(z) = (i-1)z^3 + (11-5i)z^2 - (43+i)z + 9 + 37i$$

### Questions

1. **Calculer** $P(i)$ puis **résoudre** l'équation $P(z) = 0$

2. Dans le plan rapporté à un repère orthonormé $(O, \vec{u}, \vec{v})$, on désigne par $A, B, C, A', I$ les points d'affixes respectives $i$, $5-2i$, $3+4i$, $-i$ et $1$.

   a) **Placer** les points sur une figure

   b) Soit $r$ le quart de tour direct de centre $I$. **Reconnaître** les images de $A$ et $B$ par $r$ et en déduire que les segments $[AB]$ et $[CA']$ sont perpendiculaires et de même longueur.

3. Pour tout $z \neq i$, on pose :
   $$z' = \frac{-iz - 4 + 3i}{z - i}$$
   
   Soit $f$ l'application qui à tout point $M$ d'affixe $z$ associe le point $M'$ d'affixe $z'$.

   a) **Montrer** que $OM' = \frac{1}{|z - i|}$ et que $(\vec{u}, \overrightarrow{OM'}) = -\frac{\pi}{2} + (\widehat{MA}, \widehat{MC}) \pmod{2\pi}$

   b) **Déterminer** l'ensemble des points $M'$ lorsque $M$ décrit la médiatrice de $[AC]$

   c) **Déterminer** l'ensemble des points $M$ lorsque $M'$ décrit la droite $(O, \vec{u})$

4. a) **Calculer** le produit $(z' + i)(z - i)$ et en déduire que $A'M' \times AM = 3\sqrt{2}$ et que $(\widehat{IA'}) + (\widehat{IAM}) = \frac{\pi}{4} \pmod{2\pi}$

   b) **Déterminer** une mesure de $(\widehat{I, AC})$ et préciser l'image de la droite $(AC)$ privée de $A$ par $f$.

   c) **Déterminer** aussi l'image de la droite $(AI)$ privée de $A$ par $f$.

   d) **Reconnaître** l'image du cercle de centre $A$ et passant par $C$.

---

## Ressources

- [[Cours Nombres Complexes]]
- [[Exercices Corrigés Nombres Complexes]]
- [[Formulaire Trigonométrie]]

---

*Source: Série nombre complexe 7C E.P ISLAH ERRAID 2025-2026*