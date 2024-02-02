import time
from PyDMXControl.controllers import SerialController

from PyDMXControl.profiles.Generic import Dimmer, RGB_Vdim, Custom
from PyDMXControl import Colors

from PyDMXControl.profiles.defaults import Fixture

class Spotlight(Fixture):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._register_channel('base')
        self._register_channel('red')
        self._register_channel_aliases('red', 'r')
        self._register_channel('green')
        self._register_channel_aliases('green', 'g')
        self._register_channel('blue')
        self._register_channel_aliases('blue', 'b')
        self._register_channel('effects')
        self.dim(255, channel="base")
        self.dim(0, channel='effects')



def web(dmx):
    f1 = dmx.add_fixture(Dimmer, name="base", start_channel=1)
    f2 = dmx.add_fixture(Dimmer, name="red", start_channel=2)
    f3 = dmx.add_fixture(Dimmer, name="green", start_channel=3)
    f4 = dmx.add_fixture(Dimmer, name="blue", start_channel=4)
    f5 = dmx.add_fixture(Dimmer, name="white", start_channel=5)
    f6 = dmx.add_fixture(Dimmer, name="other", start_channel=6)
    dmx.web_control()


def vdim(dmx):
    f1 = dmx.add_fixture(Dimmer, name="base", start_channel=1)
    f1.dim(255, 255)
    rgb = dmx.add_fixture(RGB_Vdim, name="rgb", start_channel=2)
    rgb.color(Colors.Red, 1000)


def spotlight(dmx):
    f = dmx.add_fixture(Spotlight, start_channel=1)
    #f.color(Colors.Red, 5000)

    f.anim(4, )


def animate(dmx):
    f = dmx.add_fixture(Spotlight, start_channel=1)
    delay = 20

    r = [i for i in range(256)]
    b = [255-i for i in range(256)]
    g = [int(i/2) for i in range(256)]

    for i in range(10):
        for i in range(256):
            f.dim(r[i], 0, "r")
            f.dim(b[i], 0, "b")
            f.dim(g[i], 0, "g")
            dmx.sleep_ms(delay)




def color_after_time(dmx):
    f = dmx.add_fixture(Spotlight, start_channel=1)
    f.dim()

    f.color(Colors.Red, 1000)
    dmx.sleep_ms(2000)
    f.color(Colors.Green, 1000)
    dmx.sleep_ms(2000)
    f.color(Colors.Blue, 1000)



if __name__ == "__main__":
    dmx = SerialController("COM3")
    try:
        color_after_time(dmx)
    except KeyboardInterrupt:
        pass
    dmx.sleep_till_enter()
    dmx.close()
