---
date: 2026-03-14
subjects: [mathematiques, physique-chimie, svt]
type: practice-session
session: BAC 2025 D/SN + BAC 2010 Normal
total_points: 57
score: 
duration_planned: 4h
duration_actual: 
status: in-progress
---

# Session de Révision — 14 Mars 2026

## Tableau de bord

| Matière         | Points | Score | Temps  | Statut |
| --------------- | ------ | ----- | ------ | ------ |
| Mathématiques   | 20 pts | /20   | 1h45   | [ ]    |
| Physique-Chimie | 19 pts | /19   | 1h30   | [ ]    |
| SVT             | 18 pts | /18   | 45 min | [ ]    |

**Score total :** /57

---

## Formules clés

> [!tip] Mathématiques
> $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
> $$P(A \cap B) = P(A) \cdot P(B|A)$$
> Racines de $a+bi$ : poser $z=x+iy$, résoudre $x^2-y^2=a$ et $2xy=b$
> $$\int_a^b u\,v'\,dx = \bigl[uv\bigr]_a^b - \int_a^b u'\,v\,dx$$

> [!tip] Physique-Chimie
> $$pH = pK_a + \log\frac{[A^-]}{[AH]} \implies \frac{[AH]}{[A^-]} = 10^{pK_a - pH}$$
> $$F = B \cdot I \cdot \ell \qquad e = -\frac{d\Phi}{dt} \qquad L = \mu_0 \frac{N^2}{l} S$$
> $$x_M(t) = a\cos\!\left(2\pi N t - \frac{2\pi d}{\lambda}\right)$$

---

## Erreurs fréquentes

> [!warning] À ne pas oublier
> 1. **Probabilités** — ne pas confondre $P(B|S)$ et $P(S|B)$
> 2. **Complexes** — vérifier la forme exponentielle avant de conclure sur la nature d'un triangle
> 3. **Analyse** — justifier la bijectivité : monotonie stricte + continuité
> 4. **Estérification** — utiliser les masses molaires pour les quantités initiales
> 5. **Ondes** — déphasage $\varphi = -\dfrac{2\pi d}{\lambda}$ (signe négatif = retard)

---

## Mathématiques — BAC 2025 Série D/SN

> [!question]+ Exercice 1 — Probabilités *(3 pts)*
>
> 120 fleurs : $25\%$ parfumées, $40\%$ des parfumées rouges, $55\%$ blanches.
> Événements : $S$ = parfumée, $R$ = rouge, $B$ = blanche.
>
> 1. Calculer $P(S)$ — *0,5 pt*
> 2. Calculer $P(R)$ — *0,5 pt*
> 3. Calculer $P(B)$ — *0,5 pt*
> 4. Calculer $P(B \cap S)$ — *0,5 pt*
> 5. Calculer $P(B \cup S)$ — *0,5 pt*
> 6. Calculer $P(S \cup R)$ — *0,5 pt*

> [!question]+ Exercice 2 — Nombres Complexes *(5 pts)*
>
> Soit $P(z) = z^3 - (2+4i)z^2 - (2-8i)z + 4 - 12i$
>
> **Partie 1 — Polynôme** *(2,25 pts)*
>
> 1. Calculer les racines carrées de $-8+6i$ — *0,5 pt*
> 2. Résoudre dans $\mathbb{C}$ : $z^2 - (3+i)z + 4 = 0$ — *1 pt*
> 3. Déterminer $z_0$ tel que $P(z) = (z-z_0)(z^2-(3+i)z+4)$ — *0,5 pt*
>
> **Partie 2 — Géométrie** *(0,75 pt)*
>
> 4. Placer $A(1-i)$, $B(2+2i)$, $C(-1+3i)$ dans le plan complexe orthonormé
>
> **Partie 3 — Transformation** *(1,5 pts)*
>
> Pour $z \neq 1-i$ : $\quad f(z) = \dfrac{z+1-3i}{z-1+i}$
>
> 5. Vérifier $f(z_C) = -i$ et déduire la nature du triangle $ABC$ — *0,75 pt*
> 6. Déterminer l'ensemble des points $M$ tels que $f(z)$ soit imaginaire pur — *0,75 pt*
>
> **Partie 4 — Suites** *(0,75 pt)*
>
> Pour $n \in \mathbb{N}$ : $z_n = (z_A)^n$, $M_n$ d'affixe $z_n$
>
> 7. Trouver les entiers $n$ pour lesquels $M_n \in$ axe réel — *0,5 pt*
> 8. Montrer que $M_{2025} \in (OA)$ — *0,25 pt*

