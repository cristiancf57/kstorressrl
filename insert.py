from database import db, Profesiones, Roles,Usuarios,Users,init_db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/kstorres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

def insert_Profesiones():
    with app.app_context():
        # instanciacio de objetos
        prof1 = Profesiones(id='ADME',profesion="Administrador de Empresas", abreviado="Lic.")
        prof2 = Profesiones(id='INGC',profesion='Ingeniero Civil',abreviado='Ing')
        prof3 = Profesiones(id='ARQU',profesion='Arquitecto',abreviado='Arq')
        prof4 = Profesiones(id='CONT',profesion='Contador',abreviado='Lic')
        prof5 = Profesiones(id='ECON',profesion='Economista',abreviado='Lic')
        prof6 = Profesiones(id='INGF',profesion='Ingeniero Financiero',abreviado='Ing')
        prof7 = Profesiones(id='INGS',profesion='Ingeniero de Sistemasr',abreviado='Ing')
        prof8 = Profesiones(id='INFO',profesion='Informatica',abreviado='Lic')
        prof9 = Profesiones(id='TECN',profesion='Tecnico',abreviado='Tec')

        db.session.add_all([prof1,prof2,prof3,prof4,prof5,prof6,prof7,prof8,prof9])
        db.session.commit()
        print('\nProfesiones insertados')

def insert_roles():
    with app.app_context():
        rol1 = Roles(id='rot',cargo='Super Admin')
        rol2 = Roles(id='adm',cargo='Administrador')
        rol3 = Roles(id='sup',cargo='Supervisor')
        rol4 = Roles(id='per',cargo='Personal')
        rol5 = Roles(id='usr',cargo='Usuario')

        db.session.add_all([rol1,rol2,rol3,rol4,rol5])
        db.session.commit()
        print('\nRoles insertados')

def insert_usuario():
    with app.app_context():
        Usr=Usuarios(nombre='Juan',apellido='Perez',foto='juan.jpg',telefono='62544275',salario='3000',id_profesion='INGS',id_rol='rot')
        rol1=Users(username='perez',passwd='perez',id_usuario='1')

        db.session.add(Usr)
        db.session.commit()
        print('\nUsuario insertados')
        db.session.add(rol1)
        db.session.commit()
        print('\nUser insertados')

if __name__ == "__main__":
    init_db()
    # insert_Profesiones()
    # insert_roles()
    insert_usuario()