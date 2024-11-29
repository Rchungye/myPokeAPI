from app import app, db
from datetime import datetime


pokemon_move = db.Table('pokemon_move',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('move_id', db.Integer, db.ForeignKey('move.id'), primary_key=True),
    db.Column('created_at', db.DateTime(), nullable=False, default=datetime.now()),
    db.Column('updated_at', db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())
)


class Move(db.Model):
    __tablename__ = "move"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    type_move_id = db.Column(db.Integer, db.ForeignKey("type_move.id"), nullable=False)
    type_move = db.relationship('TypeMove')
    descripcion = db.Column(db.String(200), nullable=False)
    pokemons = db.relationship('Pokemon', secondary=pokemon_move, back_populates='moves')
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "damage": self.damage,
            "type_move_id": self.type_move_id,
            "type_move": self.type_move.as_dict(),
            "descripcion": self.descripcion,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class TypeMove(db.Model):
    __tablename__ = "type_move"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
