

from flask import Flask, request

from dmx_app.service import DMXService
from dmx_app import Colors

app = Flask(__name__)

service = DMXService()


@app.route("/global/color/<str:color>", method=['PUT'])
def set_global_color(color):
    color = getattr(Colors, color)
    service.set_global_color(color)


@app.route("/fixtures", methods=['GET'])
def get_fixtures():
    pass


if __name__ == "__main__":
    app.run("localhost", port=8000, debug=True)