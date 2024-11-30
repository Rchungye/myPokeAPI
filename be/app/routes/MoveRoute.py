from app import app
import json
from flask import jsonify, request
from app.controllers import (
    MoveController as Move,
)


@app.route("/move/all", methods=["GET"])
def GetAllMove():
    result = Move.GetAllMove()
    return result.jsonify()

