# Génétique : Dihybridisme & Linkage

Ces notes détaillent les principes du dihybridisme et du linkage génétique, incluant le linkage partiel et absolu, le rôle du brassage intra-chromosomique (crossing-over), et leur impact sur les ratios phénotypiques et les fréquences de recombinaison.

---

## PAGE 1 — Linkage Partiel

### b) Linkage Partiel (ou Incomplet)

Le **linkage partiel** se produit lorsque deux gènes sont situés sur le même chromosome, mais à une distance telle que des événements de **crossing-over** (ou enjambement) peuvent se produire entre eux pendant la méiose. Ces échanges physiques de segments d'ADN entre chromosomes homologues entraînent la formation de gamètes **recombinées** en plus des gamètes **parentales**.

[[Placeholder: Diagramme de deux chromosomes homologues, montrant deux gènes liés (A et B) et un point de crossing-over entre eux, résultant en des chromatides recombinées.]]

Contrairement aux gènes indépendants qui produisent $25\%$ de chaque phénotype dans la descendance d'un test-cross (F₁ x double récessif), les gènes en linkage partiel donnent des fréquences inégales :
*   Les types parentaux (combinaisons d'allèles présentes chez les parents) sont plus fréquents.
*   Les types recombinés (nouvelles combinaisons d'allèles) sont moins fréquents.

**Tableau comparatif des proportions attendues dans un test-cross F₁ x double récessif:**

| Type de Gènes         | Configuration F₁ | Phénotype $[AB]$ | Phénotype $[Ab]$ | Phénotype $[aB]$ | Phénotype $[ab]$ |
| :-------------------- | :--------------- | :------------- | :------------- | :------------- | :------------- |
| **Indépendants**      | $(A/a ; B/b)$      | $1/4$ ($25\%$)      | $1/4$ ($25\%$)      | $1/4$ ($25\%$)      | $1/4$ ($25\%$)      |
| **Liés en couplage (cis)** | $(AB/ab)$          | $\bf > 1/4$      | $\bf < 1/4$      | $\bf < 1/4$      | $\bf > 1/4$      |
| **Liés en répulsion (trans)** | $(Ab/aB)$          | $\bf < 1/4$      | $\bf > 1/4$      | $\bf > 1/4$      | $\bf < 1/4$      |

---

### Exercice d'Application (Exemple du Bac 2014 7D.Sc)

**Contexte du Problème:**
Un croisement parental $(P)$ est réalisé entre:
*   Une femelle homozygote pour les allèles dominants (représentée par son phénotype $[AB]$).
*   Un mâle homozygote double récessif (phénotype $[ab]$).

Ce premier croisement produit une génération $F_1$.
Un **test-cross** est ensuite effectué: une femelle de la $F_1$ est croisée avec un mâle double récessif $[ab]$.

**Résultats du test-cross ($F_1 \text{ ♀} \times \text{ ♂ } [ab]$):**

Les phénotypes observés dans la descendance de ce test-cross (souvent appelée $F_2$ dans ce contexte) et leurs fréquences sont les suivants:

| Phénotype de la Descendance | Fréquence Observée | Classification |
| :-------------------------- | :----------------- | :------------- |
| $[bnt]$                       | $68\%$                | Type Parental  |
| $[bny]$                       | $7\%$                 | Type Recombiné |
| $[bnt]$                       | $7\%$                 | (probablement Parental) |
| $[bw]$                        | $18\%$                | Type Recombiné |
| **Total**                   | $\bf 100\%$           |                |

*Note: Les symboles $[bnt]$, $[bny]$, $[bw]$ sont des désignations génériques pour les phénotypes. Supposons pour l'analyse que $[bnt]$ est le phénotype parental dominant et $[bw]$ ou $[bny]$ sont les recombinés. La répétition de "$7\% [bnt]$" suggère une erreur de transcription dans la source originale, ou bien une ventilation des phénotypes parentaux si "bnt" représente plus d'un type. Pour la clarté, nous considérerons les deux phénotypes majoritaires comme parentaux et les deux minoritaires comme recombinés.*

**Calcul de la Fréquence de Recombinaison ($P$ ou $C.O.$):**
La fréquence de recombinaison est la somme des fréquences des types recombinés.
Fréquence des recombinés = $7\%$ $([bny])$ + $18\%$ $([bw])$ = $\bf 25\%$.
Ainsi, $\bf P = 25\%$ (ou $0.25$).
Cette valeur (entre $0\%$ et $50\%$) confirme qu'il s'agit bien d'un **linkage partiel**.

---

### Questions et Analyse

**1. Génotype des Parents $(P)$ et de la $F_1$:**

*   **Génotype des Parents $(P)$:**
    *   Femelle parentale $([AB])$: Puisqu'elle est de souche pure et de phénotype dominant, son génotype est $\bf AB/AB$.
    *   Mâle parental $([ab])$: Étant homozygote double récessif, son génotype est $\bf ab/ab$.

*   **Génotype de la $F_1$:**
    Le croisement $AB/AB \times ab/ab$ donne une première génération $F_1$ dont tous les individus sont hétérozygotes. Leurs chromosomes portent un allèle dominant et un allèle récessif pour chaque gène.
    Puisque les allèles $A$ et $B$ proviennent du même parent (la femelle $AB/AB$) et sont donc sur le même chromosome, tandis que $a$ et $b$ proviennent de l'autre parent (le mâle $ab/ab$) et sont sur le chromosome homologue, la $F_1$ est en configuration **cis (ou couplage)**.
    Son génotype est donc $\bf AB/ab$.
    Le fait que le test-cross de cette $F_1$ produise quatre phénotypes, incluant des recombinés, confirme le **linkage partiel**.

    *   La femelle $F_1$ utilisée pour le test-cross a un phénotype dominant (par exemple $[bnt]$ ou $[AB]$) et un génotype $\bf AB/ab$.
    *   Le mâle utilisé pour le test-cross est de phénotype double récessif $[ab]$ et de génotype $\bf ab/ab$.

**2. Gamètes formées par les individus de la $F_1$:**

L'individu $F_1$ hétérozygote (génotype $AB/ab$ en cis) forme quatre types de gamètes par méiose. En raison du linkage partiel et du crossing-over, ces gamètes ne sont pas produites en proportions égales:

*   **Gamètes parentales:** Ce sont les combinaisons d'allèles présentes sur les chromosomes d'origine des parents (transmises "en bloc").
    *   $\bf AB$
    *   $\bf ab$
*   **Gamètes recombinées:** Ce sont les nouvelles combinaisons d'allèles résultant du crossing-over.
    *   $\bf Ab$
    *   $\bf aB$

D'après la fréquence de recombinaison ($P = 25\%$), les fréquences de ces gamètes seraient:
*   Fréquence des gamètes parentales $(AB \text{ et } ab) = (1 - P) / 2 = (1 - 0.25) / 2 = 0.75 / 2 = \bf 37.5\% \text{ chacune}$.
*   Fréquence des gamètes recombinées $(Ab \text{ et } aB) = P / 2 = 0.25 / 2 = \bf 12.5\% \text{ chacune}$.

---

## PAGE 2 — Suite : Échiquier de Croisement & Fréquences Gamétiques

*(Cette page contient des notations mathématiques et des schémas d'échiquier de croisement partiellement remplis. Nous allons interpréter ces fragments et les compléter avec des explications standards.)*

**Contexte:** L'objectif est de comprendre la répartition des gamètes et des génotypes (et par extension, des phénotypes) lorsque des gènes sont liés et qu'il y a crossing-over.

### Calculs de Fréquences Gamétiques

Comme établi précédemment, si la fréquence de recombinaison $(P)$ est de $25\%$ ($0.25$) pour un individu $F_1$ de génotype $\bf AB/ab$ (en configuration *cis*):

*   **Fréquence des gamètes parentales ($AB$ et $ab$):**
    Ces gamètes ne résultent pas d'un crossing-over entre les deux gènes. Leur fréquence totale est $(1 - P)$. Puisqu'il y a deux types de gamètes parentales ($AB$ et $ab$), la fréquence de chacun est:
    $$ \text{Fréquence parentale} = \frac{1 - P}{2} = \frac{1 - 0.25}{2} = \frac{0.75}{2} = \bf 0.375 \text{ (37.5\%)} $$

*   **Fréquence des gamètes recombinées ($Ab$ et $aB$):**
    Ces gamètes résultent d'un crossing-over entre les deux gènes. Leur fréquence totale est $P$. Puisqu'il y a deux types de gamètes recombinées ($Ab$ et $aB$), la fréquence de chacun est:
    $$ \text{Fréquence recombinée} = \frac{P}{2} = \frac{0.25}{2} = \bf 0.125 \text{ (12.5\%)} $$

**Vérification:** La somme des fréquences de toutes les gamètes doit être égale à $100\%$:
$37.5\% (AB) + 37.5\% (ab) + 12.5\% (Ab) + 12.5\% (aB) = 100\%$.

### 3. Échiquier de Croisement de la $F_1$ (Test-Cross Complété)

Un échiquier de croisement (ou tableau de Punnett) est utilisé pour prédire les génotypes et phénotypes de la descendance. Pour le test-cross ($F_1 \text{ ♀} \times \text{ ♂ } [ab]$), nous avons:

*   **Gamètes de la femelle $F_1$ (génotype $AB/ab$ en cis):**
    *   $AB$ ($37.5\%$)
    *   $ab$ ($37.5\%$)
    *   $Ab$ ($12.5\%$)
    *   $aB$ ($12.5\%$)

*   **Gamètes du mâle double récessif (génotype $ab/ab$):**
    *   $ab$ ($100\%$)

En croisant ces gamètes, on obtient directement les fréquences des génotypes et phénotypes de la descendance:

[[Placeholder: Tableau de Punnett pour un test-cross, montrant les gamètes de la F1 femelle en ligne et les gamètes du mâle double récessif en colonne, rempli avec les génotypes et leurs fréquences.]]

| Gamètes $\text{♀ } F_1$ / Gamètes $\text{♂ } (ab)$ | $\bf ab (100\%)$ |
| :----------------------------------------- | :--------------- |
| $\bf AB (37.5\%)$                            | $AB/ab (37.5\%)$ |
| $\bf ab (37.5\%)$                            | $ab/ab (37.5\%)$ |
| $\bf Ab (12.5\%)$                            | $Ab/ab (12.5\%)$ |
| $\bf aB (12.5\%)$                            | $aB/ab (12.5\%)$ |

**Phénotypes et Fréquences dans la Descendance du Test-Cross:**

| Génotype Observé | Phénotype Observé | Fréquence Prédite | Classification |
| :--------------- | :---------------- | :---------------- | :------------- |
| $AB/ab$            | $[AB]$              | $37.5\%$             | Type Parental  |
| $ab/ab$            | $[ab]$              | $37.5\%$             | Type Parental  |
| $Ab/ab$            | $[Ab]$              | $12.5\%$             | Type Recombiné |
| $aB/ab$            | $[aB]$              | $12.5\%$             | Type Recombiné |
| **Total**        |                   | $\bf 100\%$          |                |

---

## PAGE 3 — Phénotypes, Gènes Liés & Brassage Intra-Chromosomique

### NB₂ : Fréquences Phénotypiques en $F_2$ et Signification

Ces sections abordent les différents rapports phénotypiques qui peuvent être observés en $F_2$ (descendance d'un croisement entre deux individus $F_1$ hétérozygotes) et comment ils diffèrent des attentes mendéliennes classiques, notamment en présence de linkage.

*   **Rapport Standard (Gènes Indépendants):**
    Pour deux gènes indépendants, un croisement dihibride ($F_1 \times F_1$) donne en $F_2$ une répartition de $4$ phénotypes dans les proportions $\bf 9:3:3:1$.
    *   $\Sigma \text{ph}$: Nombre total d'unités dans le ratio (par ex., $9+3+3+1 = 16$).
    *   $\equiv \text{ph}$: Représente le nombre de phénotypes distincts observés (ici $4$).
    *   La proportion $9$ correspond au double dominant.

*   **Rapports Phénotypiques Modifiés (Linkage, Épistasie, Létalité):**
    Les rapports non-standards (par exemple, $3-3-5-1$, $4-8-2-2$, $6-3-2-1$, $4-2-2-2-1-1$, $6-3-3-2-1-1$, $-1-1-1-1$) indiquent que la ségrégation des caractères ne suit pas les lois de Mendel pour des gènes indépendants. Ces modifications peuvent être dues à:
    *   **Linkage génétique:** Les gènes sont sur le même chromosome, modifiant les proportions de gamètes.
    *   **Épistasie:** Interaction entre gènes où un gène masque l'expression d'un autre.
    *   **Gènes létaux:** Certains génotypes peuvent être non viables, altérant les rapports attendus.
    *   **Pénétrance ou expressivité incomplète:** L'expression du phénotype n'est pas systématique ou complète pour un génotype donné.

Ces ratios indiquent souvent une prédominance des combinaisons parentales ou des distributions très spécifiques, s'éloignant des $9:3:3:1$ ou $1:1:1:1$ des test-cross indépendants.

---

### II — Gènes Liés Absolument

#### 1. Gènes Liés Absolument (ou Complet):
Deux gènes sont dits **liés absolument** lorsque leur proximité sur le même chromosome est telle qu'aucun **crossing-over** ne peut se produire entre eux. Dans ce cas, les gènes sont toujours transmis ensemble.
*   Il n'y a **aucune formation de gamètes recombinées**.
*   Seuls les **types parentaux** sont observés dans la descendance.
*   La **fréquence de recombinaison $(P)$ est de $0\%$**.

#### 2. Notion de Brassage Intra-chromosomique (Crossing-Over):
Le **brassage intra-chromosomique** est le processus par lequel des segments d'ADN sont échangés entre les chromatides non-sœurs de chromosomes homologues pendant la prophase I de la méiose. C'est ce phénomène qui permet la création de nouvelles combinaisons d'allèles sur un même chromosome, conduisant à la **recombinaison génétique**.

[[Placeholder: Diagramme détaillé de la méiose, illustrant la prophase I avec les chromosomes homologues appariés et un chiasma (point de crossing-over), montrant la formation de chromatides recombinées.]]

**Explication des schémas (symbolisés par $A/a$, $B/b$ et $C.O.$):**

Considérons une paire de chromosomes homologues portant deux gènes, $G_1$ (allèles $A/a$) et $G_2$ (allèles $B/b$).

*   **Avant crossing-over (Chromosomes Parentaux):**
    Supposons un individu hétérozygote pour les deux gènes avec les allèles $A$ et $B$ sur un chromosome, et $a$ et $b$ sur l'homologue (configuration *cis*).
    Chromosome 1: $---A----B---$
    Chromosome 2: $---a----b---$

*   **Après crossing-over (Formation de Gamètes):**
    Si un événement de crossing-over se produit entre les positions des gènes $A$ et $B$, cela va créer de nouvelles combinaisons d'allèles sur les chromatides:
    Gamètes formées (après méiose, en considérant une seule cellule):
    1.  $---A----B---$ (Parental)
    2.  $---a----b---$ (Parental)
    3.  $---A----b---$ (Recombiné)
    4.  $---a----B---$ (Recombiné)

---

### Interprétation de la Fréquence de Recombinaison $(P)$

La **fréquence de recombinaison $(P)$** est une mesure directe de la distance génétique entre deux gènes sur un chromosome. Elle est généralement exprimée en pourcentage ou en unités de carte (centimorgans, cM), où $1\%$ de recombinaison $= 1 \text{ cM}$.

*   $\bf P \ge 50\% \rightarrow \text{Comportement Indépendant (C. Indps.):}$
    Lorsque la fréquence de recombinaison est égale ou supérieure à $50\%$, les gènes se comportent comme s'ils étaient sur des chromosomes différents ou très éloignés l'un de l'autre sur le même chromosome (au-delà d'une distance de $50 \text{ cM}$), ce qui rend le nombre de recombinés égal ou supérieur au nombre de parentaux $(\chi P \approx \chi R)$.

*   $\bf P = 0\% \rightarrow \text{Gènes Liés Absolument:}$
    Aucun crossing-over ne se produit entre les gènes. Seuls les types parentaux sont formés. La fréquence des recombinés $(\chi R)$ est de $0\%$.

*   $\bf 0\% < P < 50\% \rightarrow \text{Gènes Liés Partiellement:}$
    Des crossing-over peuvent se produire, mais pas à chaque méiose ou pas de manière à générer une fréquence égale de parentaux et recombinés. Les types parentaux $(\chi P)$ sont significativement plus fréquents que les types recombinés $(\chi R)$. La valeur de $P$ est directement proportionnelle à la distance physique entre les gènes.

---

### Tableau Récapitulatif (Configuration Génotypique)

Ce tableau résume les configurations des allèles sur les chromosomes homologues pour différentes générations et la terminologie associée:

| Génération | Configuration Chromosomique (Allèles) | Phénotypes (ex) | Terme Associé        |
| :--------- | :------------------------------------ | :-------------- | :------------------- |
| **P₁**     | $A B / A B$                         | $[AB]$            | Parents homozygotes  |
| **P₂**     | $a b / a b$                         | $[ab]$            | Parents homozygotes  |
| **F₁**     | $A B / a b$                             | $[AB]$            | **Cis (Couplage)**   |
| **F₁**     | $A b / a B$                             | $[Ab]$ ou $[aB]$    | **Trans (Répulsion)** |

*   **Cis (Couplage):** Les deux allèles dominants $(A \text{ et } B)$ sont sur un chromosome, et les deux allèles récessifs $(a \text{ et } b)$ sont sur l'homologue. (Ex: $AB/ab$)
*   **Trans (Répulsion):** Un allèle dominant et un allèle récessif sont sur le même chromosome, et vice-versa sur l'homologue. (Ex: $Ab/aB$)
Ces configurations déterminent quels sont les types parentaux et recombinés dans la descendance d'un individu hétérozygote.

---

## PAGE 4 — Linkage Partiel (Application Approfondie)

### ② Test-Cross et Fréquences Comparées

Le **test-cross** est un outil fondamental en génétique pour analyser le linkage. En croisant un individu hétérozygote avec un individu double récessif, les proportions phénotypiques de la descendance reflètent directement les proportions des gamètes produites par l'hétérozygote.

Le tableau ci-dessous compare les proportions phénotypiques attendues dans la descendance d'un test-cross pour différents scénarios:

| Phénotype Descendance (Test-Cross) | Gènes Indépendants $(P=50\%)$ | Liés Absolument (Configuration Cis) | Liés Absolument (Configuration Trans) |
| :------------------------------- | :------------------------- | :---------------------------------- | :------------------------------------ |
| $[AB]$                         | $1/4$ ($25\%$)                  | $1/2$ ($50\%$)                           | $0\%$                                    |
| $[Ab]$                         | $1/4$ ($25\%$)                  | $0\%$                                  | $1/2$ ($50\%$)                             |
| $[aB]$                         | $1/4$ ($25\%$)                  | $0\%$                                  | $1/2$ ($50\%$)                             |
| $[ab]$                         | $1/4$ ($25\%$)                  | $1/2$ ($50\%$)                           | $0\%$                                    |

*   **Gènes Indépendants $(P=50\%)$:** Tous les phénotypes sont en proportions égales ($1:1:1:1$), car il y a autant de gamètes parentales que de gamètes recombinées ($P = 50\%$).
*   **Liés Absolument $(P=0\%)$:** Seuls les types parentaux sont produits.
    *   Si l'hétérozygote $F_1$ est en *cis* $(AB/ab)$, seuls $[AB]$ et $[ab]$ sont observés ($50\%$ chacun).
    *   Si l'hétérozygote $F_1$ est en *trans* $(Ab/aB)$, seuls $[Ab]$ et $[aB]$ sont observés ($50\%$ chacun).
*   **Liés Partiellement $(0\% < P < 50\%)$:** Les proportions des parentaux sont supérieures à $25\%$, et celles des recombinés sont inférieures à $25\%$. Les valeurs exactes dépendent de la fréquence de recombinaison $(P)$.

---

### Application (1) — Déduction de $P$ et Répartition Phénotypique

**Situation:**
Un test-cross est réalisé: un individu hétérozygote $\bf [BR]$ est croisé avec un individu double récessif $\bf [br]$.
Parmi la descendance, on observe $\bf 42\%$ d'individus de phénotype $\bf [br]$.

**1. Déduisez la valeur de $P$ (Fréquence de recombinaison):**

*   Le phénotype $\bf [br]$ est le double récessif. Dans un test-cross, le phénotype double récessif $[br]$ correspond au génotype $br/br$. Pour qu'il y ait $42\%$ de $[br]$, cela signifie que $42\%$ des gamètes produites par l'individu $[BR]$ hétérozygote étaient de type '$br$'.
*   Si le phénotype $[br]$ est observé en proportion élevée ($42\% > 25\%$), il s'agit d'un **type parental**. Ceci indique que l'individu hétérozygote $[BR]$ était en configuration **cis** (génotype $BR/br$).
*   Pour une configuration *cis* ($BR/br$), les gamètes parentales sont $BR$ et $br$. La fréquence de chaque gamète parentale est donnée par la formule: $(1 - P) / 2$.
*   Donc, nous avons l'équation: $ (1 - P) / 2 = 0.42 $
*   Multiplions par $2$: $ 1 - P = 0.84 $
*   Calculons $P$: $ P = 1 - 0.84 $
*   $\bf P = 0.16 \text{ ou } 16\%$

La fréquence de recombinaison est de $\bf 16\%$. C'est une valeur caractéristique de linkage partiel.

**2. Donner la répartition phénotypique totale:**

Maintenant que nous connaissons $P = 16\%$ ($0.16$), nous pouvons déterminer les fréquences de tous les types de gamètes produites par l'individu hétérozygote ($BR/br$) et, par conséquent, les fréquences des phénotypes dans la descendance du test-cross:

*   **Gamètes Parentales ($BR$ et $br$):**
    $$ \text{Fréquence de gamète BR} = \frac{1 - P}{2} = \frac{1 - 0.16}{2} = \frac{0.84}{2} = \bf 0.42 \text{ (42\%)} $$
    $$ \text{Fréquence de gamète br} = \frac{1 - P}{2} = \frac{1 - 0.16}{2} = \frac{0.84}{2} = \bf 0.42 \text{ (42\%)} $$
*   **Gamètes Recombinées ($Br$ et $bR$):**
    $$ \text{Fréquence de gamète Br} = \frac{P}{2} = \frac{0.16}{2} = \bf 0.08 \text{ (8\%)} $$
    $$ \text{Fréquence de gamète bR} = \frac{P}{2} = \frac{0.16}{2} = \bf 0.08 \text{ (8\%)} $$

**Répartition phénotypique de la descendance du test-cross:**

Puisque le mâle pour le test-cross ne produit que des gamètes '$br$', les génotypes et phénotypes de la descendance sont directement déterminés par les gamètes de la femelle:

| Génotype de la Descendance | Phénotype Observé | Fréquence Prédite | Classification |
| :------------------------- | :---------------- | :---------------- | :------------- |
| $BR/br$                      | $\bf [BR]$          | $\bf 42\%$           | Parental       |
| $br/br$                      | $\bf [br]$          | $\bf 42\%$           | Parental       |
| $Br/br$                      | $\bf [Br]$          | $\bf 8\%$            | Recombiné      |
| $bR/br$                      | $\bf [bR]$          | $\bf 8\%$            | Recombiné      |
| **Total**                  |                   | $\bf 100\%$          |                |

---

### NB₁ : Cas Généraux de Fréquences dans un Test-Cross ($F_1[AB] \times [ab]$)

Considérons '$x$' comme la fréquence d'un phénotype spécifique ($[ab]$ dans l'exemple original) dans la descendance d'un test-cross d'un individu $F_1$ hétérozygote avec un double récessif.

*   If $\bf x = 1/4 \text{ (25\%)}:$
    Cela indique que les gènes se comportent comme s'ils étaient **indépendants**. La fréquence de recombinaison $(P)$ est de $50\%$.

*   If $\bf 0\% < x = \theta/2 < 25\%:$
    Cela signifie que '$x$' est la fréquence d'un **type recombiné** (où $\theta$ est la fréquence de recombinaison totale $P$). Ceci serait observé si l'individu $F_1$ hétérozygote était en configuration **trans** ($Ab/aB$) et que le phénotype $[ab]$ est un recombinant. Dans ce cas, $P = 2x$.

*   If $\bf 25\% < x < 50\%:$
    Cela indique que '$x$' est la fréquence d'un **type parental**. Ceci est caractéristique d'un **linkage partiel** où les types parentaux sont plus nombreux que $25\%$. Pour un phénotype parental '$x$' (comme $[ab]$ si le $F_1$ est $AB/ab$), la relation est: $ (1 - P) / 2 = x $, ce qui permet de calculer $ P = 1 - 2x $.

Ces trois scénarios permettent de diagnostiquer le type de linkage (ou son absence) et de calculer la distance génétique $(P)$ entre les gènes.
---

## EXPANDED SECTION: Complete Genetics Analysis

### 1. The Fundamental Question: Linked or Independent?

In dihybrid genetics, the first and most critical question is always: Are the two genes located on the same chromosome or on different chromosomes?

This single question determines everything that follows:

*   The expected offspring ratios
*   The method of analysis
*   The interpretation of experimental results
*   The ability to construct genetic maps

Let me walk you through the logic as a geneticist would think it through.

---

### 2. Independent Assortment: The Mendelian Baseline

When two genes are on different chromosomes, they obey Mendel's Law of Independent Assortment. During meiosis I, homologous chromosomes align randomly at the metaphase plate. The orientation of one chromosome pair does not influence the orientation of another.

For a dihybrid cross ($AaBb \times AaBb$):

The gametes produced are:

*   AB: $25\%$
*   Ab: $25\%$
*   aB: $25\%$
*   ab: $25\%$

When these combine randomly, we get the famous $9:3:3:1$ phenotypic ratio in the $F_2$ generation.

| Phenotype               | Genotype | Ratio   |
| :---------------------- | :------- | :------ |
| Dominant A, Dominant B  | $A\_B\_$  | $9/16$  |
| Dominant A, recessive b | $A\_bb$   | $3/16$  |
| Recessive a, Dominant B | $aaB\_$   | $3/16$  |
| Recessive a, recessive b| $aabb$   | $1/16$  |

For a test cross ($AaBb \times aabb$):
If the genes are independent, the four phenotypic classes appear in equal proportions: $1:1:1:1$.

Any significant deviation from these ratios suggests linkage.

---

### 3. Gene Linkage: When Chromosomes Stick Together

When two genes are located on the same chromosome, they are physically connected. During gamete formation, they tend to travel together unless crossing over separates them.

**Important:** Linkage is not absolute. Crossing over during prophase I of meiosis can exchange genetic material between homologous chromosomes, creating new combinations.

#### The Two Phases of Linkage

**Coupling (cis) phase:**

*   The dominant alleles are on one chromosome: $AB / ab$
*   Parental gametes: $AB$ and $ab$
*   Recombinant gametes: $Ab$ and $aB$

**Repulsion (trans) phase:**

*   One dominant and one recessive on each chromosome: $Ab / aB$
*   Parental gametes: $Ab$ and $aB$
*   Recombinant gametes: $AB$ and $ab$

This distinction is crucial because it affects which phenotypes appear as the parental types in test cross offspring.

---

### 4. Recombination Frequency: The Key Measurement

The percentage of recombinant offspring reveals the distance between linked genes:

$$ RF = \frac{\text{Recombinants}}{\text{Total offspring}} \times 100\% $$

Where:

*   Recombinants = offspring showing new combinations of alleles not present in either parent
*   Parentals = offspring showing the same combinations as the original parents

**Important principle:**

*   $RF = 0\%$ $\rightarrow$ complete linkage (no crossing over)
*   $RF = 50\%$ $\rightarrow$ genes behave as if independent (either on different chromosomes or very far apart on the same chromosome)
*   $0\% < RF < 50\%$ $\rightarrow$ partial linkage (genes on same chromosome at some distance)

---

### 5. Genetic Mapping: Building the Chromosome

One of the most beautiful discoveries in genetics: recombination frequency is approximately proportional to physical distance.

*   $1\%$ recombination = $1$ map unit = $1$ centiMorgan ($cM$)

This allows us to construct genetic maps showing the order and relative distances of genes on a chromosome.

**Example from your notes:** $C_5 – A_9, B_6$

This notation strongly suggests a genetic map where:

*   Gene $C$ is at position $5$
*   Gene $B$ is at position $6$
*   Gene $A$ is at position $9$

Therefore:

*   Distance $C–B = 1$ map unit ($6 - 5 = 1$)
*   Distance $B–A = 3$ map units ($9 - 6 = 3$)
*   Distance $C–A = 4$ map units ($9 - 5 = 4$)

Gene order: $C — B — A$

```
Chromosome:   |---1---|-----3-----|
            C       B           A
           5       6           9
```

---

### 6. Types of Dominance: How Alleles Interact

Your notes touch on multiple dominance patterns. Let's expand each with concrete examples.

#### a) Complete Dominance

The classic Mendelian pattern. The dominant allele produces enough functional protein to mask the recessive.

**Example:** Pea flower color

*   Allele $P$: purple pigment production
*   Allele $p$: no pigment production
*   $PP$: purple
*   $Pp$: purple (one functional copy is enough)
*   $pp$: white

#### b) Incomplete Dominance (Autodomaine)

The heterozygote shows an intermediate phenotype. This occurs when one functional copy produces only half the protein, and half is insufficient for full expression.

**Example:** Snapdragon flower color

*   Allele $R$: red pigment
*   Allele $r$: no pigment
*   $RR$: red
*   $Rr$: pink (half the pigment)
*   $rr$: white

Your notes provide a beautiful example:

P : Fusée normal / F : Fleuve rouge / F : $100\%$ Fusée normal – fleur rose

This is classic incomplete dominance: red $\times$ white $\rightarrow$ $100\%$ pink (rose) in $F_1$.

#### c) Codominance (Double dominance)

Both alleles are expressed fully and simultaneously. Neither is dominant; both contribute equally to the phenotype.

**Example:** Human ABO blood group

*   Allele $I^A$: produces A antigen
*   Allele $I^B$: produces B antigen
*   $I^A I^A$: type A blood
*   $I^B I^B$: type B blood
*   $I^A I^B$: type AB blood (both antigens present)
*   $ii$: type O blood (neither antigen)

Your notes mention "Rouge = P blanc = b" which likely refers to a codominant system where red and white alleles together produce a mixed phenotype (possibly spotted or striped).

---

### 7. Sex-Linked Inheritance: The X Chromosome Special Case

When a gene is located on the X chromosome, inheritance patterns differ between males and females because:

*   Females (XX): two copies, follow typical dominant/recessive rules
*   Males (XY): only one copy, express whatever allele is present (hemizygous)

**Classic example:** Drosophila eye color

*   $X^R$: red eyes (dominant)
*   $X^r$: white eyes (recessive)
*   $X^R X^R$: red-eyed female
*   $X^R X^r$: red-eyed female (carrier)
*   $X^r X^r$: white-eyed female
*   $X^R Y$: red-eyed male
*   $X^r Y$: white-eyed male

**Key pattern:** Recessive X-linked traits appear more frequently in males, who inherit the trait from their carrier mothers.

Your notes mention:

Proche une érosphère : $a_1 = 6A + XX$

This appears to be describing a sex-linked gene in a species with XX/XY system, though the notation "$6A$" is unclear—possibly indicating a specific locus or experimental cross.

---

### 8. The Chi-Square Test: Validating Your Hypothesis

When you observe offspring numbers, you must determine whether deviations from expected ratios are due to chance or real linkage.

The chi-square formula:

$$ \chi^2 = \sum \frac{(O - E)^2}{E} $$

Where:

*   $O$ = observed frequency
*   $E$ = expected frequency
*   $\sum$ = sum across all phenotypic classes

**Degrees of freedom (df):**

*   $df$ = (number of phenotypic classes) - $1$
*   For a dihybrid test cross with $4$ classes, $df = 3$

**Critical values:**

*   If $\chi^2 <$ critical value (usually $7.815$ for $df=3$ at $p=0.05$), accept the hypothesis (genes are independent)
*   If $\chi^2 >$ critical value, reject the hypothesis (genes are linked)

**L'abaque (nomogram):**
Your notes mention "Grenes liés à Abaque." This refers to using a chi-square nomogram—a graphical tool that allows you to quickly determine significance without calculating $\chi^2$ manually. You simply plot your observed and expected values and read off the result.

---

### 9. The Test Cross: The Classic Linkage Detection Experiment

To determine if two genes are linked, geneticists perform a test cross:

1.  Take an $F_1$ individual heterozygous for both genes ($AaBb$)
2.  Cross it with a double recessive ($aabb$)
3.  Examine the offspring phenotypes

**If genes are independent:**

*   Four classes in $1:1:1:1$ ratio
*   Parental types = recombinant types

**If genes are linked:**

*   Four classes with unequal frequencies
*   Parental types $>$ recombinant types
*   The deviation from $1:1:1:1$ reveals linkage

**Example from your notes:**

Émotion : 1 phénotypes ($346$) $|$ $16$ $|$ $3$ $|$ $1$

This likely represents the four phenotype classes from a test cross:

*   Class 1: $346$ offspring (parental type)
*   Class 2: $16$ offspring (recombinant type)
*   Class 3: $3$ offspring (recombinant type)
*   Class 4: $1$ offspring (parental type)

Total = $346 + 16 + 3 + 1 = 366$ offspring
Recombinants = $16 + 3 = 19$

$$ RF = \frac{19}{366} \times 100\% \approx 5.19\% $$

This indicates the genes are linked at a distance of approximately $5.2$ map units.

---

### 10. The Repetitive Lists: $A_9, B_6, C_5, G_1–G_{400}$

The extensive repetition of gene symbols in your notes serves a specific purpose: rote memorization of genetic maps.

In classical genetics problems, you often need to:

*   Memorize the order of genes on a chromosome
*   Recall map distances between them
*   Predict crossover frequencies
*   Calculate the proportion of each gamete type

The format $A_9, B_6, C_5$ is a compact notation:

*   Letter = gene name
*   Number = map position (in centiMorgans from a reference point)

Thus, $C_5 – B_6 – A_9$ indicates gene order with specific distances.

The long lists ($G_1$ through $G_{400}$) are likely memorization drills where the student writes out all genes in order to internalize the map before an exam.

---

### 11. Practical Application: Solving a Complete Problem

Let me reconstruct a complete problem from your fragments and solve it step by step.

#### Problem Statement

In a certain plant:

*   Stem type: Fusée ($F$) dominant over blanche ($f$)
*   Flower color: Red ($R$) and white ($r$) show incomplete dominance ($Rr = \text{rose}$)

A cross between:

*   Fusée normal $\times$ Blanche red

Produces $F_1$: $100\%$ Fusée, rose

The $F_1$ is test crossed with blanche, white.

Offspring:

| Phenotype       | Count |
| :-------------- | :---- |
| Fusée, rose     | $346$   |
| Fusée, white    | $16$    |
| Blanche, rose   | $3$     |
| Blanche, white  | $1$     |

**Questions:**

1.  Are the genes linked?
2.  What is the recombination frequency?
3.  What is the map distance?
4.  What were the parental genotypes?

#### Solution

**Step 1: Identify parental types**

In a test cross, parental types are the most frequent classes that match the $F_1$'s allele combinations.

Since $F_1$ is Fusée, rose:

*   If genes are in coupling: $F_1$ genotype = $FR / fr$ (one chromosome has $F$ and $R$, the other has $f$ and $r$)
*   Parental gametes from $F_1$ = $FR$ and $fr$
*   Parental offspring = Fusée, rose ($FR/fr$) and blanche, white ($fr/fr$)

But our data shows:

*   Fusée, rose = $346$
*   Blanche, white = $1$

These are not equal! This suggests the $F_1$ was actually in repulsion phase: $Fr / fR$ (one chromosome has $F$ and $r$, the other has $f$ and $R$).

Then:

*   Parental gametes = $Fr$ and $fR$
*   Parental offspring = Fusée, white and blanche, rose

Looking at data:

*   Fusée, white = $16$
*   Blanche, rose = $3$

These are actually the smallest classes—contradiction.

**Reinterpretation:** The numbers might be mislabeled in the original problem statement or notes. In typical problems, the two largest classes are parentals, and the two smallest are recombinants.

Let's assume the largest class (Fusée, rose = $346$) is a parental type.
And the smallest class (Blanche, white = $1$) is the other parental type.
This would mean the $F_1$ was in **coupling** ($FR/fr$), producing $FR$ and $fr$ as parental gametes.

The recombinant types would then be Fusée, white ($16$) and Blanche, rose ($3$).

**Step 2: Calculate recombination frequency**

Using the reinterpreted parental/recombinant classifications:

$$ RF = \frac{\text{Recombinants}}{\text{Total offspring}} = \frac{16 + 3}{346 + 16 + 3 + 1} = \frac{19}{366} \approx 0.0519 = \bf 5.19\% $$

**Step 3: Interpret**

$RF = 5.19\%$ $\rightarrow$ The genes are **linked** at a distance of approximately $\bf 5.2 \text{ centiMorgans}$.

**Step 4: Parental genotypes**

Based on the $F_1$ (Fusée, rose) and the initial cross ("Fusée normal $\times$ Blanche red"):

*   Fusée is dominant ($F>f$)
*   Red and white show incomplete dominance ($R, r$; $Rr=\text{rose}$)

The $F_1$ is $100\%$ Fusée, rose, meaning the parental cross must have been:

*   Fusée normal (pure) $\rightarrow FF$
*   Blanche red (pure) $\rightarrow rr$ (this is contradictory as red is $R$, not $r$. Assuming "Blanche red" meant pure Red for flower color, $RR$)
*   Let's assume "Fusée normal" is $FFRR$ and "Blanche red" is $ffrr$. This leads to $F_1$ as $FfRr$, which matches Fusée, rose phenotype.

**Original Parents:**

*   Fusée normal: $FFRR$ (phénotype Fusée, Red)
*   Blanche red: $ffrr$ (phénotype Blanche, white)

**$F_1$ Genotype:** $FfRr$ (phénotype Fusée, rose)
**Linkage Configuration in $F_1$**: Since $F_1$ was derived from $FFRR \times ffrr$, the alleles $F$ and $R$ came from one parent and $f$ and $r$ from the other. Thus, the $F_1$ is in **coupling** ($FR/fr$).

---

### 12. Summary Table: Key Genetic Ratios

| Situation                                       | Cross Type       | Expected Ratio                         |
| :---------------------------------------------- | :--------------- | :------------------------------------- |
| Independent assortment, complete dominance      | $AaBb \times AaBb$ | $9:3:3:1$                              |
| Independent assortment, complete dominance      | $AaBb \times aabb$ | $1:1:1:1$                              |
| Independent assortment, incomplete dominance    | $AaBb \times AaBb$ | Modified $9:3:3:1$ (e.g., $3:6:3:1:2:1$) |
| Complete linkage (no crossing over)             | $AB/ab \times aabb$ | $1:1$ (two classes only)               |
| Partial linkage                                 | $AB/ab \times aabb$ | Parentals $>$ recombinants             |
| Sex-linked, complete dominance                  | $X^RX^r \times X^RY$ | Specific to sex                        |

---

### 13. Final Synthesis: What Your Notes Reveal

Your handwritten notes document a complete classical genetics curriculum focused on:

1.  Two-gene inheritance patterns (dihybridism)
2.  Distinguishing independent assortment from linkage
3.  Calculating recombination frequencies and map distances
4.  Understanding dominance types (complete, incomplete, codominant)
5.  Recognizing autosomal vs. sex-linked inheritance
6.  Using chi-square tests (with abaque/nomogram) to validate hypotheses
7.  Memorizing genetic maps through repetition

The fragmented, repetitive style is typical of a student actively working through problems, writing key numbers and conclusions, and drilling map positions into memory.

---

### RECOMMENDATIONS FOR YOUR OBSIDIAN NOTE

1.  **Keep the LaTeX equations** – they will render beautifully in Obsidian.
2.  **Replace image placeholders** with:
    *   Actual diagrams you draw
    *   Screenshots from textbooks
    *   Links to online genetics resources
3.  **Add callouts for key formulas:**
    ```markdown
    > [!formula] Recombination Frequency
    > RF = (Recombinants / Total) \times 100%
    ```
4.  **Create links between related notes** (e.g., [[Mendelian Genetics]], [[Chi-Square Test]]).

---
