---
date: {{date:YYYY-MM-DD}}
tags: meta, guide, quick-start
---

# 🚀 Quick Start: Content Improvement

**Date:** {{date:YYYY-MM-DD HH:mm}}

## Start Here

### Option 1: Fix OCR Content (Recommended First)

**Time:** 30 minutes
**Impact:** High

1. **Open** `05-Extracted/INDEX.md`
2. **Pick** 5 notes with formatting issues
3. **Fix** each note:
   - Add frontmatter: `---\ntags: [extracted, subject]\n---`
   - Remove form feed characters (Ctrl+H, find `^L`, replace with empty)
   - Add source information
4. **Link** to relevant concept notes

**Example fix:**
```markdown
---
tags: [extracted, math, matrices]
source: Cours matrices 7C E.P ISLAH ERRAID 2025-2026.pdf
extracted: 2026-03-08
---

# Cours matrices 7C E.P ISLAH ERRAID 2025-2026

← Back to [[Matrices MOC]]

## Content

[Cleaned content here]
```

### Option 2: Standardize Concept Notes

**Time:** 1 hour
**Impact:** High

1. **Open** `01-Concepts/` folder
2. **Pick** 10 concept notes
3. **Check** each note has:
   - ✅ Frontmatter with tags, status, difficulty
   - ✅ Summary box with metadata
   - ✅ Backlinks to MOC
   - ✅ Related notes section
4. **Fix** missing elements

**Template to use:**
```markdown
---
tags: [math, complex-numbers, basics]
status: active
difficulty: medium
---

# Complex Numbers - Basics

← Back to [[Complex Numbers MOC]]

## Summary

| Property | Value |
|----------|-------|
| Difficulty | Medium |
| Formulas | 7 |
| Concepts | 1 |
| Related Notes | 10 |

## Content

[Main content]

## Related Notes
- [[Complex Numbers - Operations]]
- [[Complex Numbers - Conjugates]]
```

### Option 3: Add Practice Solutions

**Time:** 1 hour
**Impact:** Medium

1. **Open** `02-Practice/` folder
2. **Pick** 5 practice notes
3. **Add** solution keys:
   - Show step-by-step work
   - Explain key concepts
   - Link to relevant theory notes
4. **Test** self-study flow

**Example solution format:**
```markdown
## Solutions

### Problem 1: $(3 + 2i) + (1 + 4i)$

**Step 1:** Group real and imaginary parts
- Real: $3 + 1 = 4$
- Imaginary: $2i + 4i = 6i$

**Step 2:** Combine
- Result: $4 + 6i$

**Key Concept:** [[Complex Numbers - Operations]]
```

## Daily Workflow

### Morning (5 minutes)
1. Open `00-Meta/Dashboard.md`
2. Check today's tasks
3. Review progress

### Study Session (variable)
1. Create daily note using template
2. Add study sessions
3. Track progress

### Evening (10 minutes)
1. Update daily note
2. Add reflections
3. Plan tomorrow

## Weekly Review (Sunday, 30 minutes)

1. **Check Dashboard**
   - Review statistics
   - Identify gaps

2. **Clean Extracted Content**
   - Fix 5-10 extracted notes
   - Add frontmatter

3. **Standardize Notes**
   - Review 10 concept notes
   - Ensure consistency

4. **Update MOCs**
   - Add new links
   - Review coverage

## Tools & Shortcuts

### Obsidian Commands
- `Ctrl+T` - Insert template
- `Ctrl+N` - New note
- `Ctrl+P` - Command palette
- `Ctrl+Shift+F` - Search (Omnisearch)

### Quick Actions
- **New Daily Note:** `06-Daily/{{date:YYYY-MM-DD}}`
- **Dashboard:** `00-Meta/Dashboard.md`
- **Index:** `00-Meta/INDEX.md`
- **Templates:** `08-Templates/`

### Keyboard Shortcuts
- `[[` - Link to note
- `#` - Add tag
- `>` - Callout
- `$$` - Math block

## Progress Tracking

### Daily
- [ ] Created daily note
- [ ] Added study sessions
- [ ] Updated tasks

### Weekly
- [ ] Fixed 5 extracted notes
- [ ] Standardized 10 concept notes
- [ ] Added solutions to 5 practice notes

### Monthly
- [ ] Complete OCR cleanup
- [ ] All notes standardized
- [ ] All practice notes have solutions

## Common Issues & Fixes

### Issue: Broken Links
**Fix:** Use `Ctrl+Click` to follow links, fix if broken

### Issue: Missing Frontmatter
**Fix:** Add `---` at top, add tags and status

### Issue: Formatting Problems
**Fix:** Use `Ctrl+H` to find/replace formatting issues

### Issue: Unclear Notes
**Fix:** Add summary box, link to related notes

## Success Indicators

✅ **You're making progress when:**
- All extracted notes have frontmatter
- All concept notes link to MOCs
- Practice notes have solutions
- Dashboard shows accurate stats
- Daily notes are consistently created

## Next Steps

1. **Today:** Fix 5 extracted notes
2. **This Week:** Standardize 20 concept notes
3. **This Month:** Complete content cleanup

---

*Start small, stay consistent! 🎯*