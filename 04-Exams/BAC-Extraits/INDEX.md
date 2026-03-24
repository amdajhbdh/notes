# BAC-Extraits - Index des Ressources

Ce dossier contient les ressources extraites et générées pour les examens BAC Mauritanie.

---

## 📁 Contenu

### Textes Originaux (38 fichiers)
Tous les PDFs convertis en texte:
- `BacD2025.txt` → `BacC2012SC.txt` (38 fichiers)

### Notes Markdown (5 fichiers)
- `BAC-2025-D-SN.md` - BAC 2025 Série D
- `BAC-2025-C-M.md` - BAC 2025 Série C  
- `BAC-2024-D-SN.md` - BAC 2024 Série D
- `BAC-2022-D-SN.md` - BAC 2022 Série D
- `GRAPHES-INVENTORY.md` - Inventaire des graphiques

### Graphiques PNG (8 fichiers)
| Fichier | Description |
|---------|-------------|
| `BAC-2025-D-Ex3.png` | Courbe $f(x)=(e^x-x-2)e^{-x}$ |
| `BAC-2025-D-Ex2.png` | Plan complexe A, B, C |
| `BAC-2024-D-Ex3.png` | Courbe $f(x)=x-3+\frac12 e^x$ |
| `BAC-2024-D-Ex4.png` | Plan complexe A, B, C, I |
| `BAC-2022-D-Ex4.png` | Courbe $f(x)=-(x+1)e^{-x}-1$ |
| `BAC-2021-D-Ex2.png` | Plan complexe |
| `BAC-2020-D-Ex2.png` | Parallélogramme |
| `BAC-2019-D.png` | Plan complexe |

### Canevas Obsidian (4 fichiers)
- `BAC-2025-D.canvas` - Vue BAC 2025 D
- `BAC-2024-D.canvas` - Vue BAC 2024 D
- `BAC-MASTER.canvas` - Index visuel
- `BAC-COMPLETE.canvas` - Vue complète

### TikZ/LaTeX (7 fichiers)
Codes sources pour graphiques:
- `TikZ/BAC-2025-D-Ex3-Courbe.tex`
- `TikZ/BAC-2025-D-Ex2-PlanComplexe.tex`
- `TikZ/BAC-2025-C-Ex3-Geometrie.tex`
- `TikZ/BAC-2024-D-Ex3-Courbe.tex`
- `TikZ/BAC-2024-D-Ex4-PlanComplexe.tex`
- `TikZ/BAC-2022-D-Ex2-PlanComplexe.tex`
- `TikZ/BAC-2022-D-Ex4-Courbe.tex`

---

## 🔧 Générer Nouveaux Graphiques

```bash
cd Graphiques
python3 BAC-2025-D-Ex3.py  # Génère le graphique correspondant
python3 generate_all.py    # Génère tous les graphiques
```

---

*Dernière mise à jour: 2026-03-24*