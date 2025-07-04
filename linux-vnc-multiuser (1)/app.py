from flask import Flask, request, redirect, render_template
import uuid
from utils.user_container import create_user_container

app = Flask(__name__)
containers = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start', methods=["POST"])
def start_machine():
    user_id = str(uuid.uuid4())[:8]
    port = 6080 + len(containers)
    url = f"http://localhost:{port}/vnc.html"
    
    create_user_container(user_id, port)
    containers[user_id] = {
        "port": port,
        "url": url
    }
    return render_template("user.html", user_id=user_id, url=url)