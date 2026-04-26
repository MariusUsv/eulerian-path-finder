# Eulerian Path Finder (Python)

## Overview

This project implements an algorithm for detecting and constructing an Eulerian path or Eulerian cycle in an undirected graph.

The solution is based on **Hierholzer’s algorithm**, which efficiently builds the Eulerian path by traversing each edge exactly once.

The application supports:

* reading graphs from text files
* detecting Eulerian path or cycle
* visualizing the graph using NetworkX

---

## Features

* Detects if a graph has:

  * Eulerian cycle (0 odd-degree vertices)
  * Eulerian path (2 odd-degree vertices)
* Constructs the Eulerian path using Hierholzer’s algorithm
* Reads graph data from input files
* Visualizes the graph structure and highlights the Eulerian path
* Saves output path to file

---

## Technologies Used

* Python 3
* NetworkX
* Matplotlib

---

## Algorithm

The project uses **Hierholzer’s algorithm**, with time complexity:

```text
O(E) — where E is the number of edges
```

Eulerian conditions:

* 0 vertices with odd degree → Eulerian cycle
* 2 vertices with odd degree → Eulerian path
* Otherwise → no Eulerian path exists

---

## How to Run

### 1. Install dependencies

```bash
pip install networkx matplotlib
```

### 2. Run the program

```bash
python src/drum_eulerian.py
```

### 3. Provide input file

Example:

```text
graf_drum.txt
```

---

## Example Output

```text
Eulerian path:
1 -> 4 -> 3 -> 2 -> 1 -> 0
```

---

## Project Structure

```text
eulerian-path-finder/
├── src/
│   └── drum_eulerian.py
├── data/
│   ├── graf_drum.txt
│   ├── graf_mare.txt
│   └── graf_mic.txt
├── screenshots/
│   ├── run_example.png
│   └── graph_output.png
├── docs/
│   ├── documentatie.pdf
│   └── prezentare.pptx
└── README.md
```

---

## Screenshots

### Program Output

![Program Output](screenshots/run_example.png)

### Graph Visualization

![Graph Visualization](screenshots/graph_output.png)

---

## What I Learned

* Graph theory fundamentals (Eulerian paths & cycles)
* Implementation of Hierholzer’s algorithm
* Working with file-based input
* Data visualization using NetworkX and Matplotlib
* Structuring a Python project for real-world usage

---

## Why This Project Matters

This project demonstrates:

* algorithmic thinking
* practical implementation of graph algorithms
* clean project structure
* ability to build complete, working applications

---
## Author
Student: Marius Zaharia Andronic
Facultatea: Fiesc Calculatoare – dual
