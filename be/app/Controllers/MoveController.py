from . import ControllerObject
from datetime import datetime, date
from app import app, db
from app.Models.Move import Move

def GetAllMove():
    moves = Move.query.all()
    return ControllerObject(
        payload=[move.as_dict() for move in moves], status=200)