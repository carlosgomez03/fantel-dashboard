from utils.db import db
from flask_login import UserMixin


class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Marca = db.Column(db.String(20), nullable=False, unique=True)
    Modelo = db.Column(db.String(80), nullable=False)
    Placa = db.Column(db.String(50), nullable=False)
    Clase = db.Column(db.String(20), nullable=False)

    def __init__(self, Marca, Modelo, Placa, Clase) -> None:
        self.Marca = Marca
        self.Modelo = Modelo
        self.Placa = Placa
        self.Clase = Clase

    def __repr__(self):
        return f"User({self.id}, '{self.Marca}', '{self.Modelo}', '{self.Placa}', '{self.Clase}')"
