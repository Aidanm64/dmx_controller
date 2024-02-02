from PyDMXControl.controllers import FTDIController
from PyDMXControl.controllers.utils.debug import Debugger
from dmx_app import functs


def run():

    dmx = FTDIController("B002FETU")
    debugger = Debugger(dmx,)

    functs.color_after_time(dmx)

    dmx.sleep_till_enter()
    dmx.close()
