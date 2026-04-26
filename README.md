# 🔍 Eulerian Path Finder

## 📌 Overview

This project implements an efficient algorithm for detecting and constructing an **Eulerian path** in an undirected graph.

It reads graph data from a file, checks if an Eulerian path exists, and if so, computes it using **Hierholzer’s algorithm**. The result is displayed both in the console and as a graphical visualization.

---

## ⚙️ Features

* ✔️ Read graph from `.txt` file (edge list)
* ✔️ Detect if Eulerian path exists
* ✔️ Identify nodes with odd degree
* ✔️ Compute Eulerian path (Hierholzer algorithm)
* ✔️ Graph visualization using NetworkX + Matplotlib
* ✔️ Clean modular structure (ready for scaling)

---

## 🧠 Algorithm Used

The project uses **Hierholzer’s Algorithm**, which constructs an Eulerian path in linear time:

* Time Complexity: **O(E)**
* Works for graphs with:

  * 0 odd-degree nodes → Eulerian circuit
  * 2 odd-degree nodes → Eulerian path

---

## 📂 Project Structure

```
eulerian-path-finder/
│
├── src/
│   ├── drum_eulerian.py
│
├── data/
│   ├── graf_drum.txt
│   ├── graf_mare.txt
│   ├── graf_mic.txt
│
├── screenshots/
│   ├── program_output.png
│   ├── graph_visual.png
│
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install networkx matplotlib
```

### 2. Run the program

```bash
python src/drum_eulerian.py
```

### 3. Input example

```
Enter graph file: data/graf_drum.txt
```

---

## 🧪 Example Input (graf_drum.txt)

```
0 1
1 2
2 3
3 4
4 1
```

---

## 📊 Output Example

```
=== EULERIAN PATH FINDER ===
Eulerian path:
1 → 4 → 3 → 2 → 1 → 0
```

---

## 📸 Screenshots

### Program Output

![Program Output](screenshots/program_output.png)

### Graph Visualization

![Graph Visualization](screenshots/graph_visual.png)

---

## 🛠️ Technologies Used

* Python 3
* NetworkX
* Matplotlib

---

## 📈 Possible Improvements

* Add support for directed graphs
* Export results to file (JSON / CSV)
* Interactive UI (Tkinter / Web)
* Performance optimization for large graphs

---

## 👤 Author

**Marius Andronic**
Computer Dual Engineering Student
Focused on practical systems, algorithms, and real-world applications

---

## 📄 License

This project is open-source and available under the MIT License.
