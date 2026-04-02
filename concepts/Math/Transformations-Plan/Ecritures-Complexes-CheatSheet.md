#  Aide-Mémoire : Écritures Complexes (BAC C)

Ce guide résume l'identification d'une transformation à partir de son expression complexe $z' = az + b$ ou $z' = a\bar{z} + b$.

---

## Similitudes Directes ($z' = az + b$)

| Valeur de $a$                        | Valeur de $b$      | Transformation                  | Éléments Caractéristiques                      |                        |                                                         |     |                                                            |
| :----------------------------------- | :----------------- | :------------------------------ | :--------------------------------------------- | ---------------------- | ------------------------------------------------------- | --- | ---------------------------------------------------------- |
| $a = 1$                              | $b = 0$            | **Identité** ($id$)             | Tous les points sont invariants.               |                        |                                                         |     |                                                            |
| $a = 1$                              | $b \neq 0$         | **Translation**                 | Vecteur $\vec{u}$ d'affixe $b$.                |                        |                                                         |     |                                                            |
| $a \in \mathbb{R}^* \setminus \{1\}$ | $b \in \mathbb{C}$ | **Homothétie**                  | Rapport $k=a$, Centre $\Omega(\frac{b}{1-a})$. |                        |                                                         |     |                                                            |
| $                                    | a                  | = 1$ ($a \neq 1$)               | $b \in \mathbb{C}$                             | **Rotation**           | Angle $\theta=\arg(a)$, Centre $\Omega(\frac{b}{1-a})$. |     |                                                            |
| $                                    | a                  | \neq 1$ ($a \notin \mathbb{R}$) | $b \in \mathbb{C}$                             | **Similitude Directe** | Rapport $k=                                             | a   | $, Angle $\theta=\arg(a)$, Centre $\Omega(\frac{b}{1-a})$. |

---

## Similitudes Indirectes ($z' = a\bar{z} + b$)

### Cas particulier : Isométries ($|a| = 1$)
On cherche s'il existe des points invariants ($z = a\bar{z} + b$).

1. **Si des points invariants existent** : C'est une **Réflexion** (Symétrie axiale).
   - L'ensemble des points invariants forme l'axe $\Delta$.
2. **Si aucun point invariant n'existe** : C'est une **Symétrie Glissée**.
   - **Vecteur $\vec{u}$** : Affixe $\frac{a\bar{b} + b}{2}$.
   - **Axe $\Delta$** : Droite passant par les milieux de $[M, f(M)]$.

---

## Propriété Fondamentale
Pour toute similitude directe $f(z) = az + b$ de centre $\Omega$, on a la relation :
$$z' - \omega = a(z - \omega)$$
*C'est la forme la plus utile pour les démonstrations de rapports de distance et d'angles.*

---
*Lien vers : [[Synthese-Transformations]] | [[Transformations-Master.canvas]]*
