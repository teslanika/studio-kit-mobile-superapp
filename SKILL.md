---
name: mobile-superapp
description: "Mobile SuperApp documentation kit with 4-level hierarchy: Platform → MiniApp → Epic → Feature, with cascading requirement traceability"
---

# Constructor Studio Skill — Kit `mobile-superapp`

## Overview

This kit provides specialized templates for mobile SuperApp development with:
- **4-Level PRD hierarchy** (Platform → MiniApp → Epic → Feature)
- **Level-specific DESIGN templates** (Platform, MiniApp, Epic)
- **Cascading DECOMPOSITION** (Platform → MiniApps, MiniApp → Epics, Epic → Features)
- **Mobile-specific FEATURE template** with KMP/Android/iOS sections
- **Platform-specific IMPL templates** (KMP, Android, iOS)

## Artifact Types

### PRD-MINIAPP
MiniApp-level PRD that refines Platform requirements.

**Use when**: Creating requirements for a self-contained feature module (e.g., Student MiniApp, Proctor MiniApp).

**Contains**:
- Traces to Platform PRD
- MiniApp-specific functional requirements
- MiniApp-level NFRs (extending Platform NFRs)
- Use cases
- Platform dependencies

### PRD-EPIC
Epic-level PRD that details MiniApp requirements for a specific screen/flow/capability.

**Use when**: Creating requirements for a screen, user flow, or cross-cutting capability.

**Contains**:
- Traces to MiniApp PRD
- Screen states and error handling
- UI/UX requirements
- Data requirements
- API contracts

### DESIGN-PLATFORM
Platform-level architecture design for the entire SuperApp.

**Use when**: Defining overall platform architecture, shared kernel, MiniApp container model.

**Contains**:
- Platform layers (Presentation, Application, Domain, Infrastructure)
- Cross-platform strategy (Native vs WebView)
- KMP SDK scope
- MiniApp container model
- Shared kernel components (Auth, Storage, Network, Notifications)
- External integrations

### DESIGN-MINIAPP
MiniApp-level architecture design.

**Use when**: Designing a specific MiniApp's module structure and internal architecture.

**Contains**:
- Module structure (KMP, Android, iOS)
- Navigation architecture
- State management (MVI)
- Domain model
- API layer
- Kernel integration

### DESIGN-EPIC
Epic-level (screen/flow/capability) technical design.

**Use when**: Designing a specific screen or feature within a MiniApp.

**Contains**:
- Component architecture
- Screen/widget components
- State management
- Data flow (UseCase, Repository)
- Platform-specific considerations
- Error handling

### DECOMPOSITION-PLATFORM
Decomposes Platform DESIGN into MiniApps.

**Use when**: Breaking down the platform into deployable MiniApp modules.

### DECOMPOSITION-MINIAPP
Decomposes MiniApp DESIGN into Epics (screens, capabilities, flows).

**Use when**: Breaking down a MiniApp into implementable epics.

### DECOMPOSITION-EPIC
Decomposes Epic DESIGN into Features.

**Use when**: Breaking down an epic into discrete, implementable features.

### FEATURE-MOBILE
Mobile-specific feature design with CDSL flows.

**Use when**: Specifying a discrete piece of functionality ready for implementation.

**Contains**:
- Actor flows (CDSL)
- Platform implementation sections (KMP, Android, iOS, WebView)
- State machines (CDSL)
- Definitions of Done
- Platform-specific acceptance criteria

### IMPL-KMP / IMPL-ANDROID / IMPL-IOS
Implementation reference documents linking code to product docs.

**Use when**: Creating traceability from code back to documentation.

## Commands

### Validation
```bash
cfs validate --artifact <path>
cfs validate --check=fr-cascade
cfs validate --check=platform-fr-coverage
cfs validate --check=feature-impl-coverage
```

### Language Check (run after every artifact generation)

