from flask import Blueprint,render_template,redirect,url_for

nosotros_bp=Blueprint('nosotros',__name__,template_folder='templates')

@nosotros_bp.route('/')
def nosotros():
    return render_template('nosotros.html')
