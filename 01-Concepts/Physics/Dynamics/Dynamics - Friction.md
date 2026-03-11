---
tags: [physics, dynamics, friction, forces]
difficulty: medium
---
> [!summary] 📊 Note Summary
> 
> | Property | Value |
> |----------|-------|
> | **Difficulty** | `easy` #difficulty/easy |
> | **Formulas** | 0 |
> | **Concepts** | 0 |
> | **Related Notes** | 10 |
> | **Word Count** | 1016 |
> | **Last Enhanced** | 2026-03-10 |



## 📊 Note Summary

| Property | Value |
|----------|-------|
| Difficulty | Easy |
| Formulas | 0 |
| Concepts | 0 |
| Related Notes | 10 |
| Word Count | 943 |
| Last Enhanced | 2026-03-10 |



# Friction

## Definition
Force that opposes relative motion between surfaces in contact.

## Types of Friction

### 1. Static Friction ($f_s$)
Prevents object from starting to move

**Formula**: $f_s \leq \mu_s N$

Where:
- $\mu_s$ = coefficient of static friction
- N = normal force
- $f_{s,max} = \mu_s N$ (maximum static friction)

### 2. Kinetic Friction ($$f_k$$)
Acts on moving object

**Formula**: $$f_k$ = \mu_k N$

Where:
- $\mu_k$ = coefficient of kinetic friction
- Always: $\mu_k < \mu_s$

## Key Relationships

### Normal Force
- Horizontal surface: N = mg
- Inclined plane: N = mg cos(θ)
- With applied force: N = mg + F sin(θ)

### Direction
- Always opposes motion (or potential motion)
- Parallel to contact surface
- Perpendicular to normal force

## Coefficients of Friction

### Typical Values
| Surfaces | $\mu_s$ | $\mu_k$ |
|----------|-----|-----|
| Steel on steel | 0.74 | 0.57 |
| Wood on wood | 0.5 | 0.3 |
| Ice on ice | 0.1 | 0.03 |
| Rubber on concrete | 1.0 | 0.8 |
| Teflon on Teflon | 0.04 | 0.04 |

### Properties
- Dimensionless (no units)
- Independent of contact area
- Independent of speed (approximately)
- Depends on surface materials

## Problem-Solving Strategy

### Step 1: Draw Free Body Diagram
- Weight (mg) downward
- Normal force (N) perpendicular to surface
- Applied forces
- Friction force (opposite to motion)

### Step 2: Choose Coordinate System
- x-axis along motion direction
- y-axis perpendicular to surface

### Step 3: Apply Newton's Second Law
- ΣFₓ = ma
- ΣFᵧ = 0 (no vertical acceleration)

### Step 4: Solve
- Find N from y-equation
- Calculate friction: f = μN
- Solve for unknown from x-equation

## Examples

### Example 1: Object on Horizontal Surface
10 kg box on floor, $\mu_s$ = 0.4, $\mu_k$ = 0.3
Applied horizontal force F = 30 N

**Find**: Will it move? If yes, find acceleration.

**Solution**:
N = mg = 10 * 10 = 100 N
$f_s$,max = $\mu_s$N = 0.4 * 100 = 40 N

F = 30 N < 40 N  ->  Box doesn't move

If F = 50 N:
F > $f_s$,max  ->  Box moves
$f_k$ = $\mu_k$N = 0.3 * 100 = 30 N
ΣF = F - $f_k$ = 50 - 30 = 20 N
a = F/m = 20/10 = 2 m/s**2

### Example 2: Inclined Plane
5 kg block on 30° incline, $\mu_s$ = 0.5

**Find**: Will it slide?

**Solution**:
N = mg cos(30°) = 5 * 10 * 0.866 = 43.3 N
$f_s$,max = $\mu_s$N = 0.5 * 43.3 = 21.65 N

F∥ = mg sin(30°) = 5 * 10 * 0.5 = 25 N

F∥ > $f_s$,max  ->  Block slides

### Example 3: Pulling at Angle
20 kg box, pull at 37° above horizontal with F = 100 N
$\mu_k$ = 0.25

**Find**: Acceleration

**Solution**:
Vertical: N + F sin(37°) = mg
N = mg - F sin(37°)
N = 200 - 100(0.6) = 200 - 60 = 140 N

$f_k$ = $\mu_k$N = 0.25 * 140 = 35 N

Horizontal: F cos(37°) - $f_k$ = ma
100(0.8) - 35 = 20a
80 - 35 = 20a
a = 45/20 = 2.25 m/s**2

### Example 4: Two Blocks Connected
Block A (5 kg) on table, connected by string over pulley to hanging block B (3 kg)
$\mu_k$ = 0.2 between A and table

**Find**: Acceleration of system

