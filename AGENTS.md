# AGENTS.md - Content Creation and Formatting Rules

## Mathematical Notation Standards

### ✅ **REQUIRED: Use LaTeX for ALL mathematical expressions**

**Inline math**: Use `$...$` for inline expressions
```markdown
The pH is calculated as $pH = -\log[H_3O^+]$
```

**Display math**: Use `$$...$$` for centered equations
```markdown
$$K_a = \frac{[H_3O^+][A^-]}{[AH]}$$
```

### ❌ **FORBIDDEN: ASCII/Unicode math symbols**

**ZERO TOLERANCE POLICY - Never use these in ANY context:**

**Subscripts (FORBIDDEN):**
- H₂O, CO₂, NH₃, SO₄, CH₃, NO₃ → Use `$H_2O$`, `$CO_2$`, `$NH_3$`, `$SO_4$`, `$CH_3$`, `$NO_3$`
- x₀, x₁, x₂, t₀, V₁, I₂ → Use `$x_0$`, `$x_1$`, `$x_2$`, `$t_0$`, `$V_1$`, `$I_2$`

**Superscripts (FORBIDDEN):**
- x², x³, e^x, 10⁻⁴, 10⁻¹⁴, Ca²⁺, m² → Use `$x^2$`, `$x^3$`, `$e^x$`, `$10^{-4}$`, `$10^{-14}$`, `$Ca^{2+}$`, `$m^2$`

**Greek letters (FORBIDDEN):**
- α, β, γ, δ, ε, θ, λ, μ, π, ρ, σ, φ, ω, Δ, Σ, Ω → Use `$\alpha$`, `$\beta$`, `$\gamma$`, `$\delta$`, `$\varepsilon$`, `$\theta$`, `$\lambda$`, `$\mu$`, `$\pi$`, `$\rho$`, `$\sigma$`, `$\phi$`, `$\omega$`, `$\Delta$`, `$\Sigma$`, `$\Omega$`

**Special symbols (FORBIDDEN):**
- ≤, ≥, ≠, ±, ×, ÷, ∑, ∫, √, ∞, ∂ → Use `$\leq$`, `$\geq$`, `$\neq$`, `$\pm$`, `$\times$`, `$\div$`, `$\sum$`, `$\int$`, `$\sqrt{}$`, `$\infty$`, `$\partial$`

**Units with symbols (FORBIDDEN):**
- Ω (ohm), µ (micro), ° (degree) → Use `$\Omega$`, `$\mu$`, `$^\circ$` or write as text: "ohms", "micro", "degrees"

### **Common LaTeX Conversions**

| ASCII/Unicode | LaTeX | Example |
|---------------|-------|---------|
| H₂SO₄ | `$H_2SO_4$` | Sulfuric acid |
| 10⁻¹⁴ | `$10^{-14}$` | Scientific notation |
| α = 0.1% | `$\alpha = 0.1\%$` | Ionization coefficient |
| ΔH° | `$\Delta H^{\circ}$` | Standard enthalpy |
| ∫₀¹ f(x)dx | `$\int_0^1 f(x)dx$` | Definite integral |
| Σᵢ₌₁ⁿ xᵢ | `$\sum_{i=1}^n x_i$` | Summation |

## Content Organization Rules

### **File Structure**
- Use descriptive filenames with hyphens: `Solutions-Aqueuses-Avancees.md`
- Include level indicators: `(7ème/Terminale)`, `(Advanced)`, `(Basic)`
- Add source attribution: `*Source: École XYZ - 2024-2025*`

### **Section Headers**
```markdown
# Main Topic - Subtopic (Level)
## Concepts Clés / Key Concepts  
### Specific Topic
#### Detailed Subtopic
```

### **Exercise Format**
```markdown
## Exercice N: Title

### Énoncé / Problem Statement
[Problem description with LaTeX math]

### Méthode de résolution / Solution Method
1. **Step 1**: Description
   $$equation$$
2. **Step 2**: Description
   $$equation$$

### Résultat / Result
$$final\_answer$$
```

## Quality Standards

### **Mathematical Rigor**
- Always show units: `$C = 0.1 \text{ mol/L}$`
- Use proper notation: `$[H_3O^+]$` not `[H3O+]`
- Include equilibrium arrows: `$\rightleftharpoons$` for reversible reactions
- Use proper chemical formulas: `$CH_3COOH$` not `CH3COOH`

### **Language Standards**
- **French**: Use for Mauritanian BAC content
- **English**: Use for international/general concepts
- **Bilingual**: Provide both when helpful

### **Content Levels**
- **Basic (6ème)**: Simple concepts, basic calculations
- **Intermediate (7ème C/D)**: Complex problems, multiple steps
- **Advanced (7ème/Terminale)**: University-prep level, theoretical depth

## Automated Checks

### **Before Publishing**
1. **Math Check**: Scan for ASCII math symbols
2. **LaTeX Validation**: Ensure all `$...$` and `$$...$$` are properly closed
3. **Level Verification**: Confirm content matches stated difficulty
4. **Source Attribution**: Include original source information

### **Conversion Script Usage**
```bash
# Find ASCII math in files
grep -r "[₀-₉⁺⁻²³¹⁴⁵⁶⁷⁸⁹]" *.md

# Convert common patterns
sed -i 's/H₂O/$H_2O$/g' *.md
sed -i 's/CO₂/$CO_2$/g' *.md
sed -i 's/10⁻¹⁴/$10^{-14}$/g' *.md
```

## Agent Responsibilities

### **Content Extraction Agents**
- Convert all ASCII/Unicode math to LaTeX during extraction
- Maintain source attribution and academic level
- Organize content into appropriate subject folders

### **Quality Assurance Agents**
- Scan for non-LaTeX mathematical notation
- Verify equation formatting and completeness
- Check for proper academic level classification

### **Update Agents**
- Apply formatting rules to existing content
- Maintain consistency across all files
- Update indexes when content is modified

---
*This document must be followed by all content creation and modification agents*
