from PyDMXControl.profiles.defaults import Fixture
from PyDMXControl.controllers import SerialController


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
        self._register_channel('white')
        self._register_channel_aliases('white', 'w')
        self._register_channel('effect')
        self.dim(255, channel="base")
        self.dim(0, channel='effect')


class DMX:

    def __init__(self):
        self.controller = SerialController("COM3")

        self.fixture1 = self.controller.add_fixture(Spotlight, name="spot1", start_channel=1)
        #self.fixture2 = self.controller.add_fixture(Spotlight, name="spot1", start_channel=7)


    def set_value(self, channel, value):
        self.fixture1.dim(value, 0, channel)
        #self.fixture2.dim(255-value, 0, channel)

    def close(self):
        self.controller.close()