# script for numerical integration of the dimerisation example

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def funcp(y, t, p):  
    # R = y[0] 
    # R2 = y[1]

    # assign parameters
    k1 = p[0]
    k2 = p[1]

    dR = 2*k1*y[1] - 2*k2*y[0]*y[0]
    dR2 = -k1*y[1] + k2*y[0]*y[0]

    return [ dR, dR2 ]

def main():

    # define parameter vector
    theta = [0.01, 0.01]

    # define a new function that fixes the parameters
    def func(y, t):
        return funcp(y, t, theta)

    # define the time range that we want to integrate
    times = np.arange(0,10,0.1)
    
    # initial conditions
    y0 = [100, 0]

    # perform the ode integration
    yobs = odeint(func, y0, times)

    # make a plot
    plt.close()  # close any existing
   
    plt.plot( times, yobs[:,0], label='R' )
    plt.plot( times, yobs[:,1], label='R2' )
    plt.legend( loc=1 )

    plt.xlabel('time')
    plt.ylabel('concentration')
    plt.savefig('dimerisation.png')
    #plt.show() # display
    

main()