> [!question]+ Exercice 3 — Analyse *(6 pts)*
>
> $$f(x) = (e^x - x - 2)e^{-x}$$
>
> Courbe $\Gamma$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.
>
> **Limites et asymptotes** *(1,75 pts)*
>
> 1. Montrer que $f(x) = 1 - x + \dfrac{2}{e^x}$ — *0,5 pt*
> 2. Justifier $\lim_{x \to -\infty} f(x) = +\infty$ et $\lim_{x \to -\infty} \frac{f(x)}{x} = -\infty$, interpréter graphiquement — *0,75 pt*
> 3. Calculer $\lim_{x \to +\infty} f(x)$, déduire l'asymptote horizontale $D$ — *0,5 pt*
>
> **Variations** *(1 pt)*
>
> 4. Montrer que $f'(x) = (x+1)e^{-x}$, dresser le tableau de variations
>
> **Bijection** *(1 pt)*
>
> Soit $h = f\big|_{[-1,+\infty[}$
>
> 5. Montrer que $h : I \to J$ est une bijection, déterminer $J$ — *0,5 pt*
> 6. Dresser le tableau de variations de $h^{-1}$ — *0,5 pt*
>
> **Équation et construction** *(1,25 pts)*
>
> 7. Montrer que $f(x)=0$ admet deux solutions $\alpha > \beta$, justifier $1{,}1 < \alpha < 1{,}2$ — *0,5 pt*
> 8. Construire $D$, $\Gamma$ et $\Gamma'$ (courbe de $h^{-1}$) — *0,75 pt*
>
> **Intégration** *(1 pt)*
>
> 9. Calculer $\displaystyle\int_0^1 xe^x\,dx$ par intégration par parties — *0,5 pt*
> 10. Calculer l'aire $\mathcal{A}$ délimitée par $\Gamma$, $D$, $x=0$ et $x=1$ — *0,5 pt*

> [!question]+ Exercice 4 — Fonction Logarithme *(6 pts)*
>
> $$f(x) = \frac{x}{2} - \frac{\ln x}{2x}, \qquad x \in \left]0, +\infty\right[$$
>
> **Fonction auxiliaire** *(2,25 pts)*
>
> Soit $g(x) = x^2 - 1 + \ln x$ sur $\left]0,+\infty\right[$
>
> 1. Calculer $g'(x)$, étudier les variations de $g$ — *1 pt*
> 2. Calculer $g(1)$, déduire le signe de $g$ — *1,25 pt*
>
> **Limites et asymptotes** *(1,25 pts)*
>
> 3. Calculer $\lim_{x \to 0^+} f(x)$ et $\lim_{x \to +\infty} f(x)$ — *0,5 pt*
> 4. Montrer que $(C)$ admet deux asymptotes dont $\Delta : y = \dfrac{x}{2}$, position relative — *0,75 pt*
>
> **Dérivée et variations** *(1 pt)*
>
> 5. Montrer que $f'(x) = \dfrac{g(x)}{2x^2}$, déduire le signe de $f'$, tableau de variations — *1 pt*
>
> **Tangente et construction** *(1,5 pts)*
>
> 6. Montrer que $(C)$ admet une tangente $T$ parallèle à $\Delta$, équation de $T$ — *0,5 pt*
> 7. Construire $(C)$, $\Delta$ et $T$ — *0,75 pt*
> 8. Discussion : nombre de solutions de $\ln x + 2mx = 0$ selon $m \in \mathbb{R}$ — *0,25 pt*
>
> **Suite** *(0,5 pt)*
>
> 9. Suite $u_n = f\!\left(\dfrac{1}{n}\right)$ : montrer croissante, calculer la limite — *0,5 pt*

---

## Physique-Chimie — BAC 2010 Session Normale

> [!question]+ Exercice 1 — Acide Benzoïque *(3 pts)*
>
> Données : $C_6H_5COOH$, $pK_a = 4{,}2$ à $25°C$
>
> 1. Écrire l'équation bilan de la réaction avec l'eau — *0,5 pt*
> 2. Calculer $K_a$, déterminer les domaines acide/basique majoritaires, représenter sur une échelle de $pH$ — *1 pt*
> 3. Soda $pH=3{,}7$ : calculer $\dfrac{[C_6H_5COOH]}{[C_6H_5COO^-]}$ — *0,5 pt*
> 4. Préparer $S$ ($C=0{,}1$ mol/L) à partir de $S_0$ ($C_0=0{,}25$ mol/L) — procédure et verrerie — *1 pt*

> [!question]+ Exercice 2 — Estérification *(3,5 pts)*
>
> Données : acide éthanoïque $24\ \text{g}$, butan-1-ol $29{,}6\ \text{g}$, $H_2SO_4$, $100°C$
> À $t=1\ \text{h}$ : $n_{\text{acide}} = 0{,}132\ \text{mol}$ — $M_C=12$, $M_H=1$, $M_O=16\ \text{g/mol}$
>
> 1. Écrire l'équation de la réaction — *0,5 pt*
> 2. Donner le nom de l'ester $E$ — *0,5 pt*
> 3. Calculer les quantités initiales de matière — *0,5 pt*
> 4. Quantités à $t=1\ \text{h}$ et rendement — *1 pt*
> 5. Rôle de $H_2SO_4$ — pourquoi doser à $0°C$ ? — *0,5 pt*
> 6. Proposer une méthode plus rapide pour préparer $E$ — *0,5 pt*

> [!question]+ Exercice 3 — Rails de Laplace *(4 pts)*
>
> Données : $E=5\ \text{V}$, $r=5\ \Omega$, $\ell=0{,}2\ \text{m}$, $B=0{,}2\ \text{T}$, $l=6\ \text{cm}$
>
> 1. Placer l'aimant en U pour que $\vec{B}$ soit perpendiculaire vers le haut — *0,5 pt*
> 2. Sens et intensité du courant dans $MN$ — *0,75 pt*
> 3. Direction, sens et valeur de la force de Laplace — *0,75 pt*
> 4. Barre déplacée de $8\ \text{cm}$ à vitesse constante — flux balayé — *0,5 pt*
> 5. f.e.m induite en $1\ \text{ms}$ — *0,5 pt*

> [!question]+ Exercice 4 — Bobine et Condensateur *(4 pts)*
>
> Données : $2000$ spires, $\varnothing=6\ \text{cm}$, $l=40\ \text{cm}$, $R=60\ \Omega$, $f=50\ \text{Hz}$, $U=120\ \text{V}$
> Résonance : $I=1{,}5\ \text{A}$ pour $C=318\ \mu\text{F}$
>
> 1. Calculer l'inductance théorique $L$ — *0,75 pt*
> 2. Déterminer $L$ expérimentale, expliquer la différence — *0,5 pt*
> 3. Calculer la résistance $R'$ de la bobine — *0,5 pt*
>
> Circuit : source + $r=25\ \Omega$ + bobine. Mesures : $U=110\ \text{V}$, $U_1=45{,}5\ \text{V}$, $U_2=80\ \text{V}$
>
> 4. Schéma du montage — *0,5 pt*
> 5. Diagramme de Fresnel — *0,5 pt*
> 6. Impédance de la bobine — *0,5 pt*
> 7. Déphasage de $u_2$ par rapport à $i$ — *0,5 pt*
> 8. Valeurs de $R$ et $L$ — *0,5 pt*
> 9. Puissance moyenne — *1 pt*

> [!question]+ Exercice 5 — Ondes *(3,5 pts)*
>
> Données : $N=50\ \text{Hz}$, $a=0{,}5\ \text{cm}$, $C=5\ \text{m/s}$
>
> 1. Équation horaire (à $t=0$ : position maximale positive) — *1 pt*
> 2. Fréquence des éclairs pour lame immobile, $10 < N_e < 50\ \text{Hz}$ — *1 pt*
> 3. Calculer $\lambda$ — *0,5 pt*
> 4. Équation du point $M$ à $22{,}5\ \text{cm}$ de $O$ — *1 pt*
> 5. État vibratoire de $M$ par rapport à $O$ — *0,5 pt*

---

## SVT — BAC C/SN

Ouvrir `mauritanian-bac/svt/bac_c_sn_2010_2018.pdf` — année **2016 ou 2017**.

> [!note] Thèmes prioritaires
> 1. **Génétique** — hérédité, crossing-over, dihybridisme
> 2. **Système nerveux** — réflexes, synapse, potentiel d'action
> 3. **Reproduction** — méiose, fécondation, développement
> 4. **Géologie** — tectonique des plaques, roches

---

## Corrigés

| Exercice | Source |
|---|---|
| Maths 2025 | `04-Exams/BAC-Recent/` |
| PC 2010 | `04-Exams/BAC-2002-2012/BAC-2010-Normal.md` |
| Maths 2005–2014 | `mauritanian-bac/mathematiques/annale_serie_D_2005_2014_corr.pdf` |

---

## Auto-évaluation

| Exercice | Max | Obtenu | Erreurs |
|---|---|---|---|
| Maths — Probabilités | 3 | | |
| Maths — Complexes | 5 | | |
| Maths — Analyse | 6 | | |
| Maths — Logarithme | 6 | | |
| PC — Acide Benzoïque | 3 | | |
| PC — Estérification | 3,5 | | |
| PC — Rails de Laplace | 4 | | |
| PC — Bobine & Condensateur | 4 | | |
| PC — Ondes | 3,5 | | |
| SVT | 18 | | |

---

## Bilan

> [!success] Ce qui était maîtrisé
> 

> [!failure] À retravailler avant le BAC
> 

> [!abstract] Prochain objectif
> 
