# Mobile Code Review Checklist

**Kit**: mobile-superapp  
**Scope**: KMP, Android (Compose), iOS (SwiftUI)

This checklist provides code review criteria for mobile SuperApp implementations.

---

## Table of Contents

1. [General Code Quality](#general-code-quality)
2. [KMP Shared Code](#kmp-shared-code)
3. [Android Code](#android-code)
4. [iOS Code](#ios-code)
5. [Traceability](#traceability)
6. [Performance](#performance)
7. [Security](#security)

---

## General Code Quality

### CODE-001: Traceability Markers

**Priority**: CRITICAL

- [ ] All new code has `@cpt-impl` markers
- [ ] Markers reference valid design IDs
- [ ] IMPL.md updated with new mappings

### CODE-002: Code Organization

**Priority**: HIGH

- [ ] Code follows directory structure from codebase/rules.md
- [ ] Domain logic in domain/ folder
- [ ] Data logic in data/ folder
- [ ] Presentation logic in presentation/ folder

### CODE-003: Error Handling

**Priority**: HIGH

- [ ] All API calls wrapped in try-catch
- [ ] Errors mapped to domain error types
- [ ] User-facing errors have meaningful messages

### CODE-004: Testing

**Priority**: HIGH

- [ ] Unit tests for use cases
- [ ] Unit tests for ViewModels
- [ ] UI tests for critical flows
- [ ] Test coverage meets threshold (80%+)

---

## KMP Shared Code

### KMP-001: State Immutability

**Priority**: CRITICAL

- [ ] State classes are `data class`
- [ ] No mutable properties in State
- [ ] Collections are immutable (List, not MutableList)

### KMP-002: Intent Pattern

**Priority**: HIGH

- [ ] All user actions represented as Intent
- [ ] Intent classes are `sealed class`
- [ ] No side effects in Intent processing

### KMP-003: Effect Pattern

**Priority**: HIGH

- [ ] Side effects are Effect class instances
- [ ] Effects are one-shot (navigation, toast)
- [ ] No business logic in Effect handling

### KMP-004: Use Case Design

**Priority**: HIGH

- [ ] Single responsibility per UseCase
- [ ] Input validation at entry point
- [ ] Returns `Result<T>` for fallible operations
- [ ] No direct UI dependencies

### KMP-005: Repository Pattern

**Priority**: MEDIUM

- [ ] Interface in domain/
- [ ] Implementation in data/
- [ ] Caching strategy documented
- [ ] Offline support where required

---

## Android Code

### ANDROID-001: Compose Best Practices

**Priority**: HIGH

- [ ] State hoisting applied
- [ ] `collectAsStateWithLifecycle()` used
- [ ] Side effects in LaunchedEffect
- [ ] No blocking calls in composables

### ANDROID-002: State Handling

**Priority**: CRITICAL

- [ ] All states handled (Loading, Content, Error, Empty)
- [ ] Loading state shows appropriate UI
- [ ] Error state has retry action
- [ ] Empty state has call-to-action

### ANDROID-003: Navigation

**Priority**: HIGH

- [ ] Routes defined as constants
- [ ] Navigation handles back stack
- [ ] Deep links work correctly
- [ ] Arguments passed via NavBackStackEntry

### ANDROID-004: Lifecycle Awareness

**Priority**: HIGH

- [ ] ViewModel survives configuration changes
- [ ] Effects handled in lifecycle-aware manner
- [ ] No memory leaks from observers

### ANDROID-005: Accessibility

**Priority**: MEDIUM

- [ ] contentDescription on images
- [ ] Semantic properties for screen readers
- [ ] Minimum touch target size (48dp)

---

## iOS Code

### IOS-001: SwiftUI Best Practices

**Priority**: HIGH

- [ ] `@StateObject` for ViewModel wrapper
- [ ] Proper use of `@ViewBuilder`
- [ ] Task cancellation handled
- [ ] No force unwrapping

### IOS-002: KMP Integration

**Priority**: CRITICAL

- [ ] ViewModel wrapper uses ObservableObject
- [ ] StateFlow subscription correct
- [ ] Intent forwarding works
- [ ] Memory management verified

### IOS-003: State Handling

**Priority**: CRITICAL

- [ ] All states handled
- [ ] Switch exhaustive
- [ ] Empty states meaningful
- [ ] Error states have recovery

### IOS-004: Navigation

**Priority**: HIGH

- [ ] Coordinator pattern followed (if used)
- [ ] Deep links handled
- [ ] Navigation state preserved

### IOS-005: Accessibility

**Priority**: MEDIUM

- [ ] VoiceOver labels
- [ ] Dynamic Type support
- [ ] Minimum touch targets

---

## Traceability

### TRACE-001: Documentation Links

**Priority**: HIGH

- [ ] Every new class has @cpt-impl marker
- [ ] IMPL.md file exists and is current
- [ ] Design components all mapped

### TRACE-002: Coverage

**Priority**: MEDIUM

- [ ] Run `cfs validate` passes
- [ ] Coverage report reviewed
- [ ] Missing implementations documented

---

## Performance

### PERF-001: Network

**Priority**: MEDIUM

- [ ] Requests are minimal
- [ ] Responses cached appropriately
- [ ] Retry logic implemented
- [ ] Timeout configured

### PERF-002: UI

**Priority**: MEDIUM

- [ ] No main thread blocking
- [ ] Lists use lazy loading
- [ ] Images loaded asynchronously
- [ ] Animations smooth (60fps)

### PERF-003: Memory

**Priority**: MEDIUM

- [ ] No memory leaks
- [ ] Large objects released
- [ ] Image caching appropriate

---

## Security

### SEC-001: Data Protection

**Priority**: CRITICAL

- [ ] Sensitive data in secure storage
- [ ] No secrets in code
- [ ] API keys in secure config

### SEC-002: Authentication

**Priority**: CRITICAL

- [ ] Tokens stored securely
- [ ] Token refresh handled
- [ ] Session expiry handled

### SEC-003: Input Validation

**Priority**: HIGH

- [ ] User input validated
- [ ] API responses validated
- [ ] No injection vulnerabilities

---

## PR Review Summary Template

```markdown
## Code Review Summary

**PR**: #{number}
**Module**: {kmp/android/ios}/{module}

### Traceability
- [ ] @cpt-impl markers present
- [ ] IMPL.md updated

### Code Quality
- [ ] Follows architecture patterns
- [ ] Error handling complete
- [ ] Tests included

### Platform-Specific
- [ ] {Platform checklist items}

### Issues Found
| ID | Severity | Description | Line |
|----|----------|-------------|------|
| | | | |

### Recommendation
- [ ] APPROVE
- [ ] REQUEST CHANGES
- [ ] NEEDS DISCUSSION
```
