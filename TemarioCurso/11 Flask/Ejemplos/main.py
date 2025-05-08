"""
main.py
========
Aplicación Flask sencilla con:
- Página de inicio
- Ejemplos de rutas dinámicas
- Páginas basadas en plantillas Jinja
- Listado de clientes

Para lanzar en consola:
    python main.py
o bien
    flask --app main run --debug
"""

from flask import Flask, render_template, request  # importamos Flask y helper para plantillas
from datetime import datetime  # importamos datetime para mostrar la fecha actual

app = Flask(__name__)  # creamos la aplicación
app.config.from_mapping(
    SECRET_KEY = 'dev'  # ¡SOLO PARA ENTORNOS DE PRUEBA!
)

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

    return render_template("home.html", name="Ángel", date=date, repeat=repeat)




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


# --------------------------------------------------
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


# --------------------------------------------------
# 5️⃣  Lista de clientes
# --------------------------------------------------
@app.route("/clientes")
def clientes():
    """
    Genera una lista de clientes (hard-coded por ahora) y se la
    pasa a la plantilla 'clientes.html' para que Jinja la recorra.
    """
    lista_clientes = [
        "Manolo García",
        "Ana Jiménez",
        "Andrés González",
        "Sonia Pérez",
    ]
    return render_template(
        "clientes.html",
        name="Ángel",           # Para el saludo opcional de la plantilla
        clientes=lista_clientes  # La lista que se mostrará
    )


# --------------------------------------------------
#  Punto de entrada cuando ejecutas “python main.py”
# --------------------------------------------------
if __name__ == "__main__":
    # debug=True recarga el servidor al guardar cambios y
    # muestra trazas completas si algo falla
    app.run(debug=True)


# --------------------------------------------------
# 💻  Filtro personalizado
# --------------------------------------------------
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# --------------------------------------------------
# ✍️  Funciones propias
#     Repetirá un String N veces
# --------------------------------------------------

def repeat(s, n):
    return s * n


# --------------------------------------------------
# 💻  Formulario de registro con WTForm

# --------------------------------------------------
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[
        DataRequired(message="Este campo es obligatorio"),
        Length(min=4, max=25, message="El nombre debe tener entre 4 y 25 caracteres")
    ])
    
    password = PasswordField("Contraseña usuario", validators=[
        DataRequired(message="Este campo es obligatorio"),
        Length(min=6, max=40, message="La contraseña debe tener entre 6 y 40 caracteres")
    ])
    
    submit = SubmitField("Registrar")

# --------------------------------------------------
# 💻  Formulario de registro

# --------------------------------------------------
@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    form = RegisterForm()
    """
    Muestra el formulario de alta de clientes.
    Si se envía el formulario, lo procesa y muestra un mensaje de éxito.
    """
    if request.method == "POST":
        # Aquí procesarías los datos del formulario
        # Por ejemplo, guardar en la base de datos
        username = request.form['username']
        password = request.form['password']
        return f"Nombre de usuario: {username}, Contraseña: {password}"
    return render_template("formulario.html", success=True, form = form)

    # Si no se envía el formulario, simplemente lo mostramos
def formulario():
    """Muestra la página del formulario de alta."""
    return render_template("formulario.html")


