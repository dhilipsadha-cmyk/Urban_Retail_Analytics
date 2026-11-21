# Urban Retail Analytics System

Python Module End Assessment 1 - Advanced Data Science Program.

## Contents
| File | Purpose |
|---|---|
| `Urban_Retail_Analytics.ipynb` | Notebook with complete code and outputs (all 5 sections) |
| `main.py` | Same code as a script (run in VS Code) |
| `inventory_utils.py` | Custom module with `check_stock()` |
| `audit_log.txt` | Log file produced by Section 3.2 |

## Sections covered
1. Basic syntax: tax calculator, order size classifier
2. Loops (`continue`/`break`), functions, lambda, recursion
3. Tuple, set, dict, list comprehension, file handling, try/except/else/finally
4. `random`, `datetime`, custom module import
5. OOP: `StoreBranch` / `FlagshipStore` with encapsulation, inheritance, overriding

## Setup (virtual environment)
```bash
python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# macOS/Linux:           source .venv/bin/activate
pip install -r requirements.txt
```
In VS Code: Ctrl+Shift+P -> *Python: Select Interpreter* -> pick `.venv`.

## Setup (virtual environment)
```bash
python -m venv venv
# Windows:  venv\Scripts\activate
# macOS/Linux:  source venv/bin/activate
pip install -r requirements.txt
```
In VS Code: Ctrl+Shift+P -> *Python: Select Interpreter* -> pick the `venv` one.

## How to run
```bash
python main.py
```
Or open the notebook in VS Code (Python + Jupyter extensions) and choose *Run All*.
