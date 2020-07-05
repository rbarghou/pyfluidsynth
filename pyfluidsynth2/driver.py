from pyfluidsynth2.lib import Lib
from pyfluidsynth2.settings import Settings
from pyfluidsynth2.synth import Synth


class Driver:
    def __init__(self, settings: Settings, synth: Synth):
        self.driver = Lib.new_fluid_audio_driver(
            settings.settings,
            synth.synth
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return Lib.delete_fluid_audio_driver(self.driver)
