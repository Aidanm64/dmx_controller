from PyDMXControl.controllers import FTD2XXController
from PyDMXControl.controllers.utils.debug import Debugger
from PyDMXControl.profiles.Generic import Dimmer, RGB_Vdim
from PyDMXControl import Colors
from dmx_app import functs
from dmx_app.my_dmx import Spotlight

def run():

    dmx = FTD2XXController(0)

    #f = dmx.add_fixture(Spotlight, "spotlight", start_channel=1)
    #f.dim(255, 0, channel="base")
    #f.dim(255, 2000, channel="r")

    dimmers = []
    for i in range(8):
        #dimmers[i] = {}
        #dimmers[i]["r"] = dmx.add_fixture(Dimmer, f"dimmer_{i}_r", start_channel=1+3*i)
        #dimmers[i]["g"] = dmx.add_fixture(Dimmer, f"dimmer_{i}_g", start_channel=2+3*i)
        #dimmers[i]["b"] = dmx.add_fixture(Dimmer, f"dimmer_{i}_b", start_channel=3+3*i)
        dimmers.append(dmx.add_fixture(RGB_Vdim, name=f"dimmer_{i}", start_channel=1+3*i))
    dmx.web_control()
    dmx.sleep_till_enter()
    dmx.close()
