

from flask import Flask

app = Flask(__name__)


@app.route("/global/color", method=['POST'])
def set_global_color():
    pass


@app.route("/fixtures", methods=['GET'])
def get_fixtures()
