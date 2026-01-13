# Simple Python Concorde Wrapper 🚀

[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.8%20%7C%203.10%20%7C%203.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20wsl-lightgrey)](https://ubuntu.com/)

A robust and straightforward solution to solve the **Traveling Salesman Problem (TSP)** using the **Concorde Solver** directly from Python. This approach avoids the complex installation and compilation headaches associated with traditional wrappers.



## 📌 Why this repository?

Most Python packages for Concorde (such as `pyconcorde`) attempt to compile 20-year-old C code into Python extensions. This frequently fails on modern systems due to GCC version mismatches or missing legacy headers.

This project uses a **"Loosely Coupled"** architecture:
- **Zero Compilation:** Interacts directly with official pre-compiled binaries.
- **Environment Agnostic:** Works flawlessly on any Python version (3.6+) and Linux distribution.
- **Production Ready:** Separates data preparation, solver execution, and result parsing.

## 🛠️ Prerequisites

* **OS:** Linux (Ubuntu 18.04+) or **WSL** (Windows Subsystem for Linux).
* **Python 3.x**.
* **External Binaries:** Concorde and QSopt (installation steps below).

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone [https://github.com/felipe-astudillo-s/simple-concorde-python.git](https://github.com/felipe-astudillo-s/simple-concorde-python.git)
cd simple-concorde-python
```
### 2. Install Official Solvers
You must download the binaries directly from the University of Waterloo. Follow these exact steps in your terminal:

#### **A. Concorde Solver**
1. Visit the [Official Concorde Downloads Page](https://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm).
2. Download the `concorde-linux` binary from the *Executable Programs* section.
3. Move the file to your project root and rename it to `concorde`.
4. Grant execution permissions:
```bash
# If the file is compressed (concorde.gz), first run: gunzip concorde.gz
chmod +x concorde
```
#### **B. QSopt (Linear Programming Solver)**
Required for Concorde to handle complex optimizations and large datasets.

1. Go to the [QSopt Download Page](https://www.math.uwaterloo.ca/~bico/qsopt/downloads/downloads.htm).
2. Locate the **Ubuntu 18 (with -fPIC)** section.
3. Download both the **Solver Executable** (`qsopt`) and the **Function Library** (`qsopt.a`).
4. Move both files to the project root and grant permissions:
```bash
chmod +x qsopt
```
Note: At the end of this step, your folder must contain: concorde, qsopt, and qsopt.a

## 💻 Usage

The project is structured for immediate use:
* `concorde_solver.py`: Core logic class handling file I/O and process execution.
* `example.py`: A comprehensive script to generate random nodes and solve them.

To run the demonstration:
```bash
python3 example.py
```
### Quick Code Snippet:
```python
from concorde_solver import ConcordeSolver

# 1. Prepare your coordinates (List of tuples)
points = [(0, 0), (10, 5), (20, 10), (5, 20)]

# 2. Initialize and Generate .tsp file
solver = ConcordeSolver(executable_path="./concorde")
tsp_path = solver.create_tsp_file(points, "my_problem.tsp")

# 3. Solve and Parse Results
sol_path = solver.run_solver(tsp_path)
if sol_path:
    tour = solver.read_solution(sol_path)
    print(f"Optimal Visit Order: {tour}")
```


## 📂 Project Structure
```text
.
├── concorde_solver.py  # Wrapper Class (The "Engine")
├── example.py          # Demo script with random data generation
├── .gitignore          # Keeps your repo clean of binaries and temp files
└── README.md           # Documentation
```

## 📄 License
This project is licensed under the MIT License. 

**Important Note:** Concorde and QSopt are owned by the University of Waterloo and are subject to their own academic use licenses. Please refer to their official websites for more information.

---
**Built to simplify optimization workflows. If this helped you, consider giving it a ⭐!**

