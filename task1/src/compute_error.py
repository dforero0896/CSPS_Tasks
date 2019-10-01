#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from scipy import stats
if len(sys.argv)!= 6:
    sys.stdout.write("ERROR:\tUnexpected number of arguments.\nUSAGE:\t%s CPPNAME COMPILE NSTEPS SHOWPLOT SHOWANALYTIC\n"%sys.argv[0])
    sys.exit(1)
N_steps = sys.argv[3]
if int(sys.argv[2]):
    os.system('g++ -o ../bin/%s.o %s.cpp'%(sys.argv[1], sys.argv[1]))
os.system('../bin/%s.o %s > ../results/%s.csv'%(sys.argv[1], N_steps, sys.argv[1]))
data = np.loadtxt('../results/%s.csv'%sys.argv[1], delimiter = ',', dtype = float, skiprows=1)
energy = data[:,1]**2 + data[:,2]**2
energy_a = data[:,3]**2 + data[:,4]**2
if int(sys.argv[4]):
    plt.plot(data[:,0], data[:,1], label = 'Position')
    plt.plot(data[:,0], data[:,2], label = 'Momentum')
    plt.plot(data[:,0], energy , label = 'Energy')
    if int(sys.argv[5]):
        plt.plot(data[:,0], data[:,3], label = 'Position-A')
        plt.plot(data[:,0], data[:,4], label = 'Momentum-A')
        plt.plot(data[:,0], energy_a, label = 'Energy-A')
    plt.legend(loc=0)
    plt.show()
# Compute absolute error
abs_err_pos = max(abs(data[:,1] - data[:,3])) #in position
abs_err_mom = max(abs(data[:,2] - data[:,4])) #in momentum
# Compute drift of Energy
slope, intercept, r_value, p_value, std_err = stats.linregress(data[:,0], energy)
# Compute RMS error
def fit_e(t):
    return slope * t + intercept
n = len(data[:,0])
rms_error_energy = np.sqrt((1./(n-2)) * sum((energy - fit_e(data[:, 0]))**2))
print("%.3f %.3f %.3f %.3f"%(abs_err_pos, abs_err_mom, slope, rms_error_energy))
