from flask import Flask, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

@app.route('/')
def index():
    
    return render_template('home.html')

@app.route('/crearUsuario',methods=['POST', 'GET'])
def crearUsuario():
    session['nombre'] = request.form['nombre']
    session['contra'] = request.form['contra']
    msg=session['nombre']
    return render_template("inicio.html", msg=msg)

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registrarse',methods=['POST', 'GET'])
def registrarse():

    session['nombre'] = request.form['nombre']
    session['contra'] = request.form['contra']
    session['pais']=request.form['pais']
    msg=session['nombre']
    return render_template("inicio.html", msg=msg)


app.run(host='0.0.0.0', port=81)