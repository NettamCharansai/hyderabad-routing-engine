import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';
import 'package:http/http.dart'
    as http; // Make sure to add 'http' to pubspec.yaml
import 'dart:convert';

void main() {
  runApp(
    const MaterialApp(debugShowCheckedModeBanner: false, home: MapScreen()),
  );
}

class MapScreen extends StatefulWidget {
  const MapScreen({super.key});

  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  final TextEditingController startNode = TextEditingController();
  final TextEditingController endNode = TextEditingController();

  // This list will hold the coordinates returned by your C++ engine
  List<LatLng> routedPoints = [];

  // Function to call your Python Bridge
  Future<void> fetchPath() async {
    final String start = startNode.text;
    final String end = endNode.text;

    try {
      // Points to your Python Bridge running on localhost:5000
      final url = Uri.parse(
        'http://127.0.0.1:5000/navigate?start=$start&end=$end',
      );
      final response = await http.get(url);

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        final List rawPath = data['path'];

        setState(() {
          routedPoints = rawPath.map((p) => LatLng(p[0], p[1])).toList();
        });

        print("Path updated with ${routedPoints.length} points");
      }
    } catch (e) {
      print("Error connecting to backend: $e");
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Ensure Python Bridge is running!")),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Hyderabad Graph Navigator"),
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
      ),
      body: Stack(
        children: [
          FlutterMap(
            options: MapOptions(
              initialCenter: LatLng(17.3850, 78.4867),
              initialZoom: 12.0,
            ),
            children: [
              TileLayer(
                urlTemplate: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                userAgentPackageName: 'com.example.hyderabad_app',
              ),
              // DYNAMIC POLYLINE LAYER
              PolylineLayer(
                polylines: [
                  Polyline(
                    points: routedPoints, // Draws the path from C++
                    color: Colors.blueAccent,
                    strokeWidth: 5,
                  ),
                ],
              ),
            ],
          ),

          // SDE UI Overlay
          Positioned(
            top: 20,
            left: 20,
            right: 20,
            child: Card(
              elevation: 8,
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    TextField(
                      controller: startNode,
                      decoration: const InputDecoration(
                        labelText: "Start Node ID",
                      ),
                    ),
                    TextField(
                      controller: endNode,
                      decoration: const InputDecoration(
                        labelText: "End Node ID",
                      ),
                    ),
                    const SizedBox(height: 15),
                    ElevatedButton.icon(
                      onPressed: fetchPath, // Calls the backend
                      icon: const Icon(Icons.navigation),
                      label: const Text("Find Shortest Path"),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
