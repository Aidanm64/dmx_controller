
from PyDMXControl.controllers import FTDIController, PrintController, FTD2XXController, SerialController, OpenDMXController
from dmx_app.my_dmx import Spotlight

port = "B002FETU"


def do_dim(dmx):
    f = dmx.add_fixture(Spotlight, "spotlight", start_channel=2)
    f.dim(255, 0, channel="base")
    f.dim(255, 2000, channel="r")
    dmx.sleep_ms(2000)

def test_ftdi_controller():
    dmx = FTDIController(port)
    do_dim(dmx)
    dmx.close()
    assert 0


def test_print_controller():

    dmx = PrintController()
    do_dim(dmx)
    dmx.close()
    assert 0

def test_ftd2xx_controller():
    dmx = FTD2XXController(port)
    do_dim(dmx)
    dmx.close()
    assert 0

def test_opendmx_controller():
    dmx = OpenDMXController()
#def test_serial_controller():
#    dmx = SerialController(port)

#    do_dim(dmx)

#    dmx.sleep(5000)
#    dmx.close()
#    assert 0 