```bash
# Check entire architecture tree (default)
python3 .cf-studio/config/kits/mobile-superapp/scripts/check-language.py

# Check a specific file or directory
python3 .cf-studio/config/kits/mobile-superapp/scripts/check-language.py architecture/miniapps/student/

# Quiet mode — violations only, no summary header
python3 .cf-studio/config/kits/mobile-superapp/scripts/check-language.py -q architecture/
```

Script: `{kit_path}/scripts/check-language.py`

**`allowed_languages` config** (top of the script):
```python
allowed_languages: list[str] = [
    "en",   # English — Latin script only (current policy)
    # "ru", # Uncomment to allow Russian / Cyrillic
    # "tr", # Turkish — already covered by Latin, no change needed
    # "ar", # Arabic
    # "zh", # Chinese (CJK)
]
```

Exit codes: `0` = all clean, `1` = violations found.

### ID Operations
```bash
cfs list-ids --kind feature
cfs where-defined --id <id>
cfs where-used --id <id>
```

## Workflows

### Generate Platform Architecture
1. Create/update `architecture/PRD.md` (use SDLC PRD)
2. Create `architecture/DESIGN.md` using DESIGN-PLATFORM template
3. Create `architecture/DECOMPOSITION.md` listing MiniApps
4. Create `architecture/adr/` for platform decisions
5. **Run language check**: `python3 {kit_path}/scripts/check-language.py architecture/`

### Generate MiniApp
1. Create `miniapps/{miniapp}/PRD.md` using PRD-MINIAPP template
2. Create `miniapps/{miniapp}/DESIGN.md` using DESIGN-MINIAPP template
3. Create `miniapps/{miniapp}/DECOMPOSITION.md` listing Epics
4. Create epics in `screens/`, `capabilities/`, `flows/`
5. **Run language check**: `python3 {kit_path}/scripts/check-language.py architecture/miniapps/{miniapp}/`

### Generate Epic
1. Create `miniapps/{miniapp}/{category}/{epic}/PRD.md` using PRD-EPIC template
2. Create `DESIGN.md` using DESIGN-EPIC template
3. Create `DECOMPOSITION.md` listing Features
4. Create features in `features/`
5. **Run language check**: `python3 {kit_path}/scripts/check-language.py architecture/miniapps/{miniapp}/{category}/{epic}/`

### Generate Feature
1. Create `features/{feature}/FEATURE.md` using FEATURE-MOBILE template
2. Create IMPL.md files in code folders:
   - `constructor-sdk/feature/{module}/IMPL.md`
   - `android-app/feature/{module}/IMPL.md`
   - `ios-app/Features/{Module}/IMPL.md`
3. **Run language check**: `python3 {kit_path}/scripts/check-language.py`

## Level Detection

| Path Pattern | Level |
|--------------|-------|
| `architecture/` | L0: Platform |
| `miniapps/{miniapp}/` (direct children) | L1: MiniApp |
| `miniapps/{miniapp}/screens/{screen}/` | L2: Epic (screen) |
| `miniapps/{miniapp}/capabilities/{capability}/` | L2: Epic (capability) |
| `miniapps/{miniapp}/flows/{flow}/` | L2: Epic (flow) |
| `miniapps/{miniapp}/*/{epic}/features/{feature}/` | L3: Feature |

## Traceability Chain

```
Platform PRD
    ↓ refined-by
Platform DESIGN + ADR
    ↓ decomposed-by
Platform DECOMPOSITION (MiniApps)
    ↓ detailed-by
MiniApp PRD
    ↓ designed-by
MiniApp DESIGN + ADR
    ↓ decomposed-by
MiniApp DECOMPOSITION (Epics)
    ↓ detailed-by
Epic PRD
    ↓ designed-by
Epic DESIGN + ADR
    ↓ decomposed-by
Epic DECOMPOSITION (Features)
    ↓ specified-by
FEATURE (CDSL)
    ↓ implemented-by
IMPL-KMP + IMPL-ANDROID + IMPL-IOS
    ↓ traces-to
Code (@cpt-impl markers)
```
