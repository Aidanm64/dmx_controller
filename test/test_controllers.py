
from PyDMXControl.controllers import FTDIController, FTD2XXController
from dmx_app.my_dmx import Spotlight

port = "B002FETU"


def do_dim(dmx):
    f = dmx.add_fixture(Spotlight, "spotlight", start_channel=1)
    f.dim(255, 0, channel="base")
    f.dim(255, 0, channel="base")

def test_ftdi_controller():
    dmx = FTDIController(port)
    dmx.close()

    


