

from dmx_app.service import DMXService
from dmx_app import Colors
import time


def test_load_config():
    service = DMXService()
    service.load_universe("config/test_universe.yaml")
    service.set_all_color(Colors.Red)
    service.set_all_intensity(128, 3000)

    for i in range(100):
        time.sleep(0.1)
