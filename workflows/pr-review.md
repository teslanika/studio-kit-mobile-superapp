# Mobile PR Review Workflow

**Kit**: mobile-superapp  
**Trigger**: When reviewing PRs in mobile SuperApp projects

## Overview

This workflow guides AI-assisted PR reviews for mobile SuperApp codebases, ensuring code quality, traceability, and adherence to architectural patterns.

---

## Prerequisites

- [ ] Load `codebase/rules.md` for implementation rules
- [ ] Load `codebase/checklist.md` for review criteria
- [ ] Identify affected modules (KMP, Android, iOS)
- [ ] Load relevant DESIGN and FEATURE documents

---

## Review Steps

### Step 1: Understand PR Context

1. Read PR description
2. Identify:
   - Feature being implemented
   - Affected MiniApps
   - Platforms changed (KMP, Android, iOS)
3. Load related documentation:
   - FEATURE.md for the feature
   - DESIGN.md for the epic/miniapp
   - IMPL.md for existing implementations

### Step 2: Traceability Check

For each new/modified class:

1. **Check @cpt-impl markers**
   - [ ] Marker present
   - [ ] ID format correct: `cpt-{platform}-{module}-{type}-{slug}`
   - [ ] Referenced design ID exists

2. **Check IMPL.md updates**
   - [ ] New implementations added to traceability table
   - [ ] Code file paths correct

3. **Run validation**
   ```bash
   cfs validate --artifact {module-path}
   ```

### Step 3: Architecture Review

#### KMP Code

- [ ] State immutability (data class, no var)
- [ ] Intent pattern (sealed class)
- [ ] Effect pattern (sealed class)
- [ ] UseCase single responsibility
- [ ] Repository interface in domain/

#### Android Code

- [ ] Compose best practices
- [ ] collectAsStateWithLifecycle()
- [ ] All states handled
- [ ] Navigation correct
- [ ] Hilt DI setup

#### iOS Code

- [ ] SwiftUI patterns
- [ ] KMP ViewModel wrapper correct
- [ ] StateFlow subscription
- [ ] All states handled

### Step 4: Code Quality Check

Apply `codebase/checklist.md` items:

- [ ] Error handling complete
- [ ] No blocking calls on main thread
- [ ] Tests included
- [ ] No hardcoded strings
- [ ] Accessibility considered

### Step 5: Generate Review Report

```markdown
## PR Review Report

**PR**: #{number} - {title}
**Reviewer**: AI (mobile-superapp kit)
**Date**: {date}

### Summary
{1-2 sentence summary of changes}

### Traceability
| Status | Check |
|--------|-------|
| ✅/❌ | @cpt-impl markers present |
| ✅/❌ | IMPL.md updated |
| ✅/❌ | cfs validate passes |

### Architecture Compliance
| Platform | Status | Notes |
|----------|--------|-------|
| KMP | ✅/❌ | {notes} |
| Android | ✅/❌ | {notes} |
| iOS | ✅/❌ | {notes} |

### Code Quality
| Category | Issues |
|----------|--------|
| Error Handling | {count} |
| Testing | {count} |
| Performance | {count} |
| Security | {count} |

### Issues

#### Critical
{list or "None"}

#### High
{list or "None"}

#### Medium
{list or "None"}

### Recommendation
- [ ] **APPROVE** - Ready to merge
- [ ] **APPROVE WITH COMMENTS** - Minor issues, can merge
- [ ] **REQUEST CHANGES** - Must fix before merge
- [ ] **NEEDS DISCUSSION** - Architectural questions

### Action Items
1. {action item}
2. {action item}
```

---

## Review Checklist Quick Reference

### Must Check
- [ ] @cpt-impl markers
- [ ] State immutability
- [ ] Error handling
- [ ] All UI states covered

### Should Check
- [ ] Test coverage
- [ ] Performance implications
- [ ] Accessibility
- [ ] Documentation updates

### Red Flags
- Mutable state properties
- Force unwrapping (iOS)
- Blocking main thread
- Missing error handling
- Hardcoded credentials
