

#  Hyderabad Routing Engine 

A **high-performance geospatial routing system** that combines low-level computational efficiency (C++) with a scalable API layer and modern mobile visualization.

This project demonstrates **system design, performance optimization, and end-to-end architecture**, making it suitable for real-world navigation workloads.

---

##  Overview

The Hyderabad Routing Engine computes optimal routes between locations using an efficient implementation of the **A* search algorithm** with geospatial heuristics.

It is designed as a **multi-layer system**:

* High-performance computation (C++)
* API orchestration (Python Flask)
* Data management (SQLite with indexing)
* Visualization (Flutter mobile app)

---

##  System Architecture

```text
                ┌──────────────────────────┐
                │     Mobile Client        │
                │      (Flutter App)       │
                └──────────┬───────────────┘
                           │ HTTP Request
                           ▼
                ┌──────────────────────────┐
                │     API Layer            │
                │   (Flask + Gunicorn)     │
                └──────────┬───────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                                      │
        ▼                                      ▼
┌──────────────────────┐             ┌──────────────────────┐
│   Cache Layer        │             │   Logging System      │
│   (Redis - Optional) │             │ (Requests / Errors)   │
└──────────┬───────────┘             └──────────────────────┘
           │
           ▼
┌──────────────────────────┐
│   Routing Engine Layer   │
│   (C++ A* Algorithm)     │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│     Data Layer           │
│ (SQLite + Indexing)      │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│   Response Formatter     │
│   (JSON Output)          │
└──────────┬───────────────┘
           │
           ▼
   ┌──────────────────────┐
   │   Mobile Client UI   │
   │ (Map Visualization)  │
   └──────────────────────┘
```

---

##  Data Flow

### Step-by-step request lifecycle:

### 1. Client Request

User inputs source and destination in the Flutter app.

```json
POST /route
{
  "source": "A",
  "destination": "B"
}
```

---

### 2. API Layer (Flask)

* Receives request
* Validates input
* Logs request

---

### 3. Cache Lookup 

* If route exists → return immediately
* Else → proceed to compute

---

### 4. Routing Engine Execution

Flask invokes the C++ engine:

```bash
./navigator source destination
```

---

### 5. A* Algorithm Processing

The shortest path is computed using:

[
f(n) = g(n) + h(n)
]

Where:

* **g(n)** = actual cost from source
* **h(n)** = heuristic (Haversine distance)

---

### 6. Data Layer Access

* Nodes and edges fetched from SQLite
* Indexed queries improve lookup performance

---

### 7. Path Computation Output

Engine returns ordered nodes representing optimal path.

---

### 8. API Response Formatting

```json
{
  "route": ["NodeA", "NodeB", "NodeC"],
  "distance": "X km",
  "time": "Y mins"
}
```

---

### 9. Observability

* Logs request metadata
* Tracks response latency
* Captures errors

---

### 10. Client Visualization

Flutter renders route on map with distance and ETA.

---

##  Tech Stack

| Layer                 | Technology               |
| --------------------- | ------------------------ |
| Core Engine           | C++ (A* Algorithm)       |
| API                   | Python (Flask)           |
| Database              | SQLite (Indexed queries) |
| Frontend              | Flutter                  |
| Optional Enhancements | Redis, Docker, CI/CD     |

---

##  Key Features

* Efficient **A* pathfinding with geospatial heuristics**
* Modular **multi-language architecture**
* Optimized **data retrieval using indexing**
* Scalable API design (stateless)
* Extensible for caching and distributed systems

---

##  Performance (Example Benchmark)

| Metric              | Value      |
| ------------------- | ---------- |
| Avg Response Time   | ~80–120 ms |
| Concurrent Requests | 100 users  |
| Dataset Size        | Scalable   |

> Benchmarked using load testing tools (k6 / custom scripts)

---

##  Installation & Usage

### 1. Clone Repository

```bash
git clone https://github.com/NettamCharansai/hyderabad-routing-engine.git
cd hyderabad-routing-engine
```

---

### 2. Compile C++ Engine

```bash
g++ src/engine.cpp -o navigator
```

---

### 3. Run API Server

```bash
cd src/api
python app.py
```

---

### 4. Run Mobile App

```bash
flutter run
```

---

##  Docker Support 

```bash
docker-compose up --build
```

---

##  CI/CD 

* Automated build pipeline
* Test execution
* Docker image generation

---

##  Future Enhancements

* Kubernetes-based scaling
* Real-time traffic integration
* Distributed caching (Redis cluster)
* Advanced observability (Prometheus + Grafana)

---

##  Engineering Highlights

* Combines **low-level performance (C++) with high-level orchestration**
* Demonstrates **system design thinking and scalability awareness**
* Built with a focus on **real-world deployment patterns**

---

##  License

MIT License

---

##  Author

**Nettam Charan Sai**

* GitHub: [https://github.com/NettamCharansai](https://github.com/NettamCharansai)
* LeetCode: [https://leetcode.com/u/CharanSai1/](https://leetcode.com/u/CharanSai1/)


Just tell me 👍
