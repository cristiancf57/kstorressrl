from flask import Blueprint,render_template

proyectos_bp=Blueprint('proyectos',__name__,template_folder='templates')

@proyectos_bp.route('/')
def proyectos():
    return render_template('proyectos/proyectos.html')