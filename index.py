from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send
#Inicializar flask/servidor web
app = Flask(__name__)
app.config['SECRET_KEY']= 'secret!'
socketio = SocketIO(app)
#Definir ruats de los arvhivos
@app.route('/')
def index():
    return render_template('index.html')
    #return "Helle World"
#Escucha de eventos
@socketio.on('message')
def handleMessage(msg):
    print('Message: '+ msg)
    #Reenviar mensaje a todos los clientes
    send(msg, broadcast = True)
#iniciar servidor
if __name__ == '__main__':
    socketio.run(app)
