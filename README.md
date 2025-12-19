These directories represent the implementation of the paper "ZShieldPQ: A Post-Quantum-Secure Multi-Party Computation for Zcash"
by Hannes Hacker, Shekoufeh Neisarian and Elif Bilge Kavun.

- "thesis_prototype_secuer_git_ceremony" holds the contents of the Git repositories utilized for the distributed SECUER generation protocol
- "thesis_prototypes_digital_signatures" holds the source code for the prototypes, benchmarks and contributions associated with the utilized digital signatures
- "benchmark_datasets" holds the benchmarking datasets for the ECDSA and Falcon implementation. It also provides scripts to display statistics on them. They can be recreated by utilizing the "thesis_prototypes_digital_signatures/test_compare_*.py" scripts.
- "PQClean" holds the PQClean Falcon-512 implementation for the "aarch64" architecture which we extended to accomodate the Public-Key-Recovery (PKR) mode. It also holds a benchmarking and a functionality testing script.

We provided a "README.md" in both directories to give an overview over content, setup and usage of them.
Other "README.md" are included, e.g. in the SECUER protocol tools, because we utilized already existing repositories.