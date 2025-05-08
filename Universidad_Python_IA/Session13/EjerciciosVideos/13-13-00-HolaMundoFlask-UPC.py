from flask import Flask

app = Flask(__name__)


@app.route('/')  # url: http://localhost:5000/
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    return '<p>Hola Mundo</p>'

if __name__ == '__main__':
    app.run(debug=True)
