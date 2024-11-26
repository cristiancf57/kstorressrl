from flask import Blueprint,render_template

contacto_bp=Blueprint('contacto',__name__,template_folder='templates')

@contacto_bp.route('/')
def contacto():
    return render_template('contacto/contacto.html')