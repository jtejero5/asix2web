from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Inicializar la base de datos al iniciar
database.init_db()

@app.route('/')
def index():
    return redirect(url_for('getmail'))

@app.route('/getmail', methods=['GET', 'POST'])
def getmail():
    resultado = None
    error = None
    nombre_busqueda = ""
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombre_busqueda = nombre
        
        if nombre:
            resultado_bd = database.buscar_email(nombre)
            if resultado_bd:
                resultado = resultado_bd['email']
            else:
                error = f"No se encontró el usuario '{nombre}'"
        else:
            error = "Por favor, introduce un nombre"
    
    return render_template('getmail.html', 
                         resultado=resultado, 
                         error=error,
                         nombre_busqueda=nombre_busqueda)

@app.route('/addmail', methods=['GET', 'POST'])
def addmail():
    mensaje = None
    tipo_mensaje = ""  # success o error
    datos_form = {"nombre": "", "email": ""}
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        
        datos_form = {"nombre": nombre, "email": email}
        
        if nombre and email:
            exito, mensaje_db = database.agregar_usuario(nombre, email)
            mensaje = mensaje_db
            tipo_mensaje = "success" if exito else "error"
            
            # Si se agregó correctamente, limpiar el formulario
            if exito:
                datos_form = {"nombre": "", "email": ""}
        else:
            mensaje = "Por favor, completa todos los campos"
            tipo_mensaje = "error"
    
    return render_template('addmail.html', 
                         mensaje=mensaje, 
                         tipo_mensaje=tipo_mensaje,
                         datos_form=datos_form)

if __name__ == '__main__':
    app.run(debug=True)