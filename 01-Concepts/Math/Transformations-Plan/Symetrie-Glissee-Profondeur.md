# Profondeur : La Symétrie Glissée (Antidéplacement sans point fixe)

> [!info] Définition
> Une symétrie glissée $f$ est la composée d'une réflexion d'axe $\Delta$ et d'une translation de vecteur $\vec{u}$, à condition que $\vec{u}$ soit **parallèle** à $\Delta$.
> $$f = t_{\vec{u}} \circ S_{\Delta} = S_{\Delta} \circ t_{\vec{u}}$$

---

## Méthodes de Détermination (BAC)

### 1. Par deux points et leurs images
Si on sait que $f(A) = A'$ et $f(B) = B'$, et que $(\vec{AB}, \vec{A'B'}) \equiv -(\vec{AB}, \vec{AC}) \pmod{2\pi}$ (antidéplacement) :
1. **Trouver l'axe $\Delta$** : C'est la droite passant par les milieux des segments $[AA']$ et $[BB']$.
   *Attention : Si les milieux sont confondus, c'est une réflexion pure.*
2. **Trouver le vecteur $\vec{u}$** : C'est le vecteur qui transforme le projeté de $A$ sur $\Delta$ en $A'$.

### 2. Par la forme $f \circ f$
C'est la méthode la plus rapide en calcul vectoriel :
- Si $f$ est une symétrie glissée de vecteur $\vec{u}$, alors $f \circ f$ est une **translation** de vecteur $2\vec{u}$.
- **Calcul :** $f(f(M)) = M + 2\vec{u}$.

---

## Propriétés de l'Axe $\Delta$ (L'Invariant)
Contrairement aux rotations ou homothéties, il n'y a pas de point $M$ tel que $f(M) = M$. 
Cependant, pour tout point $M$ du plan :
- Le milieu $I$ de $[M, f(M)]$ appartient toujours à l'axe $\Delta$.
- L'image de l'axe $\Delta$ par $f$ est $\Delta$ lui-même : $f(\Delta) = \Delta$.

---

## Cas complexe : Décomposition de $t_{\vec{v}} \circ S_{\Delta}$
Si le vecteur $\vec{v}$ n'est **pas** parallèle à l'axe $\Delta$ :
1. On décompose $\vec{v} = \vec{v}_{\parallel} + \vec{v}_{\perp}$ (composantes parallèle et normale à $\Delta$).
2. $t_{\vec{v}_{\perp}} \circ S_{\Delta}$ est une réflexion $S_{\Delta'}$ d'axe $\Delta'$ parallèle à $\Delta$.
3. Le résultat final $t_{\vec{v}_{\parallel}} \circ S_{\Delta'}$ est la **forme réduite** de la symétrie glissée.

> [!tip] Astuce visuelle
> Imaginez un pas de marche : on change de côté par rapport à une ligne (réflexion) tout en avançant (translation).

---
*Lien vers : [[Synthese-Transformations]] | [[Transformations-Master.canvas]]*
