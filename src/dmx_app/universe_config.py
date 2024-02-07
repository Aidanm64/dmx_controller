
import yaml


class Universe:
    def __init__(self, fixtures={}, groups={}):
        self.fixtures = fixtures
        self.groups = groups

    def load(self, file_path):
