import os
import sys
import re
import glob

# Extensions to ignore
IGNORED_EXTENSIONS = (
    ".txt", ".pdf", ".xlsx", ".csv", ".doc", ".json", ".img", ".png", ".jpg", ".jpeg"
)

def is_ignored_file(file_path):
    return file_path.lower().endswith(IGNORED_EXTENSIONS)

def check_code_standards():
    issues = []
    scanned_files = 0

    for file in glob.glob("**/*", recursive=True):
        if os.path.isdir(file) or is_ignored_file(file):
            continue

        scanned_files += 1

        # Only process Python files
        if file.endswith(".py"):
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            filename = os.path.basename(file)

            # --- General checks ---
            if not lines or not lines[0].strip().startswith('"""'):
                issues.append(f"{file} ⚠️ Missing module docstring")

            for i, line in enumerate(lines, 1):
                if "time.sleep(" in line:
                    issues.append(f"{file}:{i} ❌ Avoid time.sleep(), use Playwright waits")

                if "query_selector(" in line:
                    issues.append(f"{file}:{i} ❌ Use page.locator() instead of query_selector()")

                if "password" in line or "username" in line:
                    issues.append(f"{file}:{i} 🚫 Hardcoded credentials detected")

            # --- Page Object checks ---
            if "pageObjects" in file:
                if not filename.endswith("_page.py"):
                    issues.append(f"{file} ❌ Page Object file must end with '_page.py'")
                if not any("def __init__(self, page)" in l for l in lines):
                    issues.append(f"{file} ❌ Missing constructor: def __init__(self, page):")

            # --- Test Script checks ---
            if "testScripts" in file:
                if not filename.startswith("test_"):
                    issues.append(f"{file} ❌ Test script must start with 'test_'")

                test_blocks = [i for i, l in enumerate(lines) if l.strip().startswith("def test_")]
                for start in test_blocks:
                    block = lines[start:start+20]
                    if not any(("assert" in l or "expect(" in l) for l in block):
                        issues.append(f"{file}:{start+1} ⚠️ Test may be missing an assertion or expect()")

    print(f"🔍 Scanned {scanned_files} files (skipped non-code files).")
    return issues


if __name__ == "__main__":
    problems = check_code_standards()
    if problems:
        print("\n⚠️ Code Review Findings:\n")
        print("\n".join(problems))
        sys.exit(1)
    else:
        print("✅ All code follows Playwright automation standards.")
