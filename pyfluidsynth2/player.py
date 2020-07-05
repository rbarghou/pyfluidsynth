from pyfluidsynth2.lib import Lib
from pyfluidsynth2.synth import Synth


class Player:
    def __init__(self, synth: Synth):
        self.player = Lib.new_fluid_player(synth.synth)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return Lib.delete_fluid_player(self.player)
