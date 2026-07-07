#!/usr/bin/env python3
"""
check-language.py — Language validation for Constructor Studio artifacts.

Scans Markdown documents for characters outside the allowed language set.
Run after any artifact generation to catch non-English content early.

Usage:
    python check-language.py [path ...]

    path  - file or directory to scan (default: architecture/)
    -q    - quiet mode (only show violations, no summary header)
    --fix - auto-translate is not supported; use this flag to list files only

Exit codes:
    0 — all documents pass
    1 — one or more violations found
"""

import re
import sys
import unicodedata
from pathlib import Path

# ─────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────

# Languages allowed in artifact text.
# Current policy: English only.
# To allow additional scripts in the future, add to this list:
#   "ru" — Russian (Cyrillic)
#   "ar" — Arabic
#   "tr" — Turkish (mostly covered by Latin; no change needed)
#   "zh" — Chinese (CJK)
#   "ko" — Korean
#   "ja" — Japanese
#   "he" — Hebrew
#   "hi" — Devanagari / Hindi
allowed_languages: list[str] = [
    "en",  # English — Latin script only
]

# File extensions to scan.
SCAN_EXTENSIONS: set[str] = {".md"}

# Default scan path relative to this script's location (kit root → project root).
# Resolved at runtime; override by passing a path argument.
DEFAULT_SCAN_PATHS: list[str] = ["architecture"]

# Lines whose *entire content* matches these patterns are skipped.
# Prevents false positives inside IDs, URLs, code snippets, etc.
SKIP_LINE_PATTERNS: list[re.Pattern] = [
    re.compile(r"^\s*<!--.*-->"),          # HTML comments
    re.compile(r"^\s*\|.*`cpt-.*`"),       # traceability ID table rows
    re.compile(r"^\s*@cpt"),               # Constructor Studio provenance markers (@cpt-*)
]

# Fenced code blocks: content between ``` or ~~~ is skipped entirely.
FENCE_START = re.compile(r"^\s*(`{3,}|~{3,})")

# ─────────────────────────────────────────────────────────
# UNICODE SCRIPT RANGES
# Maps language code → list of (start, end) inclusive ranges.
# Characters within these ranges are ALLOWED when the language is enabled.
# ─────────────────────────────────────────────────────────

SCRIPT_RANGES: dict[str, list[tuple[int, int]]] = {
    # Latin (Basic + Extended-A/B + Supplement) — always allowed for punctuation/technical
    "en": [
        (0x0000, 0x007F),   # Basic Latin (ASCII)
        (0x0080, 0x00FF),   # Latin-1 Supplement
        (0x0100, 0x017F),   # Latin Extended-A
        (0x0180, 0x024F),   # Latin Extended-B
        (0x0250, 0x02AF),   # IPA Extensions
        (0x02B0, 0x02FF),   # Spacing Modifier Letters
        (0x0300, 0x036F),   # Combining Diacritical Marks
        (0x2000, 0x206F),   # General Punctuation (em dash, ellipsis, …)
        (0x2100, 0x214F),   # Letterlike Symbols (™, ©, etc.)
        (0x2190, 0x21FF),   # Arrows (→, ←, etc.)
        (0x2200, 0x22FF),   # Mathematical Operators
        (0x2500, 0x257F),   # Box Drawing (used in ASCII diagrams)
        (0x25A0, 0x25FF),   # Geometric Shapes
        (0x2600, 0x26FF),   # Miscellaneous Symbols (✓, ✗, etc.)
        (0x2700, 0x27BF),   # Dingbats (✅, ❌, etc.)
        (0xFE50, 0xFE6F),   # Small Form Variants
        (0xFF00, 0xFFEF),   # Halfwidth/Fullwidth Forms
    ],
    # Russian / Cyrillic
    "ru": [
        (0x0400, 0x04FF),   # Cyrillic
        (0x0500, 0x052F),   # Cyrillic Supplement
        (0x2DE0, 0x2DFF),   # Cyrillic Extended-A
        (0xA640, 0xA69F),   # Cyrillic Extended-B
    ],
    # Arabic
    "ar": [
        (0x0600, 0x06FF),   # Arabic
        (0x0750, 0x077F),   # Arabic Supplement
        (0xFB50, 0xFDFF),   # Arabic Presentation Forms-A
        (0xFE70, 0xFEFF),   # Arabic Presentation Forms-B
    ],
    # Chinese (CJK)
    "zh": [
        (0x4E00, 0x9FFF),   # CJK Unified Ideographs
        (0x3400, 0x4DBF),   # CJK Extension A
        (0x3000, 0x303F),   # CJK Symbols and Punctuation
    ],
    # Japanese
    "ja": [
        (0x3040, 0x309F),   # Hiragana
        (0x30A0, 0x30FF),   # Katakana
        (0x4E00, 0x9FFF),   # CJK (shared with Chinese)
        (0x3000, 0x303F),   # CJK Symbols
    ],
    # Korean
    "ko": [
        (0xAC00, 0xD7AF),   # Hangul Syllables
        (0x1100, 0x11FF),   # Hangul Jamo
        (0x3130, 0x318F),   # Hangul Compatibility Jamo
    ],
    # Hebrew
    "he": [
        (0x0590, 0x05FF),   # Hebrew
        (0xFB1D, 0xFB4F),   # Hebrew Presentation Forms
    ],
    # Devanagari (Hindi, etc.)
    "hi": [
        (0x0900, 0x097F),   # Devanagari
        (0xA8E0, 0xA8FF),   # Devanagari Extended
    ],
    # Thai
    "th": [
        (0x0E00, 0x0E7F),   # Thai
    ],
    # Georgian
    "ka": [
        (0x10A0, 0x10FF),   # Georgian
        (0x2D00, 0x2D2F),   # Georgian Supplement
    ],
    # Armenian
    "hy": [
        (0x0530, 0x058F),   # Armenian
        (0xFB13, 0xFB17),   # Armenian Ligatures
    ],
}

