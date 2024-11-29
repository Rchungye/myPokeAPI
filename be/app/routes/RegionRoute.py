from app import app
import json
from flask import jsonify, request
from app.Controllers import (
    RegionController as Region,
)


@app.route("/region/all", methods=["GET"])
def GetAllRegion():
    result = Region.GetAllRegion()
    return result.jsonify()
