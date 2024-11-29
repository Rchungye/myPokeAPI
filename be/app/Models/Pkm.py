from app import db
from datetime import datetime
from app.Models.Move import Move, TypeMove, pokemon_move
from app.Models.Ability import Ability, pokemon_ability


pokemon_type = db.Table('pokemon_type',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('type_pkm_id', db.Integer, db.ForeignKey('type_pkm.id'), primary_key=True),
    db.Column('created_at', db.DateTime(), nullable=False, default=datetime.now()),
    db.Column('updated_at', db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())
)


class TypePkm(db.Model):
    __tablename__ = "type_pkm"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())
    pokemons = db.relationship('Pokemon', secondary=pokemon_type, back_populates='types')
    
    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    special_attack = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())
    moves = db.relationship('Move', secondary=pokemon_move, back_populates='pokemons')
    abilities = db.relationship('Ability', secondary=pokemon_ability, back_populates='pokemons')  # Changed this line
    types = db.relationship('TypePkm', secondary=pokemon_type, back_populates='pokemons')

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "special_attack": self.special_attack,
            "special_defense": self.special_defense,
            "speed": self.speed,
            "weight": self.weight,
            "moves": [move.as_dict() for move in self.moves],
            "abilities": [ability.as_dict() for ability in self.abilities],
            "types": [type.as_dict() for type in self.types],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }