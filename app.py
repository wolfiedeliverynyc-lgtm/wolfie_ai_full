from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from agents import ChiefAI
import os

app = Flask(__name__)
CORS(app)
chief = ChiefAI()

UPLOAD_FOLDER = "project_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_task', methods=['POST'])
def send_task():
    agent = request.form.get("agent")
    task = request.form.get("task")
    files = request.files.getlist("files")
    # حفظ الملفات
    for f in files:
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    result = chief.delegate(agent, task, files)
    return jsonify({"result": result})

@app.route('/agents', methods=['GET'])
def list_agents():
    return jsonify({"agents": list(chief.agents.keys())})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
