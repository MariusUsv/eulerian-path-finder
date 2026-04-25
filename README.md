# Eulerian Path Finder

## Overview
This project implements an algorithm for detecting and constructing an Eulerian path or Eulerian cycle in an undirected graph.

The solution uses Hierholzer's algorithm and supports graph input from text files.

## Features
- Detects if an undirected graph has an Eulerian path
- Detects if an undirected graph has an Eulerian cycle
- Uses Hierholzer's algorithm
- Reads graph data from text files
- Displays the resulting path
- Supports graph visualization using NetworkX and Matplotlib

## Technologies Used
- Python 3
- NetworkX
- Matplotlib

## Algorithm
The project uses Hierholzer's algorithm.

Eulerian conditions:
- 0 vertices with odd degree → Eulerian cycle
- 2 vertices with odd degree → Eulerian path
- Otherwise → no Eulerian path or cycle
## Author
Student: Marius Zaharia Andronic
Facultatea: Fiesc Calculatoare – dual
