
from dmx_app.web.web_controller import WebController
from dmx_app.service import DMXService

service = DMXService()

web_controller = WebController(dmx_service=service)

service.dmx.sleep_till_enter()