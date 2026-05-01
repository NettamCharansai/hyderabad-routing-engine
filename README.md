                ┌──────────────────────────┐
                │     Mobile Client        │
                │      (Flutter App)       │
                └──────────┬───────────────┘
                           │ HTTP Request (Source, Destination)
                           ▼
                ┌──────────────────────────┐
                │     API Gateway Layer    │
                │   (Flask + Gunicorn)     │
                └──────────┬───────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                                      │
        ▼                                      ▼
┌──────────────────────┐             ┌──────────────────────┐
│   Cache Layer        │             │   Logging System      │
│   (Redis - Optional) │             │ (Request/Errors/Time) │
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
│ (SQLite + Spatial Index) │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│   Response Formatter     │
│   (Flask JSON Output)    │
└──────────┬───────────────┘
           │
           ▼
   ┌──────────────────────┐
   │   Mobile Client UI   │
   │ (Map Visualization)  │
   └──────────────────────┘
