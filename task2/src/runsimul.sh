#!/usr/bin/env bash
export PATH=/home/daniel/gdrive/EPFL/2019-2020/ComputerSimulation/Tasks/task2/MD:$PATH
MD=/home/daniel/gdrive/EPFL/2019-2020/ComputerSimulation/Tasks/task2/MD
PWD=$(pwd)
if [[ -e sample10.dat ]]; then
rm sample10.dat
fi
expect create_lattice.exp 1.7048 6 6 6 0.05 sample10.dat
$MD/md1.x < testrun.in