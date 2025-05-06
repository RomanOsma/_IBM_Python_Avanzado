from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'llave_secreta_123'

# Clase Cliente para manejo de datos
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')

# DAO para manejo de base de datos (simulado)
class ClienteDAO:
    clientes = []

    @classmethod
    def seleccionar(cls):
        return cls.clientes

    @classmethod
    def insertar(cls, cliente):
        if cliente.id is None:
            cliente.id = len(cls.clientes) + 1
        cls.clientes.append(cliente)
        return 1

    @classmethod
    def actualizar(cls, cliente):
        for i, c in enumerate(cls.clientes):
            if c.id == cliente.id:
                cls.clientes[i] = cliente
                return 1
        return 0

    @classmethod
    def eliminar(cls, cliente):
        for i, c in enumerate(cls.clientes):
            if c.id == cliente.id:
                del cls.clientes[i]
                return 1
        return 0

    @classmethod
    def seleccionar_por_id(cls, id):
        for c in cls.clientes:
            if c.id == id:
                return c
        return None

# Formulario WTForms
class ClienteForma(FlaskForm):
    id = HiddenField('Id')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia = IntegerField('Membresia', validators=[DataRequired()])
    guardar = SubmitField('Guardar')

# Ejemplos HTML
def ejemplo_html_basico():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Introducción a HTML</title>
    </head>
    <body>
        <h1>Bienvenido a HTML</h1>
        <p>Este es un ejemplo básico de una página HTML.</p>
    </body>
    </html>
    """
    with open('ejemplo_html_basico.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Ejemplo HTML básico creado en 'ejemplo_html_basico.html'")

def ejemplo_hola_mundo_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Mundo</title>
    </head>
    <body>
        <h1>Hola Mundo</h1>
    </body>
    </html>
    """
    with open('ejemplo_hola_mundo_html.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Ejemplo Hola Mundo HTML creado en 'ejemplo_hola_mundo_html.html'")

def ejemplo_links_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Links en HTML</title>
    </head>
    <body>
        <h1>Links en HTML</h1>
        <a href="https://www.google.com" target="_blank">Ir a Google</a>
    </body>
    </html>
    """
    with open('ejemplo_links_html.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Ejemplo Links HTML creado en 'ejemplo_links_html.html'")

# Ejemplos CSS
def ejemplo_css_interno():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Estilos Internos en CSS</title>
        <style>
            p {
                color: green;
            }
        </style>
    </head>
    <body>
        <h1>Estilos Internos en CSS</h1>
        <p>Este texto es verde debido a los estilos internos.</p>
    </body>
    </html>
    """
    with open('ejemplo_css_interno.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Ejemplo CSS Interno creado en 'ejemplo_css_interno.html'")

def ejemplo_css_externo():
    css_content = """
    p {
        color: red;
    }
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Estilos Externos en CSS</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>Estilos Externos en CSS</h1>
        <p>Este texto es rojo debido a los estilos externos.</p>
    </body>
    </html>
    """
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    with open('ejemplo_css_externo.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Ejemplo CSS Externo creado en 'ejemplo_css_externo.html' y 'styles.css'")

# Ejemplos Bootstrap
def ejemplo_bootstrap_basico():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Introducción a Bootstrap</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <h1 class="text-center">Introducción a Bootstrap</h1>
        <div class="container">
            <p class="text-primary">Este texto es azul (text-primary).</p>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """
    with open('ejemplo_bootstrap_basico.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Ejemplo Bootstrap Básico creado en 'ejemplo_bootstrap_basico.html'")

def ejemplo_tabla_bootstrap():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabla HTML con Bootstrap</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h2>Tabla de Clientes</h2>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Edad</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Juan Pérez</td>
                        <td>30</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Ana López</td>
                        <td>25</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """
    with open('ejemplo_tabla_bootstrap.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Ejemplo Tabla Bootstrap creado en 'ejemplo_tabla_bootstrap.html'")

# Ejemplos Flask
@app.route('/')
def inicio_flask():
    clientes = ClienteDAO.seleccionar()
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo='Zona Fit (GYM)', clientes=clientes, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar_cliente():
    cliente_forma = ClienteForma()
    if cliente_forma.validate_on_submit():
        cliente = Cliente(
            id=cliente_forma.id.data,
            nombre=cliente_forma.nombre.data,
            apellido=cliente_forma.apellido.data,
            membresia=cliente_forma.membresia.data
        )
        if cliente.id:
            ClienteDAO.actualizar(cliente)
        else:
            ClienteDAO.insertar(cliente)
        return redirect(url_for('inicio_flask'))
    return redirect(url_for('inicio_flask'))

@app.route('/limpiar')
def limpiar_formulario():
    return redirect(url_for('inicio_flask'))

@app.route('/editar/<int:id>')
def editar_cliente(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForma(cliente)
    return render_template('index.html', titulo='Zona Fit (GYM)', forma=cliente_forma)

@app.route('/eliminar/<int:id>')
def eliminar_cliente(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    if cliente:
        ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio_flask'))

# Menú principal
def main_menu():
    while True:
        print("\nMenú Principal:")
        print("1. Ejemplos HTML")
        print("2. Ejemplos CSS")
        print("3. Ejemplos Bootstrap")
        print("4. Ejemplos Flask")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            html_menu()
        elif choice == '2':
            css_menu()
        elif choice == '3':
            bootstrap_menu()
        elif choice == '4':
            flask_menu()
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Submenús
def html_menu():
    while True:
        print("\nEjemplos HTML:")
        print("1. HTML Básico")
        print("2. Hola Mundo HTML")
        print("3. Links en HTML")
        print("4. Regresar al Menú Principal")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            ejemplo_html_basico()
        elif choice == '2':
            ejemplo_hola_mundo_html()
        elif choice == '3':
            ejemplo_links_html()
        elif choice == '4':
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def css_menu():
    while True:
        print("\nEjemplos CSS:")
        print("1. CSS Interno")
        print("2. CSS Externo")
        print("3. Regresar al Menú Principal")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            ejemplo_css_interno()
        elif choice == '2':
            ejemplo_css_externo()
        elif choice == '3':
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def bootstrap_menu():
    while True:
        print("\nEjemplos Bootstrap:")
        print("1. Bootstrap Básico")
        print("2. Tabla con Bootstrap")
        print("3. Regresar al Menú Principal")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            ejemplo_bootstrap_basico()
        elif choice == '2':
            ejemplo_tabla_bootstrap()
        elif choice == '3':
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def flask_menu():
    print("\nPara ejecutar la aplicación Flask:")
    print("1. Asegúrate de tener Flask y Flask-WTF instalados")
    print("2. Ejecuta el script con 'python nombre_archivo.py'")
    print("3. Abre un navegador y ve a http://localhost:5000")
    input("\nPresiona Enter para regresar al Menú Principal...")

if __name__ == '__main__':
    print("Bienvenido al menú de ejemplos de desarrollo web")
    main_menu()