#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include "sqlite3.h"

using namespace std;

struct Node {
    int id;
    double lat, lon;
};

struct PathNode {
    int id;
    double f_score; 
    bool operator>(const PathNode& other) const { return f_score > other.f_score; }
};

// Haversine formula for real-world distances
double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
    double dLat = (lat2 - lat1) * M_PI / 180.0;
    double dLon = (lon2 - lon1) * M_PI / 180.0;
    double a = sin(dLat/2) * sin(dLat/2) + cos(lat1 * M_PI / 180.0) * cos(lat2 * M_PI / 180.0) * sin(dLon/2) * sin(dLon/2);
    return 12742 * atan2(sqrt(a), sqrt(1-a)); 
}

int main() {
    sqlite3* db;
    if (sqlite3_open("hyderabad_map.db", &db)) return 1;

    int startID, endID;
    if (!(cin >> startID >> endID)) return 1;

    // 1. Fetch all nodes from SQLite into memory for speed
    unordered_map<int, Node> nodes;
    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, "SELECT id, lat, lon FROM nodes", -1, &stmt, NULL);
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        int id = sqlite3_column_int(stmt, 0);
        nodes[id] = {id, sqlite3_column_double(stmt, 1), sqlite3_column_double(stmt, 2)};
    }
    sqlite3_finalize(stmt);

    // 2. A* Algorithm Core
    priority_queue<PathNode, vector<PathNode>, greater<PathNode>> pq;
    unordered_map<int, int> parent;
    unordered_map<int, double> g_score;

    pq.push({startID, 0});
    g_score[startID] = 0;

    while (!pq.empty()) {
        int current = pq.top().id;
        pq.pop();

        if (current == endID) break; // Path found!

        // In a full map, we'd query the 'edges' table here
        // For our 3-node test, let's assume direct links exist
        for (auto const& [neighborID, neighborNode] : nodes) {
            if (neighborID == current) continue;
            
            double weight = calculateDistance(nodes[current].lat, nodes[current].lon, neighborNode.lat, neighborNode.lon);
            double tent_g = g_score[current] + weight;

            if (g_score.find(neighborID) == g_score.end() || tent_g < g_score[neighborID]) {
                parent[neighborID] = current;
                g_score[neighborID] = tent_g;
                double f = tent_g + calculateDistance(neighborNode.lat, neighborNode.lon, nodes[endID].lat, nodes[endID].lon);
                pq.push({neighborID, f});
            }
        }
    }

    // 3. Output the Path for Flutter
    int curr = endID;
    while (curr != startID) {
        cout << nodes[curr].lat << "," << nodes[curr].lon << endl;
        curr = parent[curr];
    }
    cout << nodes[startID].lat << "," << nodes[startID].lon << endl;

    sqlite3_close(db);
    return 0;
}