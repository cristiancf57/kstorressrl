from flask import Flask
# Registrar Blueprints
from blueprints.routes.welcome_route import welcome_bp
from blueprints.routes.nosotros_route import nosotros_bp
from blueprints.routes.service_route import service_bp
from blueprints.routes.proyectos_route import proyectos_bp
from blueprints.routes.contacto_route import contacto_bp
from blueprints.login import login_bp

def create_route():
    app = Flask(__name__)

    app.register_blueprint(welcome_bp)
    app.register_blueprint(nosotros_bp, url_prefix='/nosotros')
    app.register_blueprint(service_bp,url_prefix='/servicios')
    app.register_blueprint(proyectos_bp,url_prefix='/proyectos')
    app.register_blueprint(contacto_bp,url_prefix='/contacto')
    app.register_blueprint(login_bp,url_prefix='/login')

    return app
