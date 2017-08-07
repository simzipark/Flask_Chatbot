from app import app
from flask import request, jsonify
from .manager import APIHandler


@app.route("/keyboard/keyboard", methods=["GET"])
def yellow_keyboard():
    message, code = APIHandler.process("home")
    return jsonify(message), code


@app.route("/keyboard/message", methods=["POST"])
def yellow_message():
    message, code = APIHandler.process("message", request.json)
    return jsonify(message), code


@app.route("/keyboard/friend", methods=["POST"])
def yellow_friend_add():
    message, code = APIHandler.process("add", request.json)
    return jsonify(message), code


@app.route("/keyboard/friend/<key>", methods=["DELETE"])
def yellow_friend_block(key):
    message, code = APIHandler.process("block", key)
    return jsonify(message), code


@app.route("/keyboard/chat_room/<key>", methods=["DELETE"])
def yellow_exit(key):
    message, code = APIHandler.process("exit", key)
    return jsonify(message), code
