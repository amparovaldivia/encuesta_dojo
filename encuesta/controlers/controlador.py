from encuesta import app
from flask import render_template,redirect,request,session
@app.route('/')
def formulario():
    return render_template('formulario.html')
@app.route('/result')
def resultado():
    data={
        'nombre':session['nombre'],
        'ubicacion':session['ubicacion'],
        'favorito':session['favorito'],
        'comentario':session['comentario']
    }
    return render_template('datos.html',dato=data)
@app.route('/result',methods=['POST'])
def  guardar_data():
    session['nombre']=request.form['nombre']
    session['ubicacion']=request.form['ubicacion']
    session['favorito']=request.form['favorito']
    session['comentario']=request.form['comentario']
    return redirect('/result')  
