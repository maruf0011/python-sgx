from sgx.sealing import sealing_swig
from sgx.sealing.sealing_swig import *


def seal(secret, plain_text=bytes()):
    return sealing_swig.seal(secret, len(secret), plain_text, len(plain_text))
