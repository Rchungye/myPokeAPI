from app import app
import json
from flask import jsonify, request
from app.controllers import PkmController as Pokemon


@app.route("/pokemon/all", methods=["GET"])
def GetAllPokemon():
    result = Pokemon.GetAllPkm()
    return result.jsonify()


