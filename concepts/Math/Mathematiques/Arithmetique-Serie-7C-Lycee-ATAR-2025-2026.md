---
title: Arithmétique - Série 7C (2025-2026)
date: 2025-2026
tags:
  - mathématiques
  - arithmétique
  - 7c
  - série
  - lycée-d-atar
aliases:
  - Arithmetic 7C
---

# Arithmétique - Série 7C

**Établissement**: Lycée D'ATAR  
**Année**: 2025-2026  
**Classe**: 7ème C  
**Professeur**: Med Salem

> [!info] Objectif
> Cette série couvre les congruences, les équations diophantiennes, le PGCD, et les propriétés arithmétiques des entiers.

---

## Exercice 1: Divisibilité

1) **Déterminer** les chiffres $x$ et $y$ pour que le nombre $n = 43x57y$ soit divisible par $15$ et par $2$.

2) En base 9, **trouver** tous les couples $(x,y)$ pour lesquels le nombre $7x6y4_9$ est divisible par $7$ et par $8$. (On pourra utiliser le système décimal comme système intermédiaire)

> [!tip] Méthode
> - Divisible par 15 = divisible par 3 et 5
> - Divisible par 2 = le dernier chiffre est pair

---

## Exercice 2: Équations de congruence

**Résoudre** dans $\mathbb{Z}$ les équations suivantes :

a) $3x \equiv 5 \pmod{7}$  
b) $6x \equiv 5 \pmod{9}$  
c) $35x \equiv 7 \pmod{4}$  
d) $22x \equiv 33 \pmod{5}$  
e) $x^2 + x \equiv 6 \pmod{13}$  
f) $x^2 - 3x + 4 \equiv 0 \pmod{?}$

---

## Exercice 3: Propriétés de $5^n$

1) **Trouver**, suivant les valeurs de l'entier naturel $n$, le reste de la division euclidienne de $5^n$ par 7.

2) **Trouver** le reste de la division euclidienne de $2021^{2920}$ par 7.

3) Soit $X = 2011^{20} + 1 \equiv 20^{42m+41}$

   a) **Montrer** que tout entier naturel $m$, $X$ est divisible par 25

   b) **Montrer** que $X$ est divisible par 7

   c) $X$ est-il divisible par 175 ?

4) **Montrer** que pour tout $n \in \mathbb{Z}$ : $(3^n + 2)^n \equiv ?$

---

## Exercice 4: PGCD

1) On considère l'équation $(E) : 8x + 5y = 14$ où $x$ et $y$ sont des entiers relatifs.

   a) **Donner** une solution particulière de $(E)$

   b) **Résoudre** l'équation $(E)$

2) Soit $N$ un entier naturel tel qu'il existe un couple $(a, b)$ de nombres entiers naturels vérifiant :
   $$\begin{cases} N = 8a + 1 \\ N = 5b + 2 \end{cases}$$

   a) **Montrer** que le couple $(a, -b)$ est une solution de $(E)$

   b) **Quelle** est le reste de la division de $N$ par 40 ?

3) a) **Résoudre** l'équation $(E) : 8x + 5y = 100$ où $x$ et $y$ sont des entiers relatifs

   b) **Application**: Au VIIIème siècle, un groupe composé d'hommes et de femmes a dépensé 100 pièces de monnaie dans une auberge. Les hommes ont dépensé 8 pièces et les femmes ont dépensé 5 pièces chacune. Combien pourrait-il y avoir d'hommes et de femmes ?

---

## Exercice 5: Suite récurrente

On considère la suite $(x_n)$ d'entiers naturels définies par $x_0 = 14$ et $x_{n+1} = 5x_n - 6$ pour tout $n \in \mathbb{N}$.

1. **Calculer** $x_1$, $x_2$, $x_3$

2. a) **Montrer** que $x_{n+2} \equiv x_n \pmod{4}$

   b) **En déduire** que pour tout $n \in \mathbb{N}$ : $x_n \equiv 2 \pmod{4}$ si $n$ est pair, et $x_n \equiv 0 \pmod{4}$ si $n$ est impair

3. a) **Par** récurrence, montrer que $V_n$ et $x_{n+2}$ sont premiers entre eux

   b) **Déduire** les deux derniers chiffres de l'écriture décimal de $x_n$ suivant les valeurs de $n$

---

## Exercice 6: Fonction arithmétique

Soit $x$ et $y$ des entiers relatifs. On pose $f(x,y) = 2x - 3y$.

1. a) **Calculer** $f(5, 3)$

   b) **En déduire** les solutions dans $\mathbb{Z}$ de l'équation $2x - 3y = 1$

2. Pour tout entier naturel $n$ on pose $X_n = f(5^n, 3^n)$.

   a) **Trouver**, suivant les valeurs de $n$, le reste de la division euclidienne de $X_n$ par 7

   b) **Montrer** que $X_{5915} - 5$ est divisible par 7

---

## Exercice 7: Équation diophantienne

On considère l'équation $(E) : 5x - 3y = 17$, où $x$ et $y$ sont des entiers relatifs.

1. a) **Justifier** que l'équation $(E)$ admet des solutions entières et vérifier que le couple $(4, 1)$ est une solution particulière de $(E)$

   b) **Déterminer** l'ensemble des solutions de $(E)$

2. Soit $(x, y)$ une solution de $(E)$.

   a) **Montrer** que si $x$ est un diviseur de $y$, alors $x$ est un diviseur de 17

   b) Soit $m$ un entier relatif. **Trouver** les valeurs de $m$ telles que le quotient $\frac{y}{x+m}$ soit un entier relatif

---

## Exercice 8: Équation de Bezout

On considère l'équation $(E) : 25x - 49y = 5$, où $x$ et $y$ sont des entiers relatifs.

1. a) **Déterminer** le pgcd de 25 et 49 à l'aide de l'algorithme d'Euclide et en déduire que l'équation $(E)$ admet des solutions entières

   b) **Vérifier** que le couple $(10, 5)$ est solution particulière de l'équation $(E)$. **Résoudre** $(E)$

   c) **Montrer** qu'il existe un unique entier $p$ compris entre 1960 et 2018 tel que : $25p \equiv 5 \pmod{49}$

2. a) **Justifier** que si $(x, y)$ est une solution de $(E)$ alors $5x \equiv 1 \pmod{7}$ et $y \equiv 0 \pmod{5}$

   b) **Montrer** que $5x \equiv 1 \pmod{7}$ si et seulement si $x \equiv 3 \pmod{7}$

3. a) Soit $x$ un entier relatif. **Qualifier** sont les restes de $x^2$ dans la division euclidienne par 7 ?

---

## Ressources

- [[Cours Arithmétique]]
- [[Équations Diophantiennes]]
- [[PGCD et PPCM]]
- [[Congruences]]

---

*Source: Série arithmétique 7C lycée D'ATAR 2025-2026*