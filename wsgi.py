
from dmx_app.web.web_controller import WebController
from dmx_app.service import DMXService
import time

service = DMXService()
service.load_universe("config/test_universe.yaml")

web_controller = WebController(dmx_service=service)

while True:
    try:
        time.sleep(0.001)
    except KeyboardInterrupt:
        break

service.dmx.close()