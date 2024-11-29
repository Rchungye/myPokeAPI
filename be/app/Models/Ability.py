from app import db
from datetime import datetime


pokemon_ability = db.Table('pokemon_ability',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id'), primary_key=True),
    db.Column('created_at', db.DateTime(), nullable=False, default=datetime.now()),
    db.Column('updated_at', db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())
)


class Ability(db.Model):
    __tablename__ = "ability"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    pokemons = db.relationship('Pokemon', secondary=pokemon_ability, back_populates='abilities')  # This matches now
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }