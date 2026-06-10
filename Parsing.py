import pymupdf
from pathlib import Path
import os

base_dir = Path.home()
CURRENT_DIR = Path(__file__).resolve().parent

doc = pymupdf.open()

print(f"Base Dir: {base_dir}")
print(f"Current Dir: {CURRENT_DIR}")
print("Success")