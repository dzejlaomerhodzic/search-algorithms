# Search Algorithms

This document contains implementations of several search algorithms used in graph traversal and pathfinding. Specifically, it includes the following algorithms:

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **A Search (with both Manhattan and Euclidean heuristics)**

These algorithms are commonly used in various applications, including puzzle-solving, pathfinding in games, network routing, and more.

## Algorithms Overview

### Depth-First Search (DFS)

DFS is a fundamental search algorithm that explores as deeply as possible along each branch before backtracking. It uses a stack (either explicitly or via recursion) to manage traversal.

#### How DFS Works:
1. Start from the root (or any chosen node).
2. Visit a node and mark it as visited.
3. Recursively visit an unvisited adjacent node.
4. If a node has no unvisited adjacent nodes, backtrack.
5. Repeat until all nodes are visited or a goal is found.

#### Key Characteristics:
- Prioritizes depth over breadth.
- Does not guarantee the shortest path in unweighted graphs.
- Requires less memory than BFS, as it stores only the current path.

#### Advantages:
- Uses less memory in sparse graphs compared to BFS.
- Can be efficient for problems like topological sorting or puzzle solving.

#### Disadvantages:
- May explore unnecessary paths, leading to inefficiency.
- Can fail to find the shortest path.

---

### Breadth-First Search (BFS)

BFS explores all neighbors at the current depth before moving deeper. It uses a queue (FIFO) for traversal.

#### How BFS Works:
1. Start from the root (or any chosen node).
2. Visit all adjacent unvisited nodes, mark them as visited, and enqueue them.
3. Dequeue a node, visit its neighbors, and repeat until all nodes are visited or a goal is found.

#### Key Characteristics:
- Explores nodes level by level.
- Guarantees the shortest path in unweighted graphs.
- Requires more memory than DFS, as it stores all nodes at the current depth.

#### Advantages:
- Guarantees the shortest path is found.
- Useful for shortest path problems in networking or AI.

#### Disadvantages:
- High memory usage for large graphs or dense grids.
- Slower than DFS when the goal is located deep in the graph.

---

### A* Search

A* is a heuristic-based search algorithm that finds the shortest path efficiently by balancing actual distance and estimated cost to the goal.

#### How A* Works:
1. Uses a priority queue (often implemented as a min-heap).
2. Expands nodes with the lowest cost function: **f(n) = g(n) + h(n)**
   - **g(n)** = cost from the start node to **n**.
   - **h(n)** = heuristic estimate from **n** to the goal (e.g., Manhattan or Euclidean distance).
3. Continues until the goal is reached or all possible paths are explored.

#### Key Characteristics:
- Prioritizes nodes based on cost and heuristic.
- Guarantees the shortest path if the heuristic is admissible (never overestimates the cost).
- Uses heuristics to guide the search.

#### Advantages:
- Finds the optimal (shortest) path efficiently.
- Performance depends on the choice of heuristic.

#### Disadvantages:
- Poor heuristic choices can lead to inefficiency.
- Requires more memory than DFS or BFS.

---

## Performance Comparison

The following table summarizes the performance of the algorithms based on runtime, memory usage, and the number of nodes expanded in a specific grid configuration:

| Algorithm          | Runtime (s) | Memory (KB) | Nodes Expanded |
|--------------------|-------------|-------------|----------------|
| DFS               | 0.001       | 12.34       | 8              |
| BFS               | 0.002       | 15.67       | 10             |
| A* (Manhattan)    | 0.003       | 18.23       | 7              |
| A* (Euclidean)    | 0.004       | 20.45       | 9              |

### Findings:
- **DFS** works well for deep pathways in sparse graphs.
- **BFS** is ideal for unweighted graphs where finding the shortest path is necessary.
- **A*** is the best option for weighted graphs or scenarios requiring optimization, particularly with the **Manhattan heuristic** for grid-based navigation.
