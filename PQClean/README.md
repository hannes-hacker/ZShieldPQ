# Description
This repository represents the implementation and contribution based on the Falcon-512 implementation of the PQClean project.

We extracted the Falcon-512 code for the "aarch64" architecture out of the GitHub repository (https://github.com/PQClean/PQClean)
and extended it to accomodate the Public-Key-Recovery (PKR) mode, a benchmarking script (inspired by the "libsecp256k1" implementation (https://github.com/bitcoin-core/secp256k1)
we compared it to in the paper) and a basic functionality test.

## Scripts
The benchmarking script is located under "PQClean/aarch/benchmark_falcon.c".
The functionality test script is located under "test_function.c".

## Contributions
We implemented the Public-Key-Recovery (PKR) mode where we had to make adjustments in the code.
Those adjustments are pointed out in the following and can be looked at in detail in the code.

- PQClean/aarch/api.h
    - line 10: PQCLEAN_FALCON512_AARCH64_CRYPTO_BYTES_PKR
    - line 15: PQCLEAN_FALCONPADDED512_AARCH64_CRYPTO_BYTES_PKR
    - line 42: PQCLEAN_FALCON512_AARCH64_crypto_sign_signature_pkr
    - line 68: PQCLEAN_FALCON512_AARCH64_crypto_sign_verify_pkr_recover

- PQClean/aarch/inner.h
    - line 139: "Note that all additions with suffix "_pkr" are made by us."
    - line 168: PQCLEAN_FALCON512_AARCH64_comp_encode_pkr
    - line 177: PQCLEAN_FALCON512_AARCH64_comp_decode_pkr
    - line 801: PQCLEAN_FALCON512_AARCH64_sign_dyn_pkr

- PQClean/aarch/codec.c
    - line 386: PQCLEAN_FALCON512_AARCH64_comp_encode_pkr
    - line 545: PQCLEAN_FALCON512_AARCH64_comp_decode_pkr

- PQClean/aarch/pqclean.c
    - line 211: do_sign_pkr
    - line 385: do_verify_pkr_recover
    - line 491: PQCLEAN_FALCON512_AARCH64_crypto_sign_verify_pkr_recover
    - line 506: PQCLEAN_FALCON512_AARCH64_crypto_sign_signature_pkr

- PQClean/aarch/sign.c
    - line 955: do_sign_dyn_pkr
    - line 1144: PQCLEAN_FALCON512_AARCH64_sign_dyn_pkr

# Setup
For executing the scripts we added a Makefile which can be utilized as following:
    - install "make"
    - install "gcc"
    - change the first filename of "SOURCES"/"OBJECTS" to either "test_function.c"/"test_function.out" or "benchmark_falcon.c"/"benchmark_falcon.out"
    - change directory in the terminal to "PQClean/aarch64"
    - type "make" into the terminal
    - type "./benchmark_falcon.out" or "./test_function.out" into the terminal (depending on what file you created through the Makefile)