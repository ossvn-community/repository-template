from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "CONTRIBUTING.md",
    "docs/TESTING.md",
    ".github/workflows/validate.yml",
]

errors = []

for path in REQUIRED:
    if not (ROOT / path).exists():
        errors.append(f"Missing required file: {path}")

workflow = ROOT / ".github/workflows/validate.yml"
if workflow.exists():
    text = workflow.read_text(encoding="utf-8")
    if "python scripts/validate_repo.py" not in text:
        errors.append("validate workflow must run: python scripts/validate_repo.py")

if errors:
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

print("Repository validation passed.")
