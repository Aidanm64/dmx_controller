from PyDMXControl.profiles.defaults import Fixture
from PyDMXControl.profiles.Generic import RGB_Vdim, Dimmer
import sys

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


def from_str(class_name):
    return getattr(sys.modules[__name__], class_name)