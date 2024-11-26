from flask import Flask
from flask_sqlalchemy import SQLAlchemy
def create_app():
    app = Flask(__name__)
    # Configuración de la base de datos MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/kstorres"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar SQLAlchemy
    db = SQLAlchemy(app)
    