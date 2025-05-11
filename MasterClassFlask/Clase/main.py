# This is a simple Flask application that returns "Hola mundo!!!" when accessed at the root URL.
# It also includes a variable 'nombre' that is set to "Angel".

from datetime import datetime
from itertools import repeat
from flask import Flask, render_template 

# Create a Flask application instance
# Import the Flask class from the flask module

app = Flask(__name__) 

# --------------------------------------------------
# 1️⃣  Página de inicio
# --------------------------------------------------
@app.route("/")        # ruta raíz
@app.route("/home")    # alias /home → misma función
def home():
    """
    Renderiza la página de inicio.
    Pasamos la variable 'name' para saludar al usuario.
    """
    date = datetime.now()

    return render_template(
        "home.html", 
        name="Ángel", 
        date=date, 
        repeat=repeat
        )


# --------------------------------------------------
# 4️⃣  Páginas “estáticas” (renderizadas con Jinja,
#     pero sin lógica adicional)
# --------------------------------------------------

@app.route("/contacto")
def contacto():
    """Muestra la página de contacto."""
    return render_template("contacto.html")


@app.route("/servicios")
def servicios():
    """Muestra la página de servicios."""
    return render_template("servicios.html")

@app.route("/clientes")
def clientes():
    """Muestra la página de clientes."""
    return render_template("clientes.html")


# --------------------------------------------------
# 2️⃣  Saludo simple
# --------------------------------------------------
@app.route("/saludo_personal/<nombre>")
def saludo_personal(nombre):
    """
    Saluda al usuario con el nombre capturado en la URL.
    Ej.: /saludo_personal/Ada -> “Bienvenido Ada”
    """
    return f"<h1>Bienvenido {nombre}</h1>"


ç# --------------------------------------------------
# 3️⃣  Saludo con edad
# --------------------------------------------------
@app.route("/saludo_edad/<nombre>/<int:edad>")
def saludo_edad(nombre, edad):
    """
    Devuelve un mensaje distinto según la edad recibida:
    - < 18  : menor de edad
    - == 18 : acaba de cumplir la mayoría
    - > 18  : mayor de edad
    """
    # Determinamos el texto adecuado
    if edad < 18:
        titulo = "eres menor de edad"
    elif edad == 18:
        titulo = "acabás de cumplir la mayoría de edad"
    else:
        titulo = "eres mayor de edad"

    # Nota: devolvemos HTML en crudo porque es un ejemplo rápido
    return f"<h1>Hola {nombre}, tienes {edad} años, {titulo}.</h1>"

# --------------------------------------------------
# 5️⃣  C:\Users\roman\Cursos\IBM_Python_Avanzado\TemarioCurso\11 Flask\Ejemplos
# --------------------------------------------------