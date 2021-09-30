from flask import Flask, render_template
from webargs.flaskparser import use_args
from flask_socketio import join_room
from flask_socketio import SocketIO
from webargs import fields
from flask import request

app = Flask(__name__)
app.config["SECRET_KEY"] = "Lorem ipsum dor sit amet"
socketio = SocketIO(app)

args = {
    "signature": fields.Str(required=True),
    "address": fields.Str(required=True)
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app.json")
def app_json():
    return {
        "name": "Callback Test",
        "icon": "https://source.boringavatars.com/beam/120/codepillow?colors=264653,2a9d8f,e9c46a,f4a261,e76f51"
    }

@app.route("/call/<string:session>", methods=["POST"])
@use_args(args, location="json")
def call(args, session):
    socketio.emit(session, args, to=session)
    return {
        "status": "success"
    }

@socketio.on("callback")
def callback(session, *args):
    join_room(session, request.sid)
    return True
