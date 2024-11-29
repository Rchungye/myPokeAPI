from . import ControllerObject
from datetime import datetime, date
from app import app, db
from app.Models.Region import Region

def GetAllRegion():
    regions = Region.query.all()
    return ControllerObject(
        payload=[region.as_dict() for region in regions], status=200)

