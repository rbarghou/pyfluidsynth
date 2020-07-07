from functools import wraps


FLUID_OK = 0
FLUID_FAILED = -1


class PyFluidSynth2Exception(BaseException):
    pass


def check_result(result):
    if result == FLUID_FAILED:
        raise PyFluidSynth2Exception("FluidSynthFailure")
    else:
        return result
