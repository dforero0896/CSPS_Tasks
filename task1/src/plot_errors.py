#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import sys
methods = ["harmosc_euler", "harmosc_euler_improved", "harmosc_pc", "harmosc_verlet"]
N_steps = np.arange(3, 100, 5)
abs_errors = np.zeros((len(N_steps), len(methods)))
drift_errors = np.copy(abs_errors)
rms_errors = np.copy(abs_errors)
for j, method in enumerate(methods):
    sys.stdout.write('Computing with method %s...'%method)
    for i, N in enumerate(N_steps):
        output = subprocess.check_output("python compute_error.py %s 0 %i 0"%(method, N), shell=True)
        split_output = np.array(output.split()).astype(float)
        abs_errors[i,j] = split_output[0]
        drift_errors[i,j] = split_output[2]
        rms_errors[i,j] = split_output[3]
    sys.stdout.write("\t\tDone.\n")
plt.figure()
[plt.plot(N_steps, abs_errors[:,m], label = methods[m], lw=4) for m in range(len(methods))]
plt.title("Absolute error")
plt.legend()
plt.ylim(0,5)
plt.gcf()
plt.savefig("../results/abserr.png")

plt.figure()
[plt.plot(N_steps, drift_errors[:,m], label = methods[m], lw= 4) for m in range(len(methods))]
plt.title("Drift error")
plt.legend()
plt.ylim(0,5)
plt.gcf()
plt.savefig("../results/drifterr.png")

plt.figure()
[plt.plot(N_steps, rms_errors[:,m], label = methods[m], lw =4) for m in range(len(methods))]
plt.title("RMS error")
plt.legend()
plt.ylim(0,5)
plt.gcf()
plt.savefig("../results/rmserr.png")
