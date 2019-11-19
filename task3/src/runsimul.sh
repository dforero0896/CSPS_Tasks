#!/usr/bin/env bash
MD=/home/daniel/gdrive/EPFL/2019-2020/ComputerSimulation/Tasks/task2/MD
PWD=$(pwd)
WORKDIR=/home/daniel/gdrive/EPFL/2019-2020/ComputerSimulation/Tasks/task3/Task3/
$MD/md1.x < $WORKDIR/Step1_Startup/md_equil.in 
