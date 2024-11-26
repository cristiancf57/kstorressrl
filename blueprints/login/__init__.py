from flask import Blueprint,render_template,request,redirect,session
from sqlalchemy import and_
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from database import Usuarios,Users,init_db,db,app

login_bp=Blueprint('login',__name__,template_folder='templates')

app.secret_key = 'clavesecreta'

# def login_required(f):
#     @wraps(f)
#     def decorate_function(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect('/login')
#         return f(*args, **kwargs)
#     return decorate_function

@login_bp.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=request.form['username']
        password=request.form['password']

        usuario = Users.query.filter_by(username=user).first()
        # usuario = Users.query.filter(and_(Users.username == user,Users.passwd==password)).first()
        if usuario and check_password_hash(usuario['password'],password):
            session['user_id']=usuario['usuario_id']
            return redirect('/admin/dashboard')
    return render_template('login.html')