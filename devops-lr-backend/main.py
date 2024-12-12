import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = os.path.join('data', 'data.txt')

@app.route('/api/send-data', methods=['POST'])
def receive_data():
    data = request.json.get('data')
    with open(DATA_FILE, 'a') as f:
        f.write(data + '\n')
    return {'status': 'success'}



@app.route('/api/get-data', methods=['GET'])
def get_data():
    with open(DATA_FILE, 'r') as f:
        data = f.read()
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
