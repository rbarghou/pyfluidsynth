from ctypes import byref, c_int, c_double, c_float

from pyfluidsynth2.exception import check_result
from pyfluidsynth2.settings import Settings
from pyfluidsynth2.lib import Lib


class Synth:
    def __init__(self, settings: Settings):
        self.synth = Lib.new_fluid_synth(settings.settings)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        check_result(Lib.delete_fluid_synth(self.synth))

    def get_settings(self):
        # TODO: Must be implemented in conjunction with settings class
        pass

    def set_gain(self, gain: float):
        check_result(
            Lib.fluid_synth_set_gain(
                self.synth,
                c_float(gain))
        )

    def note_on(self, chan: int, key: int, vel: int):
        check_result(Lib.fluid_synth_noteon(
            self.synth,
            c_int(chan),
            c_int(key),
            c_int(vel)
        ))

    def note_off(self, channel: int, key: int):
        check_result(Lib.fluid_synth_noteoff(
            self.synth,
            c_int(channel),
            c_int(key),
        ))

    def cc(self, chan: int, ctrl: int, val: int):
        check_result(Lib.fluid_synch_cc(
            self.synth,
            c_int(chan),
            c_int(ctrl),
            c_int(val),
        ))

    def get_cc(self, chan: int, ctrl: int):
        val = c_int()
        check_result(
            Lib.fluid_synth_get_cc(
                self.synth,
                c_int(chan),
                c_int(ctrl),
                byref(val)
            )
        )
        return val.value

    def sysex(self):
        # TODO: investigate function more before implementing
        pass

    def pitch_bend(self, chan: int, val: int):
        check_result(
            Lib.fluid_synth_pitch_bend(
                self.synth,
                c_int(chan),
                c_int(val)
            )
        )

    def get_pitch_bend(self, chan: int):
        pitch_bend = c_int()
        check_result(
            Lib.fluid_synth_get_pitch_bend(
                self.synth,
                c_int(chan),
                byref(pitch_bend)
            )
        )
        return pitch_bend.value

    def pitch_wheel_sens(self, chan: int, val: int):
        check_result(
            Lib.fluid_synth_pitch_wheel_sens(
                self.synth,
                c_int(chan),
                c_int(val)
            )
        )
    
    def get_pitch_wheel_sens(self, chan: int):
        val = c_int()
        check_result(
            Lib.fluid_synth_get_wheel_sens(
                self.synth,
                c_int(chan),
                byref(val)
            )
        )

    def program_change(self, channel, preset_num):
        check_result(
            Lib.fluid_synth_program_change(
                self.synth,
                c_int(channel),
                c_int(preset_num)
            )
        )

    def channel_pressure(self, chan: int, val: int):
        check_result(
            Lib.fluid_synth_channel_pressure(
                self.synth,
                c_int(chan),
                c_int(val)
            )
        )

    def key_pressure(self, chan: int, key: int, val: int):
        check_result(
            Lib.fluid_synth_key_pressure(
                self.synth,
                c_int(chan),
                c_int(key),
                c_int(val)
            )
        )

    def bank_select(self, chan: int, bank: int):
        check_result(
            Lib.fluid_synth_bank_select(
                self.synth,
                c_int(chan),
                c_int(bank)
            )
        )

    def sfont_select(self, chan: int, sfont_id: int):
        check_result(
            Lib.fluid_synth_sfont_select(
                self.synth,
                c_int(chan),
                c_int(sfont_id)
            )
        )

    def program_select(
            self,
            chan: int,
            sfont_id: int,
            bank_num: int,
            preset_num: int
    ):
        check_result(
            Lib.fluid_synth_program_select(
                self.synth,
                c_int(chan),
                c_int(sfont_id),
                c_int(bank_num),
                c_int(preset_num)
            )
        )

    def program_select_by_sfont_name(
            self,
            chan: int,
            sfont_name: str,
            bank_num: int,
            preset_num: int
    ):
        check_result(
            Lib.fluid_synth_program_select_by_sfont_name(
                self.synth,
                c_int(chan),
                sfont_name.encode(),
                c_int(bank_num),
                c_int(preset_num)
            )
        )

    def get_program(self, chan: int):
        sfont_id = c_int()
        bank_num = c_int()
        preset_num = c_int()
        check_result(
            Lib.fluid_synth_get_program(
                self.synth,
                c_int(chan),
                byref(sfont_id),
                byref(bank_num),
                byref(preset_num)
            )
        )
        return sfont_id.value, bank_num.value, preset_num.value

    def unset_program(self, chan: int):
        check_result(
            Lib.fluid_synth_unset_program(
                self.synth,
                c_int(chan)
            )
        )

    def program_reset(self):
        check_result(
            Lib.fluid_synth_program_reset(
                self.synth
            )
        )

    def system_reset(self):
        check_result(
            Lib.fluid_synth_system_reset(
                self.synth
            )
        )

    def all_notes_off(self, chan: int):
        check_result(
            Lib.fluid_synth_all_notes_off(
                self.synth,
                c_int(chan)
            )
        )

    def all_sounds_off(self, chan: int):
        check_result(
            Lib.fluid_synth_all_sounds_off(
                self.synth,
                c_int(chan)
            )
        )

    def set_channel_type(self, chan: int, _type: int):
        check_result(
            Lib.fluid_synth_set_channel_type(
                self.synth,
                c_int(chan),
                c_int(_type)
            )
        )

    def get_channel_preset(self, chan: int):
        # TODO: implement after examining return types
        pass

    def start(self):
        # TODO: implement after examining use cases and types
        pass

    def stop(self):
        # TODO: implement after examining use cases and types
        pass

    def sfload(self, sf2_path: str, reset_presets=True):
        check_result(Lib.fluid_synth_sfload(
            self.synth,
            sf2_path.encode(),
            c_int(reset_presets)
        ))

