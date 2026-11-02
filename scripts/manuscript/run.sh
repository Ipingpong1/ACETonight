#!/bin/bash
# Launcher: single-threaded BLAS/OpenMP (forked lavaan workers otherwise oversubscribe the 16 cores), then Rscript.
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 GOTO_NUM_THREADS=1
cd /home/mo2273 || exit 1
exec /home/mo2273/ace_r_env/bin/Rscript "$@"
