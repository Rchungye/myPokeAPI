import requests
import pandas as pd
from app import db, app
from sqlalchemy import insert

from app.Models.Pkm import Pokemon, TypePkm
from app.Models.Ability import Ability
from app.Models.Move import Move, TypeMove

def seed_db():

    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=150')
    data = response.json()['results']
    df = pd.DataFrame(data)


