from app import app, db
from datetime import datetime


class Region(db.Model):
    __tablename__ = "region"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    pokemons = db.relationship('Pokemon', backref='region', lazy=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())

    def as_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }