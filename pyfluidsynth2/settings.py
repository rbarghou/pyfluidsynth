import ctypes

from pyfluidsynth2.lib import Lib


class Settings:
    def __init__(self, settings=None):
        self.settings = Lib.new_fluid_settings()
        if settings:
            for key, val in settings.items():
                self.set(key, val)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return Lib.delete_fluid_settings(self.settings)

    def set(self, key, val):
        if isinstance(key, str):
            key = key.encode()
        if isinstance(val, bytes):
            self.set_str(key, val)
        elif isinstance(val, str):
            self.set_str(key, val.encode())
        elif isinstance(val, int):
            self.set_int(key, val)
        elif isinstance(val, float):
            self.set_num(key, val)
        else:
            raise TypeError("val %s is not a valid type", val)

    def set_str(self, key: bytes, val: bytes) -> int:
        return Lib.fluid_settings_setstr(self.settings, key, val)

    def set_int(self, key: bytes, val: int) -> int:
        return Lib.fluid_settings_setint(self.settings, key, ctypes.c_int(val))

    def set_num(self, key: bytes, val: float) -> int:
        return Lib.fluid_settings_setnum(
            self.settings,
            key,
            ctypes.c_double(val)
        )

