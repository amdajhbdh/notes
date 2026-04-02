# 🌀 Les Transformations du Plan : Guide Expert (7e C)

> [!abstract] Objectif BAC
> Maîtriser la classification des isométries et des similitudes, leur écriture complexe et la décomposition des transformations indirectes (symétrie glissée).

---

## 1. Architecture des Transformations

Toute application bijective $f: \mathcal{P} \to \mathcal{P}$ est une transformation. Mais en Terminale C, nous nous focalisons sur celles qui conservent des structures métriques.

### 1.1 La Hiérarchie des Similitudes
Une similitude de rapport $k$ ($k > 0$) multiplie toutes les distances par $k$.

| Type | Rapport | Propriété Clé | Exemples |
| :--- | :--- | :--- | :--- |
| **Isométrie** | $k = 1$ | Conserve la distance | Translation, Rotation, Réflexion |
| **Similitude Propre** | $k \neq 1$ | Change l'échelle | Homothétie, Similitude Directe |

---

## 2. Déplacements vs Antidéplacements

C'est ici que se joue la réussite des exercices de construction.

### 2.1 Les Déplacements (Orientation conservée)
Ils conservent les angles orientés : $(\vec{AB}, \vec{AC}) = (\vec{A'B'}, \vec{A'C'})$.
- **Si $k=1$** : 
    - **Translation** (si aucun point fixe ou $id$).
    - **Rotation** (si un point fixe unique $\Omega$).
- **Si $k \neq 1$** :
    - **Similitude directe** (toujours un centre unique $\Omega$, un rapport $k$, et un angle $\theta$).

### 2.2 Les Antidéplacements (Orientation inversée)
Ils transforment un angle en son opposé.
- **Réflexion (Symétrie axiale)** : Points invariants = une droite $\Delta$.
- **Symétrie Glissée** : Aucun point invariant. Décomposition unique : $f = t_{\vec{u}} \circ S_{\Delta}$ avec $\vec{u}$ directeur de $\Delta$.

> [!danger] Attention au Piège
> Une symétrie glissée **n'a pas de point fixe**, mais elle possède un **axe invariant** (la droite $\Delta$ est globalement invariante, $f(\Delta) = \Delta$).

---

## 3. L'Outil Puissant : Écritures Complexes

Si $z' = az + b$ (Similitude Directe) :

1. **Si $a = 1$** : Translation de vecteur $\vec{u}(b)$.
2. **Si $a \in \mathbb{R}^* \setminus \{1\}$** : Homothétie de rapport $a$ et de centre $\Omega\left(\frac{b}{1-a}\right)$.
3. **Si $|a| = 1$ ($a \neq 1$)** : Rotation d'angle $\arg(a)$ et de centre $\Omega\left(\frac{b}{1-a}\right)$.
4. **Si $|a| \neq 1$ et $a \in \mathbb{C} \setminus \mathbb{R}$** : Similitude directe de rapport $|a|$, d'angle $\arg(a)$ et de centre $\Omega\left(\frac{b}{1-a}\right)$.

---

## 4. Méthode de Composition : Le secret des axes

> [!theory] Composition de deux réflexions $S_{\Delta} \circ S_{\Delta'}$
> - Si $\Delta \parallel \Delta'$ : Le résultat est une **Translation** de vecteur $2\vec{w}$ (où $\vec{w}$ est le vecteur normal joignant $\Delta'$ à $\Delta$).
> - Si $\Delta \cap \Delta' = \{O\}$ : Le résultat est une **Rotation** de centre $O$ et d'angle $2(\vec{u}, \vec{v})$ où $\vec{u}$ et $\vec{v}$ sont les vecteurs directeurs des axes.

---

## 5. Focus : La Symétrie Glissée (La "Bestiole" du programme)

Une symétrie glissée $f$ est caractérisée par un axe $\Delta$ et un vecteur $\vec{u}$ parallèle à $\Delta$.

**Propriétés fondamentales pour les exercices :**
- $f \circ f = t_{2\vec{u}}$. (C'est ainsi qu'on trouve souvent le vecteur).
- Le milieu de $[M, f(M)]$ appartient toujours à l'axe $\Delta$. (C'est ainsi qu'on trouve l'axe).
- Forme réduite : $f = t_{\vec{u}} \circ S_{\Delta} = S_{\Delta} \circ t_{\vec{u}}$. (Commutativité).

---
*Fiche optimisée pour la préparation au concours d'excellence et au BAC.*
