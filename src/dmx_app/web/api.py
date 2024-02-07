


from flask import Blueprint, request, current_app

from dmx_app.service import DMXService
from dmx_app import Colors

api_routes = Blueprint("api", __name__, url_prefix="/")

service = DMXService()

@api_routes.route("/global/color/<color>", methods=['PUT'])
def set_global_color(color):
    color = getattr(Colors, color)
    current_app.parent.dmx_service.set_global_color(color)


@api_routes.route("/fixtures", methods=['GET'])
def get_fixtures():
    pass
