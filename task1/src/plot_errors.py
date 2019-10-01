#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import sys
if len(sys.argv) != 2:
    sys.stdout.write("ERROR:\tUnexpected number of arguments.\nUSAGE:\t%s DAMPED\n"%sys.argv[0])
    sys.exit(1)
methods = ["harmosc_euler", "harmosc_euler_improved", "harmosc_pc", "harmosc_verlet"]
if int(sys.argv[1]):
    name='damp'
    methods = [name+m for m in methods]
else:
    name=''
N_steps = np.arange(10, 100, 5)
abs_errors = np.zeros((len(N_steps), len(methods)))
drift_errors = np.copy(abs_errors)
rms_errors = np.copy(abs_errors)
for j, method in enumerate(methods):
    sys.stdout.write('Computing with method %s...'%method)
    for i, N in enumerate(N_steps):
        output = subprocess.check_output("python compute_error.py %s 0 %i 0 1"%(method, N), shell=True)
        split_output = np.array(output.split()).astype(float)
        abs_errors[i,j] = split_output[0]
        drift_errors[i,j] = split_output[2]
        rms_errors[i,j] = split_output[3]
    sys.stdout.write("\t\tDone.\n")
plt.figure()
[plt.loglog(N_steps, abs_errors[:,m], label = methods[m], lw=4) for m in range(len(methods))]
plt.title("Absolute error")
plt.legend()
plt.gcf()
plt.savefig("../results/abserr%s.png"%name)

plt.figure()
[plt.loglog(N_steps, drift_errors[:,m], label = methods[m], lw= 4) for m in range(len(methods))]
plt.title("Drift error")
plt.legend()
plt.gcf()
plt.savefig("../results/drifterr%s.png"%name)

plt.figure()
[plt.loglog(N_steps, rms_errors[:,m], label = methods[m], lw =4) for m in range(len(methods))]
plt.title("RMS error")
plt.legend()
plt.gcf()
plt.savefig("../results/rmserr%s.png"%name)
