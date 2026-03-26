from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app) # Allows Flutter to talk to this script

@app.route('/navigate')
def navigate():
    start_id = request.args.get('start')
    end_id = request.args.get('end')
    
    # Trigger the C++ Engine
    process = subprocess.Popen(['../backend/engine.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = process.communicate(input=f"{start_id}\n{end_id}")
    
    # Process coordinates into a list
    path = [[float(x.split(',')[0]), float(x.split(',')[1])] for x in stdout.splitlines()]
    return jsonify({"path": path})

if __name__ == '__main__':
    app.run(port=5000)