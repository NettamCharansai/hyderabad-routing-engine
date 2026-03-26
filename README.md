# Hyderabad Routing Engine 🛰️

A high-performance navigation system that bridges low-level computational efficiency with a modern mobile interface.

## 🚀 The Tech Stack
- **Engine:** C++17 implementing the **A* Search Algorithm** with Haversine Heuristics.
- **Middleware:** Python (Flask) acting as a high-concurrency wrapper for the C++ binary.
- **Database:** SQLite with spatial indexing for O(1) landmark retrieval.
- **Frontend:** Flutter (Dart) for cross-platform geospatial visualization.

## ⚙️ Core Logic: A* Search
The engine calculates the optimal path by minimizing $f(n) = g(n) + h(n)$, where:
- $g(n)$ is the actual cost from the start node.
- $h(n)$ is the estimated cost to the destination (Haversine distance).

http://googleusercontent.com/image_content/139



## 🛠️ Installation & Usage
1. Compile the Engine: `g++ backend/engine.cpp -o navigator`
2. Run the API: `python bridge/app.py`
3. Launch Mobile App: `flutter run`
