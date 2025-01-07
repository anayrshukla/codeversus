from flask import Flask, jsonify
from flask_socketio import SocketIO
import requests

app = Flask(__name__)
socketio = SocketIO(app)

# Root route
@app.route('/')
def home():
    return "Welcome to Coding 1v1!"

# Judge0 API test route
@app.route('/test')
def test_judge0():
    url = "https://judge0-ce.p.rapidapi.com/submissions"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "6fbb88036dmshfc1766bf072dcbep12b785jsn8f2ba10f773e"  # Replace with your API Key
    }
    data = {
        "source_code": "print('Hello, World!')",
        "language_id": 71,  # Python 3
    }

    # Make the API request
    response = requests.post(url, headers=headers, json=data)

    # Return the API response as JSON
    if response.status_code == 201:  # Submission created successfully
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to connect to Judge0 API", "status_code": response.status_code})

# Run the Flask app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