# ─────────────────────────────────────────────────────────
# BUILD ALLOWED RANGE SET
# ─────────────────────────────────────────────────────────

def _build_allowed_ranges(languages: list[str]) -> list[tuple[int, int]]:
    """Merge Unicode ranges for all allowed languages into a sorted list."""
    ranges: list[tuple[int, int]] = []
    for lang in languages:
        ranges.extend(SCRIPT_RANGES.get(lang, []))
    # Also always allow common symbols / emoji that are language-neutral
    common = [
        (0x1F300, 0x1F9FF),  # Emoji (common in markdown)
        (0x200B, 0x200F),    # Zero-width / directional markers
        (0xFEFF, 0xFEFF),    # BOM
    ]
    ranges.extend(common)
    return sorted(ranges, key=lambda r: r[0])


def _is_allowed(cp: int, ranges: list[tuple[int, int]]) -> bool:
    """Binary search: is code point cp within any allowed range?"""
    lo, hi = 0, len(ranges) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        start, end = ranges[mid]
        if start <= cp <= end:
            return True
        if cp < start:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


# ─────────────────────────────────────────────────────────
# SCANNING
# ─────────────────────────────────────────────────────────

class Violation:
    def __init__(self, path: Path, lineno: int, line: str, chars: list[tuple[int, str]]):
        self.path = path
        self.lineno = lineno
        self.line = line.rstrip()
        self.chars = chars  # [(code_point, character), ...]

    def script_names(self) -> str:
        names = {unicodedata.name(ch, f"U+{cp:04X}") for cp, ch in self.chars}
        # Simplify: group by script block prefix
        blocks: set[str] = set()
        for name in names:
            blocks.add(name.split(" ")[0])
        return ", ".join(sorted(blocks))

    def __str__(self) -> str:
        preview = self.line[:100] + ("…" if len(self.line) > 100 else "")
        bad_chars = "".join(ch for _, ch in self.chars[:5])
        return (
            f"  {self.path}:{self.lineno}  [{bad_chars}]  {preview}"
        )


def _scan_file(path: Path, allowed_ranges: list[tuple[int, int]]) -> list[Violation]:
    """Scan a single file and return all violations."""
    violations: list[Violation] = []
    in_fence = False

    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
        print(f"  WARNING: cannot read {path}: {e}", file=sys.stderr)
        return []

    for lineno, line in enumerate(text.splitlines(), start=1):
        # Toggle fenced code block state
        if FENCE_START.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # Skip certain structural lines to reduce noise
        if any(p.match(line) for p in SKIP_LINE_PATTERNS):
            continue

        # Check each character
        bad: list[tuple[int, str]] = []
        for ch in line:
            cp = ord(ch)
            if not _is_allowed(cp, allowed_ranges):
                bad.append((cp, ch))

        if bad:
            violations.append(Violation(path, lineno, line, bad))

    return violations


def scan(paths: list[Path], allowed_ranges: list[tuple[int, int]]) -> list[Violation]:
    """Recursively scan all .md files under given paths."""
    all_violations: list[Violation] = []
    for root in paths:
        if root.is_file():
            if root.suffix in SCAN_EXTENSIONS:
                all_violations.extend(_scan_file(root, allowed_ranges))
        elif root.is_dir():
            for file in sorted(root.rglob("*")):
                if file.suffix in SCAN_EXTENSIONS:
                    all_violations.extend(_scan_file(file, allowed_ranges))
    return all_violations


# ─────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────

def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    quiet = "-q" in sys.argv[1:]

    # Resolve scan paths
    if args:
        roots = [Path(a) for a in args]
    else:
        # Default: scan relative to project root (two levels up from this script)
        script_dir = Path(__file__).resolve().parent
        # scripts/ → mobile-superapp kit → kits/ → config/ → .cf-studio/ → project root
        project_root = script_dir.parents[4]
        roots = [project_root / p for p in DEFAULT_SCAN_PATHS]

    # Validate roots exist
    missing = [str(r) for r in roots if not r.exists()]
    if missing:
        print(f"ERROR: paths not found: {', '.join(missing)}", file=sys.stderr)
        return 1

    allowed_ranges = _build_allowed_ranges(allowed_languages)

    if not quiet:
        lang_list = ", ".join(f'"{l}"' for l in allowed_languages)
        print(f"check-language  allowed_languages=[{lang_list}]")
        print(f"scanning: {', '.join(str(r) for r in roots)}")
        print()

    violations = scan(roots, allowed_ranges)

    if not violations:
        if not quiet:
            print("OK  no language violations found")
        return 0

    # Group by file for cleaner output
    by_file: dict[Path, list[Violation]] = {}
    for v in violations:
        by_file.setdefault(v.path, []).append(v)

    total_files = len(by_file)
    total_lines = len(violations)

    print(f"FAIL  {total_lines} violation(s) in {total_files} file(s)\n")
    for file_path, file_violations in by_file.items():
        print(f"  {file_path}  ({len(file_violations)} line(s))")
        for v in file_violations:
            bad_chars = "".join(ch for _, ch in v.chars[:8])
            preview = v.line.strip()[:90]
            print(f"    line {v.lineno:>4}  [{bad_chars}]  {preview}")
        print()

    print("Fix: rewrite flagged text in English.")
    print(f"     To allow additional scripts, add language codes to allowed_languages in:")
    print(f"     {__file__}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
