from app import db
from datetime import datetime


pokemon_move = db.Table('pokemon_move',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('move_id', db.Integer, db.ForeignKey('move.id'), primary_key=True)
)


class Move(db.Model):
    __tablename__ = "move"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    type_move_id = db.Column(db.Integer, db.ForeignKey("type_move.id"), nullable=False)
    type_move = db.relationship('TypeMove')
    pokemons = db.relationship('Pokemon', secondary=pokemon_move, back_populates='moves')

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "type_move_id": self.type_move_id,
            "type_move": self.type_move.as_dict(),
        }


class TypeMove(db.Model):
    __tablename__ = "type_move"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
        }
