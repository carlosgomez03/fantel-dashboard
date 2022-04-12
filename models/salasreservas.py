from utils.db import db

class ReservaSalas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solicitante = db.Column(db.String(50), nullable=False)
    idSala = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    horaInicio = db.Column(db.String(20), nullable=False)
    horaFinal = db.Column(db.String(20), nullable=False)
    
    
    
    def __init__(self, solicitante, idSala, fecha, horaInicio, horaFinal) -> None:
        self.solicitante = solicitante
        self.idSala = idSala
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
 
    def __repr__(self):
        return f"User({self.id}, '{self.solicitante}', '{self.idSala}', '{self.fecha}', '{self.horaInicio}', '{self.horaFinal}')"
