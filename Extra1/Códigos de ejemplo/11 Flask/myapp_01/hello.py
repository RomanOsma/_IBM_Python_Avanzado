# ----------------------------------------------------------------------
# Importamos Flask para la app y render_template para renderizar HTML
# ----------------------------------------------------------------------
from flask import Flask, render_template
from markupsafe import escape   # Escape evita XSS al mostrar texto arbitrario

# ----------------------------------------------------------------------
# Creamos la aplicación Flask
# ----------------------------------------------------------------------
app = Flask(__name__)

# ----------------------------------------------------------------------
# Ruta “/” y alias “/index”.
# Devuelve la plantilla 'index.html' y pasa variables de contexto.
# ----------------------------------------------------------------------

# Filtros personalizados
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# Podríamos haber registrado nuestro filtro de esta forma:
# app.add_template_filter(today, "today")

# Funciones propias
def repeat(s, n):
    return s * n


from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    name = 'Angel'           # String a mostrar en la vista
    friends = ['Alexander', 'Roel', 'Juan', 'Pedro']    # Lista para el bucle
       # Renderizamos la plantilla. Flask + Jinja2 se encargan de la herencia.
    date = datetime.now()
    return render_template(
        'index.html',
        name=name,
        friends=friends,
        date=date,
        repeat=repeat
    )


# ----------------------------------------------------------------------
# Tres variantes de la ruta /hello:
#   • /hello           → “Hola Mundo”
#   • /hello/<name>    → Personalización con nombre
#   • /hello/<name>/<int:age> → Calcula el doble de la edad
# ----------------------------------------------------------------------
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name=None, age=None):
    if name is None and age is None:
        return '<h1>Hola Mundo!</h1>'
    elif age is None:
        return f'<h1>Hola, {name}!</h1>'
    else:
        return f'<h1>Hola, {name}! El doble de tu edad es {age * 2}!</h1>'

# ----------------------------------------------------------------------
# Ruta que muestra código “tal cual” escapado para evitar XSS
# ----------------------------------------------------------------------
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

# ----------------------------------------------------------------------
# Solo ejecuta la app cuando el archivo se lanza directamente
# (Útil para debug con `flask run` o `python hello.py`)
# ----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
