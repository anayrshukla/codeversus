from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return "Welcome to Coding 1v1!"

if __name__ == '__main__':
    socketio.run(app, debug=True)