**Solution**:
For A: T - $f_k$ = m_aa
$f_k$ = $\mu_k$m_ag = 0.2 * 5 * 10 = 10 N
T - 10 = 5a ... (1)

For B: m_bg - T = m_ba
30 - T = 3a ... (2)

Add equations:
30 - 10 = 8a
a = 2.5 m/s**2

## Inclined Plane with Friction

### Sliding Down
Net force = mg sin(θ) - $f_k$
= mg sin(θ) - $\mu_k$mg cos(θ)
= mg(sin(θ) - $\mu_k$ cos(θ))

a = g(sin(θ) - $\mu_k$ cos(θ))

### Minimum Angle to Slide
At threshold: mg sin(θ) = $\mu_s$mg cos(θ)
tan(θ) = $\mu_s$
θ = arctan($\mu_s$)

### Example 5
$\mu_s$ = 0.6, find minimum angle

θ = arctan(0.6) = 31°

## Stopping Distance

### With Friction
v**2 = u**2 + 2as
0 = u**2 - 2$\mu_k$gd (deceleration = $\mu_k$g)
d = u**2/(2$\mu_k$g)

### Example 6
Car at 20 m/s, $\mu_k$ = 0.7, find stopping distance

d = 20**2/(2 * 0.7 * 10)
d = 400/14 = 28.6 m

## Air Resistance (Fluid Friction)

### Low Speed (Laminar)
F = bv (proportional to velocity)

### High Speed (Turbulent)
F = cv**2 (proportional to v**2)

### Terminal Velocity
When drag = weight:
mg = cv**2
v_terminal = √(mg/c)

## Rolling Friction

Much smaller than sliding friction
f_roll = μ_roll * N
Typical μ_roll = 0.001 - 0.02

## Practice Problems

### Problem 1
8 kg box, $\mu_s$ = 0.5, $\mu_k$ = 0.3
Horizontal force F = 50 N. Find acceleration.

<details>
<summary>Solution</summary>
N = 80 N
$f_s$,max = 0.5 * 80 = 40 N
F > $f_s$,max  ->  moves
$f_k$ = 0.3 * 80 = 24 N
a = (50-24)/8 = 3.25 m/s**2
</details>

### Problem 2
Block on 45° incline, $\mu_k$ = 0.4
Find acceleration down the plane.

<details>
<summary>Solution</summary>
a = g(sin(45°) - $\mu_k$cos(45°))
= 10(0.707 - 0.4×0.707)
= 10(0.707 - 0.283)
= 4.24 m/s**2
</details>

### Problem 3
Car braking, initial speed 25 m/s, $\mu_k$ = 0.6
Find stopping distance.

<details>
<summary>Solution</summary>
d = u**2/(2$\mu_k$g)
= 625/(2×0.6×10)
= 625/12 = 52.1 m
</details>

## Related
- [[Dynamics - Newton Laws]]
- [[Dynamics - Forces]]
- [[Dynamics - Circular Motion]]


## 🔗 Related Notes

- [[Resource Links.md|Resource Links]]
- [[00-Meta/DEEP-CONTENT-STATUS.md|DEEP-CONTENT-STATUS]]
- [[00-Meta/MOCs/Physics MOC.md|Physics MOC]]
- [[Animations/README.md|README]]
- [[Animations/ALL-EXERCISES-COVERED.md|ALL-EXERCISES-COVERED]]
- [[Animations/ANIMATION_SPEC.md|ANIMATION_SPEC]]
- [[Resource Links.md|Resource Links]]
- [[VAULT-COMPLETION-REPORT.md|VAULT-COMPLETION-REPORT]]
- [[ANIMATION-SYSTEM-COMPLETE.md|ANIMATION-SYSTEM-COMPLETE]]
- [[Animations/ALL-EXERCISES-COVERED.md|ALL-EXERCISES-COVERED]]


> [!related] 🔗 Related Notes
> 
> - [[QUICK-REFERENCE.md|QUICK-REFERENCE]]
> - [[Resource Links.md|Resource Links]]
> - [[ANIMATION-SYSTEM-COMPLETE.md|ANIMATION-SYSTEM-COMPLETE]]
> - [[QUICK-REFERENCE.md|QUICK-REFERENCE]]
> - [[ANIMATION-SYSTEM-COMPLETE.md|ANIMATION-SYSTEM-COMPLETE]]
> - [[Animations/ALL-EXERCISES-COVERED.md|ALL-EXERCISES-COVERED]]
> - [[00-Meta/DEEP-CONTENT-STATUS.md|DEEP-CONTENT-STATUS]]
> - [[00-Meta/MOCs/Chemistry MOC.md|Chemistry MOC]]
> - [[01-Concepts/Math/Complex-Numbers/Complex Numbers - Operations.md|Complex Numbers - Operations]]
> - [[Animations/ANIMATION_SPEC.md|ANIMATION_SPEC]]
