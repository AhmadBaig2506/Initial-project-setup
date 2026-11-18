import sys
import importlib

packages = [
    "ddgs",
    "trafilatura",
    "rank_bm25",
    "streamlit",
    "requests",
    "pytest"
]

print("Python:", sys.version)
print("\nChecking dependencies...")

failed = []

for package in packages:
    try: 
        importlib.import_module(package)
        print(f"[PASS] {package}")
    except ImportError:
        print(f"[FAIL] {package}")
        failed.append(package)

if failed:
    raise SystemExit(
        f"Missing dependencies: {failed}"
    )

print("\nDay 1 environment verification passed!")