from app import app
import json
from flask import jsonify, request
from app.controllers import AbilityController as Ability


@app.route("/ability/all", methods=["GET"])
def GetAllAbility():
    result = Ability.GetAllAbility()
    return result.jsonify()


