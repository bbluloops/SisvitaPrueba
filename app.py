from flask import Flask
from utils.db import db
from services.estudiante import estudiantes
from services.Test import Tests
from services.opcionesTest import OpcionesTests
from services.especialista import especialistas
from services.preguntasTest import PreguntasTests
from services.horarioEspecialista import HorariosEspecialistas
from services.especialidad import Especialidades
from services.estadoCita import EstadosCita
from services.rangosPuntaje import RangosPuntajes
from services.respuestasTest import RespuestasTests
from config import DATABASE_CONNECTION

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

db.init_app(app)

app.register_blueprint(estudiantes)
app.register_blueprint(Tests)
app.register_blueprint(OpcionesTests)
app.register_blueprint(especialistas)
app.register_blueprint(PreguntasTests)
app.register_blueprint(HorariosEspecialistas)
app.register_blueprint(Especialidades)
app.register_blueprint(EstadosCita)
app.register_blueprint(RangosPuntajes)
app.register_blueprint(RespuestasTests)
with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
