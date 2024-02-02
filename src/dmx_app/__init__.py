from PyDMXControl.controllers import FTDIController
from dmx_app import functs


def run():

    dmx = FTDIController("B002FETU")

    functs.colour_after_time(dmx)

    dmx.sleep_till_enter()
    dmx.close()
