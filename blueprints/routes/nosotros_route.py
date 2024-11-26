from flask import Blueprint, render_template

nosotros_bp = Blueprint('nosotros',__name__,template_folder='templates')

@nosotros_bp.route('/')
def index():
    return render_template('nosotros/nosotros.html')

