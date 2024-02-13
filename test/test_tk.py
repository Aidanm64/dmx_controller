
from dmx_app.service import DMXService
from dmx_app.ui_tk import App

from PyDMXControl.controller import PrintController


def test_ui():
    dmx = PrintController()
    service = DMXService(dmx)
    app = App(dmx_service=service)
    app.start()
