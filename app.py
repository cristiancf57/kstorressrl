from flask import Flask,render_template,request,redirect,flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'creadsys@gmail.com'  # Cambia esto
app.config['MAIL_PASSWORD'] = '*******'  # Cambia esto
app.config['MAIL_DEFAULT_SENDER'] = 'creadsys@gmail.com'  # Cambia esto
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.secret_key = 'supersecreto'
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/servidet')
def detalleserv():
    return render_template('detallserv.html')

@app.route('/proyectos',methods=['GET','POST'])
def proyectos():
    return render_template('proyectos.html')

@app.route('/noticiadet')
def noticiadet():
    return render_template('noticiadet.html')

@app.route('/contacto',methods=['GET','POST'])
def contacto():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject=subject, recipients=[email])
        msg.body = f"Correo de contacto: {email}\n\nMessaje:\n{message}"
        try:
            mail.send(msg)
            flash('Correo enviado exitosamente.', 'success')
        except Exception as e:
            flash(f'Error al enviar el correo: {str(e)}', 'danger')

        return redirect('contacto.html')
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)