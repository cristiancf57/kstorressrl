from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/kstorres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Modelo 
class Profesiones(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    profesion = db.Column(db.String(60),nullable=False)
    abreviado = db.Column(db.String(5),nullable=False)
    usuario = db.relationship('Usuarios',backref='titulo', lazy=True)

class Roles(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    cargo = db.Column(db.String(50),nullable=True)
    usuario = db.relationship('Usuarios',backref='rol',lazy=True)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    foto = db.Column(db.Text,nullable=True)
    telefono = db.Column(db.Numeric(9),nullable=True)
    salario = db.Column(db.Numeric(10,2),nullable=False)
    obs = db.Column(db.Text,nullable=True)
    id_profesion = db.Column(db.String(5),db.ForeignKey('profesiones.id'),nullable=False)
    id_rol = db.Column(db.String(5),db.ForeignKey('roles.id'),nullable=False)
    user = db.relationship('Users', backref='user', lazy=True)
    proyecto = db.relationship('Proyectos', backref='supervisor', lazy=True)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),nullable=False,unique=True)
    passwd = db.Column(db.Text,nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

class Proyectos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    proyecto = db.Column(db.String(100),nullable=False)
    caracteristica = db.Column(db.String(100),nullable=False)
    superfice = db.Column(db.Numeric(15),nullable=True)
    ubicacion = db.Column(db.String(100),nullable=False)
    imagen = db.Column(db.Text,nullable=True)
    fecha_inicio = db.Column(db.Date,nullable=False)
    fecha_fin = db.Column(db.Date,nullable=True)
    estado = db.Column(db.String(20),nullable=True)
    presupuesto = db.Column(db.Numeric(10,2),nullable=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuarios.id'),nullable=False)
    gastos = db.relationship('Gastos',backref='gasto',lazy=True)
    intentario = db.relationship('Inventarios',backref='almacen',lazy=True)
    foto = db.relationship('Fotos',backref='foto',lazy=True)

class Gastos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    monto = db.Column(db.Numeric(8,2),nullable=False)
    concepto = db.Column(db.Text,nullable=False)
    nro_factura = db.Column(db.Numeric(11),nullable=False)
    fecha = db.Column(db.Date,nullable=False)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyectos.id'),nullable=False)

class Inventarios(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    material = db.Column(db.String(200),nullable=True)
    cantidad = db.Column(db.Numeric(10),nullable=False)
    unidad = db.Column(db.String(20),nullable=True)
    costo_unit = db.Column(db.Numeric(10,2),nullable=False)
    total = db.Column(db.Numeric(15,2),nullable=True)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyectos.id'),nullable=False)

class Fotos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    detalle = db.Column(db.Text,nullable=False)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyectos.id'),nullable=False)

# funcion para inicializar la base de datos
def init_db():
    with app.app_context():
        db.create_all()
        print("\nBase de datos creada satisfactoriamente\n")

if __name__ == "__main__":
    init_db()