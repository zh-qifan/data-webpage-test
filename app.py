from flask import Flask, jsonify, send_from_directory
import random

app = Flask(__name__)

# Sample data
data1 = {
    "value": 0
}

data2 = {
    "value": 0
}

@app.route('/data1')
def get_data1():
    data1["value"] = random.randint(1, 100)
    return jsonify(data1)

@app.route('/data2')
def get_data2():
    data2["value"] = random.randint(1, 100)
    return jsonify(data2)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
