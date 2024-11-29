from app import db
from datetime import datetime


pokemon_ability = db.Table('pokemon_ability',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id'), primary_key=True)
)


class Ability(db.Model):
    __tablename__ = "ability"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    pokemons = db.relationship('Pokemon', secondary=pokemon_ability, back_populates='abilities')  # This matches now

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
        }