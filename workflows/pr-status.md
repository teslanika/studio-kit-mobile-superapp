# Mobile PR Status Report Workflow

**Kit**: mobile-superapp  
**Trigger**: When generating PR status reports

## Overview

This workflow generates status reports for mobile SuperApp PRs, tracking implementation progress against documentation.

---

## Prerequisites

- [ ] PR number and repository known
- [ ] Access to PR diff
- [ ] Load relevant FEATURE and DECOMPOSITION documents

---

## Report Generation Steps

### Step 1: Gather PR Information

```bash
gh pr view {number} --json title,state,author,createdAt,updatedAt,additions,deletions,changedFiles
```

### Step 2: Analyze Changes

1. List changed files by platform:
   - KMP: `constructor-sdk/feature/{module}/**`
   - Android: `android-app/feature/{module}/**`
   - iOS: `ios-app/Features/{Module}/**`

2. Map changes to documentation:
   - Which FEATURE does this implement?
   - Which DODs are addressed?
   - Which Epic is this part of?

### Step 3: Calculate Progress

For each affected FEATURE:

1. Count total DODs
2. Count DODs with implementations
3. Calculate coverage percentage

### Step 4: Generate Status Report

```markdown
# PR Status Report

## PR Information

| Field | Value |
|-------|-------|
| PR | #{number} |
| Title | {title} |
| Author | {author} |
| State | {open/merged/closed} |
| Created | {date} |
| Updated | {date} |

## Change Summary

| Metric | Value |
|--------|-------|
| Files Changed | {count} |
| Additions | +{count} |
| Deletions | -{count} |

### By Platform

| Platform | Files | Lines |
|----------|-------|-------|
| KMP | {count} | +{add}/-{del} |
| Android | {count} | +{add}/-{del} |
| iOS | {count} | +{add}/-{del} |
| Other | {count} | +{add}/-{del} |

## Feature Implementation Status

### {Feature Name}

**Feature ID**: `cpt-{hierarchy-prefix}-feature-{slug}`
**Epic**: `cpt-{hierarchy-prefix}-epic-{epic}`

#### Definitions of Done

| DOD ID | Description | Status |
|--------|-------------|--------|
| `cpt-{hierarchy-prefix}-dod-{slug}-1` | {description} | ✅ Done / 🔄 In Progress / ⏳ Not Started |
| `cpt-{hierarchy-prefix}-dod-{slug}-2` | {description} | ✅ / 🔄 / ⏳ |

**Progress**: {completed}/{total} ({percentage}%)

#### Platform Implementation

| Platform | Component | Status |
|----------|-----------|--------|
| KMP | ViewModel | ✅ / 🔄 / ⏳ |
| KMP | UseCase | ✅ / 🔄 / ⏳ |
| KMP | Repository | ✅ / 🔄 / ⏳ |
| Android | Screen | ✅ / 🔄 / ⏳ |
| Android | Widgets | ✅ / 🔄 / ⏳ |
| iOS | View | ✅ / 🔄 / ⏳ |
| iOS | Wrapper | ✅ / 🔄 / ⏳ |

## Traceability Status

| Check | Status |
|-------|--------|
| @cpt-impl markers | ✅ All present / ❌ {count} missing |
| IMPL.md files | ✅ Updated / ❌ Needs update |
| cfs validate | ✅ Pass / ❌ Fail |

## Blocking Issues

{List blocking issues or "None"}

## Next Steps

1. {next step}
2. {next step}

## Timeline

| Milestone | Date | Status |
|-----------|------|--------|
| PR Created | {date} | ✅ |
| Code Review | {date} | ✅ / 🔄 / ⏳ |
| Tests Passing | {date} | ✅ / 🔄 / ⏳ |
| Approved | {date} | ✅ / 🔄 / ⏳ |
| Merged | {date} | ✅ / 🔄 / ⏳ |
```

---

## Status Icons

| Icon | Meaning |
|------|---------|
| ✅ | Complete |
| 🔄 | In Progress |
| ⏳ | Not Started |
| ❌ | Failed/Blocked |
| ⚠️ | Needs Attention |
