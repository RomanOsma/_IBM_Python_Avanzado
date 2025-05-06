from flask import Flask, render_template, redirect, url_for

from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_forma import ClienteForma

app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave_secreta_123'

titulo_app = 'Zona Fit (GYM)'

@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html')  # url http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    # Recuperamos los clientes de la bd
    clientes_db = ClienteDAO.seleccionar()
    # Creamos un objeto de cliente form vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db,
                           forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    # Creamos los objetos de cliente inicialmente objetos vacios
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    if cliente_forma.validate_on_submit():
        # Llenamos el objeto cliente con los valores del formulario
        cliente_forma.populate_obj(cliente)
        # Guardamos el nuevo cliente en la bd
        ClienteDAO.insertar(cliente)
    # Redireccionar a la pagina de inicio
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
