# Mobile SuperApp Kit — Agent Rules

## Navigation Rules

### PRD Templates (with traceability)
ALWAYS open and follow `{kit_path}/artifacts/PRD-MINIAPP/template.md` WHEN creating MiniApp-level PRD

ALWAYS open and follow `{kit_path}/artifacts/PRD-EPIC/template.md` WHEN creating Epic-level PRD

### DESIGN Templates
ALWAYS open and follow `{kit_path}/artifacts/DESIGN-PLATFORM/template.md` WHEN creating Platform-level DESIGN

ALWAYS open and follow `{kit_path}/artifacts/DESIGN-MINIAPP/template.md` WHEN creating MiniApp-level DESIGN

ALWAYS open and follow `{kit_path}/artifacts/DESIGN-EPIC/template.md` WHEN creating Epic-level DESIGN (screen, capability, flow)

### DECOMPOSITION Templates
ALWAYS open and follow `{kit_path}/artifacts/DECOMPOSITION-PLATFORM/template.md` WHEN creating Platform DECOMPOSITION

ALWAYS open and follow `{kit_path}/artifacts/DECOMPOSITION-MINIAPP/template.md` WHEN creating MiniApp DECOMPOSITION

ALWAYS open and follow `{kit_path}/artifacts/DECOMPOSITION-EPIC/template.md` WHEN creating Epic DECOMPOSITION

### FEATURE Templates
ALWAYS open and follow `{kit_path}/artifacts/FEATURE-MOBILE/template.md` WHEN creating mobile FEATURE

### IMPL Templates
ALWAYS open and follow `{kit_path}/artifacts/IMPL-KMP/template.md` WHEN creating KMP implementation reference

ALWAYS open and follow `{kit_path}/artifacts/IMPL-ANDROID/template.md` WHEN creating Android implementation reference

ALWAYS open and follow `{kit_path}/artifacts/IMPL-IOS/template.md` WHEN creating iOS implementation reference

### Validation
ALWAYS open and follow `{kit_path}/constraints.toml` WHEN validating mobile-superapp artifacts

## Level Detection

WHEN artifact path matches `architecture/` → Platform level (L0)
WHEN artifact path matches `miniapps/{miniapp}/` (direct children) → MiniApp level (L1)
WHEN artifact path matches `miniapps/{miniapp}/screens/{screen}/` → Epic level (L2, screen)
WHEN artifact path matches `miniapps/{miniapp}/capabilities/{capability}/` → Epic level (L2, capability)
WHEN artifact path matches `miniapps/{miniapp}/flows/{flow}/` → Epic level (L2, flow)
WHEN artifact path matches `miniapps/{miniapp}/*/{epic}/features/{feature}/` → Feature level (L3)

## Template Selection

| Level | PRD | DESIGN | DECOMPOSITION | FEATURE |
|-------|-----|--------|---------------|---------|
| L0: Platform | SDLC PRD | DESIGN-PLATFORM | DECOMPOSITION-PLATFORM | — |
| L1: MiniApp | **PRD-MINIAPP** | DESIGN-MINIAPP | DECOMPOSITION-MINIAPP | — |
| L2: Epic | **PRD-EPIC** | DESIGN-EPIC | DECOMPOSITION-EPIC | — |
| L3: Feature | — | — | — | FEATURE-MOBILE |

## Traceability Rules

### FR Cascade Requirements

When creating MiniApp PRD:
1. MUST include "Traces To Platform" table
2. Each MiniApp FR SHOULD reference parent Platform FR
3. FRs without parent must be tagged `miniapp-specific`

When creating Epic PRD:
1. MUST include "Traces To Parent Requirements" table
2. Each Epic FR SHOULD reference parent MiniApp FR
3. FRs without parent must be tagged `epic-specific`

When creating FEATURE:
1. MUST include "Traces To" section with Epic FR references
2. Each DOD SHOULD trace back to Epic FR

### Validation Commands

```bash
# Validate FR traceability cascade
cfs validate --check=fr-cascade

# Check coverage of Platform FRs → MiniApp FRs
cfs validate --check=platform-fr-coverage

# Check coverage of MiniApp FRs → Epic FRs  
cfs validate --check=miniapp-fr-coverage

# Check Feature implementation coverage
cfs validate --check=feature-impl-coverage
```
