from flask import Flask, send_file, jsonify, CORS
import json
import os

app = Flask(__name__, static_folder='.', static_url_path='/')
CORS(app)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/data.json')
def get_data():
    try:
        with open('data.json', 'r') as f:
            return jsonify(json.load(f))
    except:
        return jsonify({error: 'Data file not found'}), 404

@app.route('/status')
def status():
    return jsonify({status: 'ok'})

if __name__ == '__main__':
    port = int(os.getenv.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port, debug=True)
