from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: '+ msg)
    
    send(msg, broadcast = True)

if __name__ == '__main__':
    socketio.run(app)
