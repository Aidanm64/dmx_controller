from PyDMXControl.controllers import FTD2XXController
from yaml import load, Loader
from dmx_app.fixtures import from_str


class DMXService:
    def __init__(self, dmx=FTD2XXController(0)):
        self.dmx = dmx
        self.fixtures = {}

    def set_global_color(self, color, ms=0):
        for fixture in self.fixtures:
            fixture.color(color, ms)

    def load_universe(self, path="/app/config/habitat_universe.yaml"):
        with open(path, "r") as f:
            universe_obj = load(f.read(), Loader=Loader)

        for name, fixture in universe_obj['fixtures'].items():
            fixture_class = from_str(fixture['kind'])
            self.fixtures[name] = self.dmx.add_fixture(fixture_class, name=name, start_channel=fixture['start_channel'])
