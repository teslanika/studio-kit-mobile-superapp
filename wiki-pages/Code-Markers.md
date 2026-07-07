# Code Markers

Code markers provide traceability from code back to design documents.

## Marker Types

### Simple Marker: `@cpt-impl`

Shows that a file/class implements a design element.

```kotlin
// @cpt-impl cpt-learn-course-list-viewmodel-kmp
class CourseListViewModel { ... }
```

**Use when:**
- Marking file-level implementation
- DOCS-ONLY traceability mode
- Quick reference needed

### Scope Marker: `@cpt-{kind}:{id}:p{N}`

Shows that a function/class implements a specific flow/algo/state.

```kotlin
// @cpt-flow:cpt-learn-flow-course-list-load:p1
fun loadCourses() { ... }
```

**Use when:**
- Marking function-level implementation
- Need to track implementation phases

### Block Markers: `@cpt-begin`/`@cpt-end`

Wrap specific lines that implement a CDSL instruction.

```kotlin
// @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-1
viewModelScope.launch {
    _state.update { it.copy(isLoading = true) }
// @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-1
```

**Use when:**
- FULL traceability mode
- Need line-level traceability
- Multiple CDSL instructions in one function

## Traceability Modes

### DOCS-ONLY Mode

Simplified markers, no block markers required.

```kotlin
// @cpt-impl cpt-learn-course-list-viewmodel-kmp
class CourseListViewModel(
    private val loadCoursesUseCase: LoadCoursesUseCase
) : ViewModel() {
    
    fun loadCourses() {
        // Implementation without block markers
    }
}
```

### FULL Mode

Complete traceability with block markers for each CDSL instruction.

```kotlin
// @cpt-flow:cpt-learn-flow-course-list-load:p1
fun loadCourses() {
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-1
    viewModelScope.launch {
        _state.update { it.copy(isLoading = true) }
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-1
    
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-2
        val result = loadCoursesUseCase()
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-2
    
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-3
        _state.update { it.copy(courses = result, isLoading = false) }
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-3
    }
}
```

## Platform-Specific Patterns

### KMP (Kotlin)

```kotlin
// @cpt-impl cpt-kmp-learn-viewmodel-courselist
class CourseListViewModel { ... }

// @cpt-impl cpt-kmp-learn-usecase-loadcourses
class LoadCoursesUseCase { ... }

// @cpt-impl cpt-kmp-learn-repository-course
class CourseRepositoryImpl { ... }
```

### Android (Compose)

```kotlin
// @cpt-impl cpt-android-learn-screen-courselist
@Composable
fun CourseListScreen() { ... }

// @cpt-impl cpt-android-learn-component-coursecard
@Composable
fun CourseCard() { ... }
```

### iOS (SwiftUI)

```swift
// @cpt-impl cpt-ios-learn-view-courselist
struct CourseListView: View { ... }

// @cpt-impl cpt-ios-learn-wrapper-courselist
class CourseListViewModelWrapper { ... }
```

## Checkbox Cascade

Block markers trigger checkbox updates in FEATURE-MOBILE:

| Code State | FEATURE-MOBILE State |
|------------|---------------------|
| All `inst-*` markers for a flow exist | Mark flow `[x]` |
| All flows for a feature marked `[x]` | Mark feature as IMPLEMENTED |

Example cascade:

```
Code: @cpt-begin:...:inst-kmp-1 exists
Code: @cpt-begin:...:inst-kmp-2 exists
Code: @cpt-begin:...:inst-kmp-3 exists
    ↓
FEATURE: flow cpt-learn-flow-course-list-load [x]
    ↓
DECOMPOSITION-EPIC: feature course-list [x]
    ↓
DECOMPOSITION-MINIAPP: epic course-catalog [x]
```

## Validation

```bash
# Check all markers
cfs validate code

# Check specific feature
cfs validate code for course-list

# Find orphaned markers
cfs validate code orphans

# Check coverage
cfs validate code coverage
```

## Best Practices

1. **Granularity**: Each `@cpt-begin/@cpt-end` wraps the smallest code fragment for its CDSL instruction
2. **Placement**: Place markers as close to implementing code as possible
3. **No empty blocks**: Every block must contain actual implementation
4. **Matched pairs**: Every `@cpt-begin` must have matching `@cpt-end`
5. **Valid IDs**: Markers must reference IDs that exist in design documents
