import ctypes

from pyfluidsynth2.settings import Settings
from pyfluidsynth2.lib import Lib


class Synth:
    def __init__(self, settings: Settings):
        self.synth = Lib.new_fluid_synth(settings.settings)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return Lib.delete_fluid_synth(self.synth)

    def sf_load(self, sf2_path: str, reset_presets=True):
        return Lib.fluid_synth_sfload(
            self.synth,
            sf2_path.encode(),
            ctypes.c_int(reset_presets)
        )

    def set_gain(self, gain: float):
        return Lib.fluid_synth_set_gain(self.synth, ctypes.c_float(gain))

    def note_on(self, channel: int, key: int, velocity: int):
        return Lib.fluid_synth_noteon(
            self.synth,
            ctypes.c_int(channel),
            ctypes.c_int(key),
            ctypes.c_int(velocity)
        )

    def note_off(self, channel: int, key: int):
        return Lib.fluid_synth_noteoff(
            self.synth,
            ctypes.c_int(channel),
            ctypes.c_int(key),
        )
