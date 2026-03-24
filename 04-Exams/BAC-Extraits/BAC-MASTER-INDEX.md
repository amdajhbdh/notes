# BAC Mauritanie - Index Complet

## 📊 Collection Complète (2012-2025)

Cette collection contient tous les examens BAC Mauritanie disponibles avec :
- ✅ Textes originaux (PDF → TXT)
- ✅ Notes structurées en Markdown
- ✅ Graphiques (PNG)
- ✅ Canevas Obsidian (.canvas)
- ✅ Codes TikZ/PGFPlots

---

## 📁 Structure des Fichiers

```
04-Exams/BAC-Extraits/
├── Textes originaux (38 fichiers .txt)
│   ├── BacD2025.txt → BacD2012.txt
│   ├── BacC2025.txt → BacC2012.txt
│   ├── BacLM2019.txt, BacLM2018.txt
│   └── BacLO2019.txt → BacLO2016.txt
│
├── Notes Markdown (5 fichiers .md)
│   ├── BAC-2025-D-SN.md
│   ├── BAC-2025-C-M.md
│   ├── BAC-2024-D-SN.md
│   ├── BAC-2022-D-SN.md
│   └── GRAPHES-INVENTORY.md
│
├── Graphiques PNG (8 fichiers)
│   └── Graphiques/
│       ├── BAC-2025-D-Ex3.png    # Courbe exponentielle
│       ├── BAC-2025-D-Ex2.png    # Plan complexe
│       ├── BAC-2024-D-Ex3.png   # Courbe avec asymptote
│       ├── BAC-2024-D-Ex4.png   # Plan complexe
│       ├── BAC-2022-D-Ex4.png   # Courbe différentielle
│       ├── BAC-2021-D-Ex2.png   # Plan complexe
│       ├── BAC-2020-D-Ex2.png   # Parallélogramme
│       ├── BAC-2019-D.png
│       └── BAC-2018-D.png
│
├── Canevas Obsidian (3 fichiers)
│   ├── BAC-2025-D.canvas
│   ├── BAC-2024-D.canvas
│   ├── BAC-MASTER.canvas
│   └── BAC-COMPLETE.canvas       # Vue d'ensemble
│
└── TikZ (codes LaTeX)
    └── TikZ/
        ├── BAC-2025-D-Ex3-Courbe.tex
        ├── BAC-2025-D-Ex2-PlanComplexe.tex
        ├── BAC-2025-C-Ex3-Geometrie.tex
        ├── BAC-2024-D-Ex3-Courbe.tex
        ├── BAC-2024-D-Ex4-PlanComplexe.tex
        ├── BAC-2022-D-Ex2-PlanComplexe.tex
        └── BAC-2022-D-Ex4-Courbe.tex
```

---

## 📈 Année par Année

### 2025 (Complet)
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| D | 4 (20 pts) | Ex2, Ex3 |
| C | 4 (15 pts) | Ex3 |

### 2024 (Complet)
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| D | 4 (15 pts) | Ex3, Ex4 |

### 2022 (Complet)
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| D | 4 (14 pts) | Ex2, Ex4 |

### 2021
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| D | 4 | Ex2 |

### 2020
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| D | 4 | Ex2 |

### 2019
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| D | 4 | ✓ |
| LM | 2 | - |
| LO | 2 | - |

### 2018
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| D | 4 | ✓ |
| LM | 2 | - |
| LO | 2 | - |

### 2017
| Série | Exercices | Graphiques |
|-------|-----------|------------|
| C | 1 | - |

---

## 🔢 Sujets Couverts

| Matière | Années | Status |
|---------|--------|--------|
| Math D (Sciences Naturelles) | 2012, 2015-2025 | ✅ 13 ans |
| Math C (Mathématiques) | 2012-2025 | ✅ 14 ans |
| LM (Lettres Modernes) | 2018-2019 | ✅ |
| LO (Lettres Originales) | 2016, 2018-2019 | ✅ |
| Physique/Chimie | - | ❌ Non disponible |

---

## 🎯 Concepts Maths par Année

| Année | Probabilités | Complexes | Analyse | Suites | Géométrie |
|-------|--------------|-----------|---------|--------|------------|
| 2025 | ✓ | ✓ | ✓ (exp, log) | - | ✓ |
| 2024 | ✓ | ✓ | ✓ (exp) | - | - |
| 2022 | ✓ | ✓ | ✓ (diff) | ✓ | - |
| 2021 | - | ✓ | ✓ | ✓ | - |
| 2020 | - | ✓ | ✓ | ✓ | - |
| 2019 | ✓ | ✓ | ✓ | ✓ | - |
| 2018 | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## 🚀 Utilisation

### Dans Obsidian
1. Copier les fichiers `.canvas` dans le vault
2.Importer les images `.png` dans les notes
3. Utiliser les liens `[[...]]` pour naviguer

### Pour LaTeX
1. Compiler les fichiers `.tex` dans `TikZ/`
2. Requires: `texlive-latex-base`, `texlive-pgfplots`

### Pour Python
1. Modifier les scripts dans `Graphiques/`
2. Exécuter: `python3 Graphiques/BAC-2025-D-Ex3.py`

---

## 📝 Notes

- **2023**: Non disponible (pas de source en ligne)
- **Physique/Chimie**: Non disponible sur les sources consultées
- **Français/Philosophie**: Non disponible

---

*Dernière mise à jour: 2026-03-24*
*Source: maurimath.net, SIGMaths, Devoir.TN*