from flask import Blueprint, render_template

welcome_bp = Blueprint('welcome',__name__,template_folder='templates')

@welcome_bp.route('/')
def index():
    return render_template('welcome/index.html')