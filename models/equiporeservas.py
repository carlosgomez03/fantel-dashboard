from utils.db import db

class ReservaEquipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solicitudno = db.Column(db.String(50), nullable=False)
    solicitante = db.Column(db.String(50), nullable=False)
    numinventario = db.Column(db.String(50), nullable=False)
    fechaesperada = db.Column(db.String(20), nullable=False)
    motivosalida = db.Column(db.String(20), nullable=False)
    portadores = db.Column(db.String(300), nullable=False)
    fecharetorno = db.Column(db.String(20), nullable=False)
    funcionamiento = db.Column(db.Boolean, nullable=False)
    comentarios = db.Column(db.String(20), nullable=False)
    verificadorRetorno = db.Column(db.String(50), nullable=False)
    
    
    
    
    def __init__(self, solicitante, idSala, fecha, horaInicio, horaFinal) -> None:
        self.solicitante = solicitante
        self.idSala = idSala
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
 
    def __repr__(self):
        return f"User({self.id}, '{self.solicitante}', '{self.idSala}', '{self.fecha}', '{self.horaInicio}', '{self.horaFinal}')"
