from . import ControllerObject
from datetime import datetime, date
from app import app, db
from app.Models.Ability import Ability

def GetAllAbility():
    abilitys = Ability.query.all()
    return ControllerObject(
        payload=[ability.as_dict() for ability in abilitys], status=200)

