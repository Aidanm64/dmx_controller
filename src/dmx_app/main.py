
from dmx_app.service import DMXService


def run():
    service = DMXService()
    service.load_universe("config/test_universe.yaml")

    service.dmx.web_control()
    service.dmx.sleep_till_enter()
    service.dmx.close()
