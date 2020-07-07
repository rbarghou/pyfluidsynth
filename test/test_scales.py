import ctypes
import time

from pyfluidsynth2.driver import Driver
from pyfluidsynth2.exception import PyFluidSynth2Exception
from pyfluidsynth2.player import Player
from pyfluidsynth2.settings import Settings
from pyfluidsynth2.synth import Synth

CHANNEL = 1
SFID = 1
BANK = 1
PRESET_NUM = 60


def test_scales():
    with Settings({"audio.driver": "alsa"}) as settings:
        with Synth(settings) as synth:
            with Player(synth) as player:
                with Driver(settings, synth) as driver:
                    synth.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2", 1)

                    scale = [0, 4,  7, 12,]
                    scale = scale + list(reversed(scale))[1:]
                    programs = [10, 30, 59, 110, 120]
                    for channel, program in enumerate(programs):
                        synth.program_change(channel, program)

                    for channel, j in enumerate(scale):
                        for i in scale:
                            notes = [k + i for k in [60 + j, 67 + j,]]
                            for note in notes:
                                synth.note_on(channel, note, 100)
                            time.sleep(.25)

                            from pyfluidsynth2.lib import Lib
                            x = ctypes.c_int()

                            Lib.fluid_synth_pitch_bend(
                                synth.synth,
                                0,
                                ctypes.c_int(123)
                            )
                            Lib.fluid_synth_get_pitch_bend(
                                synth.synth,
                                0,
                                ctypes.byref(x)
                            )
                            print(x.value)


                            for note in notes:
                                try:
                                    synth.note_off(channel, note);
                                except PyFluidSynth2Exception as e:
                                    print(e)


if __name__ == "__main__":
    test_scales()