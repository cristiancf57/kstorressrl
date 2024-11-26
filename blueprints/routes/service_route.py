from flask import Blueprint,render_template

service_bp=Blueprint('servicios',__name__,template_folder='templates')

@service_bp.route('/')
def service():
    return render_template('servicios/service.html')