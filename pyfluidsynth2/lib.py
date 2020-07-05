import ctypes.util


Lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("fluidsynth"))
