from flask import Flask
from flask_socketio import SocketIO
from dmx_app.service import DMXService

app = Flask(__name__)

socket = SocketIO(app)

service = DMXService()

@socket.on('message')
def handle_message(data):
    data = data
    for f_id, f in data['fixtures'].items():
        service.set_fixture_color(f_id, f['color'], ms=f.get("ms", 0))


if __name__ == "__main__":
    app.run("0.0.0.0", 8001, debug=True)