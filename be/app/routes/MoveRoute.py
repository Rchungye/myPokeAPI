from app import app
import json
from flask import jsonify, request
from app.Controllers import (
    MoveController as Move,
)


@app.route("/move/all", methods=["GET"])
def GetAllMove():
    result = Move.GetAllMove()
    return result.jsonify()

