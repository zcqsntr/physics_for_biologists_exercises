# script for numerical integration of the dimerisation example

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(y, t, p):  
    # mX = y[0]   mRNA
    # X  = y[1]   protein

    # assign parameters
    k1 = p[0]
    k2 = p[1]
    d1 = p[2]
    d2 = p[3]
    
    dmX = k1 - d1*y[0]
    dX  = k2*y[0] - d2*y[1]

    return [ dmX, dX ]

def main():

    # define parameter vector
    theta = [5e-8, 10, 20, 2]

    # define the time range that we want to integrate
    times = np.arange(0,10,0.1)
    
    # initial conditions
    y0 = [0, 0]

    # perform the ode integration
    yobs = odeint(func, y0, times, args=(theta,), atol=1e-15  )

    # make a plot
    plt.close()  # close any existing
   
    plt.plot( times, yobs[:,0]/1e-9, label='mRNA' )
    plt.plot( times, yobs[:,1]/1e-9, label='protein' )
    plt.legend(loc=7)

    plt.xlabel('time (hours)')
    plt.ylabel('concentration (nM)')
    plt.savefig('plot-gene-expression.png')
    
main()

