# Chat local básico con Flask

![Python Flask](static/img/flask.png)

## Contenido

* [Descripción del proyecto](#Descripción)
* [Instalación de paquetes](#Instalación)

## Descripción

Desarrollo de un chat web básico utilizando el framework **Flask** escrito en _**Python**_ y **HTML.**

* [Flask:][1] Framework escrito en Python para la creación de manera sencilla aplicaicones web bajo el patron **MVC.**

* [Python:][2] Lenguaje de programación de alto nivel multiplataforma.

* [MVC][3] Es un patrón de desarrollo que permite diferenciar y separar el modelo de datos **(Base de datos),** la vista **(página HTML)** y el controlador **(donde se gestionan las peticiones de la App Web).**

[1]: https://flask.palletsprojects.com/en/1.1.x/
[2]: https://www.python.org
[3]: https://codigofacilito.com/articulos/mvc-model-view-controller-explicado

## Instalación

Instala y actualiza usando [pip:][1]

[1]: https://pip.pypa.io/en/stable/quickstart/

`pip install flask`

`pip install flask-socketio`

## Ejemplo

```Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

## Tutorial

```Python
from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send
#Inicializar flask/servidor web
app = Flask(__name__)
app.config['SECRET_KEY']= 'secret!'
socketio = SocketIO(app)
#Definir rutas de los arvhivos
@app.route('/')
def index():
    return render_template('index.html')
#Escucha de eventos
@socketio.on('message')
def handleMessage(msg):
    print('Message: '+ msg)
    #Reenviar mensaje a todos los clientes
    send(msg, broadcast = True)
#iniciar servidor
if __name__ == '__main__':
    socketio.run(app)
```