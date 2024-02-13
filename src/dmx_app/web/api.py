import json
from flask import Blueprint, request, current_app, Response
from dmx_app import Colors

api_routes = Blueprint("api", __name__, url_prefix="/api")


@api_routes.route("/all", methods=['GET'])
def get_fixtures():
    body = current_app.parent.dmx_service.to_dict()
    return Response(json.dumps(body), status=200, mimetype="application/json")


@api_routes.route("/all/color/<color>", methods=['PUT'])
def set_all_color(color):
    color = getattr(Colors, color)
    print("Setting color:", color)
    ms = int(request.args.get("ms", 0))
    current_app.parent.dmx_service.set_all_color(color, ms)
    return "OK"


@api_routes.route("/all/color", methods=['PUT'])
def set_all_color_from_args():
    r = int(request.args.get('r', 0))
    g = int(request.args.get('g', 0))
    b = int(request.args.get('b', 0))
    w = int(request.args.get('w', 0))
    ms = int(request.args.get('ms', 0))
    print("Setting color:", [r, g, b, w])
    current_app.parent.dmx_service.set_all_color([r, g, b, w], ms)
    return 'OK'


@api_routes.route("/all/intensity/<int:intensity>", methods=['PUT'])
def set_all_intensity(intensity):
    print("Setting intensity:", intensity)
    ms = int(request.args.get("ms", 0))
    current_app.parent.dmx_service.set_all_intensity(int(intensity), ms)
    return "OK"


@api_routes.route("/all/state", methods=['POST', 'PUT'])
def set_state():
    state = request.get_json()
    for fixture_id, values in state.items():
        if values.get("color"):
            current_app.parent.dmx_service.set_fixture_color(fixture_id, values["color"], ms=values.get("ms", 0))
        if values.get("intensity"):
            current_app.parent.dmx_service.set_fixture_intensity(fixture_id, values["intensity"]["value"], ms=values.get("ms", 0))
    return "OK"


@api_routes.route("/fixtures/<fixture_id>", methods=['GET'])
def get_fixture(fixture_id):
    body = current_app.parent.dmx_service.fixtures[fixture_id].json_data
    return Response(json.dumps(body), status=200, mimetype="application/json")


@api_routes.route("/fixtures/<fixture_id>/intensity/<int:value>", methods=['PUT'])
def set_fixture_intensity(fixture_id, value):
    channel = request.args.get("channel", "dimmer")
    ms = int(request.args.get("ms", 0))
    current_app.parent.dmx_service.set_fixture_intensity(fixture_id, value, ms=ms, channel=channel)
    return "OK"


@api_routes.route("/fixtures/<fixture_id>/color", methods=['PUT'])
def set_fixture_color(fixture_id):
    r = int(request.args.get('r', 0))
    g = int(request.args.get('g', 0))
    b = int(request.args.get('b', 0))
    w = int(request.args.get('w', 0))
    ms = int(request.args.get('ms', 0))

    current_app.parent.dmx_service.set_fixture_color(fixture_id, [r, g, b, w], ms)

    return "OK"

