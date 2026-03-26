from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app) 

@app.route('/navigate')
def navigate():
    start_id = request.args.get('start')
    end_id = request.args.get('end')
    
    # Run your A* Engine
    process = subprocess.Popen(
        ['./navigator.exe'], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        text=True
    )
    
    # Send IDs to C++
    stdout, _ = process.communicate(input=f"{start_id} {end_id}")
    
    # Parse coordinates
    path = []
    for line in stdout.strip().split('\n'):
        if "," in line:
            lat, lon = map(float, line.split(','))
            path.append([lat, lon])
            
    return jsonify({"path": path})

if __name__ == '__main__':
    print("🚀 Google Maps Replica Bridge is LIVE on http://127.0.0.1:5000")
    app.run(port=5000)