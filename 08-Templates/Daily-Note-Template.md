---
date: {{date}}
tags: daily-note
status: planning
---

# {{date}}

## 📅 Daily Overview

**Day of Week:** {{date:dddd}}
**Week Number:** {{date:WW}}
**Month:** {{date:MMMM}}

## ✅ Tasks for Today

```dataview
TASK
WHERE completed = false
AND due = date({{date:YYYY-MM-DD}})
SORT priority DESC
```

## 📝 Quick Notes

- 

## 📚 Study Sessions

### Session 1
**Time:** 
**Topic:** 
**Duration:** 
**Rating:** 

### Session 2
**Time:** 
**Topic:** 
**Duration:** 
**Rating:** 

## 🎯 Goals

- [ ] 
- [ ] 
- [ ] 

## 📊 Progress Tracking

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  status AS "Status",
  date AS "Date"
FROM "01-Concepts"
WHERE date >= date({{date:YYYY-MM-DD}}) - dur(7 days)
SORT date DESC
LIMIT 10
```

## 🔗 Links

### Recent Notes
```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  file.mtime AS "Modified"
FROM ""
WHERE file.mtime >= date({{date:YYYY-MM-DD}}) - dur(1 day)
SORT file.mtime DESC
LIMIT 5
```

### Backlinks
```dataview
LIST
FROM [[{{date:YYYY-MM-DD}}]]
```

## 📅 Schedule

| Time | Activity | Status |
|------|----------|--------|
| 08:00 | Morning Review | ⬜ |
| 09:00 | Study Session 1 | ⬜ |
| 11:00 | Break | ⬜ |
| 11:30 | Study Session 2 | ⬜ |
| 13:00 | Lunch | ⬜ |
| 14:00 | Study Session 3 | ⬜ |
| 16:00 | Review & Plan | ⬜ |
| 17:00 | Free Time | ⬜ |

## 💡 Insights & Reflections

### What went well today?
- 

### What could be improved?
- 

### Key learnings:
- 

### Tomorrow's priorities:
1. 
2. 
3. 

---

*Daily Note Template - Created {{date:YYYY-MM-DD}}*