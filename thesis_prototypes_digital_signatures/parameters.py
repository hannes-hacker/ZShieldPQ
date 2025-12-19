from Crypto.Hash import SHAKE256, cSHAKE256, TurboSHAKE256, KangarooTwelve

default_hash_function = KangarooTwelve

XOF_numerical = {SHAKE256: 0, cSHAKE256: 1, TurboSHAKE256: 2, KangarooTwelve: 3}

benchmark_iterations = 2000

def hash_numerical():
    return XOF_numerical[default_hash_function]