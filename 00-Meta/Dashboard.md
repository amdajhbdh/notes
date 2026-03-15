---
tags: dashboard, meta
updated: {{date:YYYY-MM-DD}}
---

# 📊 Vault Dashboard

> **Last Updated:** {{date:YYYY-MM-DD HH:mm}}

## 📈 Overview

```dataviewjs
const pages = dv.pages('');
const totalNotes = pages.length;
const concepts = pages.where(p => p.file.folder === "01-Concepts").length;
const practice = pages.where(p => p.file.folder === "02-Practice").length;
const daily = pages.where(p => p.file.folder === "06-Daily").length;

dv.paragraph(`**Total Notes:** ${totalNotes}`);
dv.paragraph(`**Concepts:** ${concepts}`);
dv.paragraph(`**Practice:** ${practice}`);
dv.paragraph(`**Daily Notes:** ${daily}`);
```

## 📅 Today's Summary

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  status AS "Status",
  time AS "Time"
FROM "06-Daily"
WHERE file.name = this.file.name
```

## 📝 Recent Notes

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  file.folder AS "Folder",
  file.mtime AS "Modified"
FROM ""
SORT file.mtime DESC
LIMIT 10
```

## 📚 Concepts Overview

```dataview
TABLE WITHOUT ID
  file.link AS "Concept",
  subject AS "Subject",
  status AS "Status"
FROM "01-Concepts"
SORT file.name ASC
```

## ✅ Tasks Overview

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  completed AS "Completed",
  due AS "Due Date",
  priority AS "Priority"
FROM ""
WHERE completed = false
AND due != null
SORT due ASC
LIMIT 10
```

## 📊 Progress by Subject

```dataviewjs
const subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "French"];
const subjectData = subjects.map(subject => {
  const notes = dv.pages(`"${subject}"`);
  return {
    subject: subject,
    count: notes.length,
    recent: notes.sort(p => p.file.mtime, 'desc').limit(1)[0]?.file.link || "None"
  };
});

dv.table(["Subject", "Notes", "Recent"], subjectData.map(d => [d.subject, d.count, d.recent]));
```

## 🔗 Quick Links

### Daily Notes
- [[{{date:YYYY-MM-DD}}]] - Today
- [[{{date:YYYY-MM-DD - 1}}]] - Yesterday
- [[{{date:YYYY-MM-DD - 7}}]] - Last Week

### Important Notes
- [[START-HERE]] - Getting Started
- [[QUICK-START]] - Quick Start Guide
- [[SYSTEM-STATUS]] - System Status

### Resources
- [[00-Meta/README]] - Vault Documentation
- [[00-Meta/INDEX]] - Master Index

## 📅 Calendar View

```calendar
{{date:YYYY-MM}}
```

## 🎯 Goals & Progress

### Weekly Goals
- [ ] Complete 5 practice sessions
- [ ] Review all concepts from last week
- [ ] Update daily notes consistently

### Monthly Goals
- [ ] Complete all practice exercises
- [ ] Master key concepts
- [ ] Prepare for exams

---

*Dashboard - Auto-generated*