from PyDMXControl.controllers import FTD2XXController
from PyDMXControl.controllers.utils.debug import Debugger
from dmx_app import functs
from dmx_app.my_dmx import Spotlight

def run():

    dmx = FTD2XXController(0)

    f = dmx.add_fixture(Spotlight, "spotlight", start_channel=1)
    f.dim(255, 0, channel="base")
    f.dim(255, 2000, channel="r")

    dmx.web_control()
    dmx.sleep_till_enter()
    dmx.close()
