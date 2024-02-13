from PyDMXControl.controllers import FTD2XXController
from yaml import load, Loader
from dmx_app.fixtures import from_str


class DMXService:
    def __init__(self, dmx=FTD2XXController(0), universe_file="config/test_universe.yaml"):
        self.dmx = dmx
        self.fixtures = {}
        self.load_universe(universe_file)

    def set_all_color(self, color, ms=0):
        for key in self.fixtures:
            self.fixtures[key].color(color, int(ms))

    def set_all_intensity(self, intensity, ms=0):
        for key in self.fixtures:
            self.fixtures[key].dim(intensity, int(ms))

    def load_universe(self, path="/app/config/habitat_universe.yaml"):
        self.fixtures = {}
        with open(path, "r") as f:
            self.universe = load(f.read(), Loader=Loader)

        for name, fixture in self.universe['fixtures'].items():
            fixture_class = from_str(fixture['kind'])
            self.fixtures[name] = self.dmx.add_fixture(fixture_class, name=name, start_channel=fixture['start_channel'])

    def set_fixture_color(self, fixture_id, color, ms=None):
        self.fixtures[fixture_id].color(color, ms)

    def set_fixture_intensity(self, fixture_id, intensity, channel="dimmer", ms=None):
        self.fixtures[fixture_id].dim(intensity, ms=ms, channel=channel)

    def set_channel_value(self, channel_id, value):
        self.dmx.channels[channel_id].set(int(value))

    def to_dict(self):

        result = {
            "universe": self.universe['name'],
            "fixtures":{},
            "groups":{}
        }

        for f in self.fixtures:
            result['fixtures'][f.name] = f.json_data

        return result
