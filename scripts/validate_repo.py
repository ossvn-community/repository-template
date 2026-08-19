from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "CONTRIBUTING.md",
    "docs/TESTING.md",
    ".ossvn.yml",
    ".github/workflows/validate.yml",
]

errors = []

for path in REQUIRED:
    if not (ROOT / path).exists():
        errors.append(f"Missing required file: {path}")

manifest = ROOT / ".ossvn.yml"
if manifest.exists():
    text = manifest.read_text(encoding="utf-8")
    if not re.search(r"(?m)^risk_level:\s*R[0-3]\s*$", text):
        errors.append(".ossvn.yml must contain risk_level: R0, R1, R2 or R3")
    if not re.search(r"(?m)^\s*-\s*validate\s*$", text):
        errors.append(".ossvn.yml testing.required_checks must include validate")

workflow = ROOT / ".github/workflows/validate.yml"
if workflow.exists():
    text = workflow.read_text(encoding="utf-8")
    if "python scripts/validate_repo.py" not in text:
        errors.append("validate workflow must run: python scripts/validate_repo.py")

if errors:
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

print("Repository validation passed.")
