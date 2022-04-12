from utils.db import db


class ReservaTransporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solicitante = db.Column(db.String(50), nullable=False )
    acompanantes = db.Column(db.String(50), nullable=True)
    origen = db.Column(db.String(300), nullable=False)
    destino = db.Column(db.String(300), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    horaInicio = db.Column(db.String(20), nullable=False)
    esperar = db.Column(db.Boolean, nullable=False)
    recogerLuego = db.Column(db.Boolean, nullable=False)
    horaRecoger = db.Column(db.String(20), nullable=True)
    motivo = db.Column(db.String(300), nullable=False)
    vehiculoSolicitado = db.Column(db.String(100), nullable=False)
    servicioProvisto = db.Column(db.Boolean, nullable=False)
    comentariosAdministracion = db.Column(db.String(500), nullable=True)
    identificadorArchivos = db.Column(db.String(100), nullable=False)
    
    
    def __init__(self, solicitante, acompanantes, origen, destino, fecha, horaInicio, esperar, recogerLuego, horaRecoger, motivo, vehiculoSolicitados, servicioProvisto, comentariosAdministracion, identificadorArchivos) -> None:
        self.solicitante = solicitante
        self.acompanantes = acompanantes
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.esperar = esperar
        self.recogerLuego = recogerLuego
        self.horaRecoger = horaRecoger
        self.motivo = motivo
        self.vehiculoSolicitado = vehiculoSolicitados
        self.servicioProvisto = servicioProvisto
        self.comentariosAdministracion = comentariosAdministracion
        self.identificadorArchivos = identificadorArchivos
 
    def __repr__(self):
        return f"User({self.id}, '{self.solicitante}', '{self.acompanantes}', '{self.origen}', '{self.destino}','{self.fecha}', '{self.horaInicio}', '{self.esperar}', '{self.recogerLuego}', '{self.horaRecoger}', '{self.motivo}', '{self.vehiculoSolicitado}', '{self.servicioProvisto}', '{self.comentariosAdministracion}', '{self.identificadorArchivos}')"
