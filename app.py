from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from rag_model import get_answer

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("send_message")
def handle_message(data):
    question = data.get("question", "")
    answer = get_answer(question)
    socketio.emit("receive_message", {"question": question, "answer": answer})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)
