import ctypes
import time

from pyfluidsynth2.driver import Driver
from pyfluidsynth2.lib import Lib
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
                    synth.sf_load("/usr/share/sounds/sf2/FluidR3_GM.sf2", 1)


                    scale = [0, 4,  7, 12,]
                    scale = scale + list(reversed(scale))[1:]

                    for j in scale:
                        Lib.fluid_synth_program_change(
                            synth.synth,
                            ctypes.c_int(CHANNEL),
                            ctypes.c_int(PRESET_NUM + j)
                        )
                        for i in scale:
                            notes = [k + i for k in [60 + j, 67 + j, 75 + j]]
                            for note in notes:
                                synth.note_on(CHANNEL, note, 100)
                            time.sleep(.25)

                            for note in notes:
                                synth.note_off(CHANNEL, note);
