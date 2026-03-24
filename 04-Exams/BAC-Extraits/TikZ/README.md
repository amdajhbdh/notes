# TikZ/PGFPlots - Figures BAC Mauritanie

Ce dossier contient les codes TikZ et PGFPlots pour les graphiques BAC Mauritanie.

---

## Fichiers Créés

### BAC 2025

| Fichier | Description |
|---------|-------------|
| `BAC-2025-D-Ex3-Courbe.tex` | Courbe $f(x) = (e^x - x - 2)e^{-x}$ avec asymptote $y=1$ |
| `BAC-2025-D-Ex2-PlanComplexe.tex` | Points A($1-i$), B($2+2i$), C($(-1+3i)$) |
| `BAC-2025-C-Ex3-Geometrie.tex` | Triangle ABC rectangle isocèle avec milieux |

### BAC 2024

| Fichier | Description |
|---------|-------------|
| `BAC-2024-D-Ex3-Courbe.tex` | Courbe $f(x) = x - 3 + \frac12 e^x$ avec asymptote $D: y = x - 3$ |
| `BAC-2024-D-Ex4-PlanComplexe.tex` | Points A($3i$), B(1), C($4+i$), I(milieu) |

### BAC 2022

| Fichier | Description |
|---------|-------------|
| `BAC-2022-D-Ex2-PlanComplexe.tex` | Parallélogramme ABCD, ensembles E et F |
| `BAC-2022-D-Ex4-Courbe.tex` | Courbe $f(x) = -(x+1)e^{-x} - 1$ |

---

## Compilation

Pour compiler les fichiers TikZ :

```bash
# Avec pdflatex
pdflatex BAC-2025-D-Ex3-Courbe.tex

# Pour les figures PGFPlots, nécessite --shell-escape
pdflatex -shell-escape BAC-2025-D-Ex3-Courbe.tex
```

---

## Dépendances

- `\usepackage{pgfplots}` - Pour PGFPlots
- `\usepackage{tikz}` - Pour TikZ
- `\usepackage{amsmath}` - Pour formules mathématiques
- `\usepackage{amssymb}` - Pour symboles

---

## Personnalisation

### Ajuster l'échelle
```latex
\begin{tikzpicture}[scale=1.5]
```

### Ajuster les limites
```latex
xmin=-5, xmax=5, ymin=-2, ymax=3
```

### Couleurs
```latex
\addplot[blue, thick] % bleu
\addplot[red, dashed] % rouge pointillé
\addplot[green, dotted] % vert pointillé
```

---

*Dernière mise à jour: 2026-03-24*