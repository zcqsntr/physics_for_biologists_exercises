# script for numerical integration of the dimerisation example
from numpy import *
from scipy import *
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def funcp(y, t, p):  
   
    a1 = p[0]
    a2 = p[1]
    beta = p[2]
    gamma = p[3]
    
    du = -y[0] + a1/(1 + pow(y[1],beta))
    dv = -y[1] + a2/(1 + pow(y[0],gamma))

    return [ du, dv ]

def main():

    # define parameter vector
    theta = [10.0, 10.0, 2.0, 2.0]

    # define the time range that we want to integrate
    times = arange(0,10,0.1)
    
    y0_1 = [0.1, 1.0]
    yobs1 = odeint(funcp, y0_1, times, args = (theta,) )
    y0_2 = [5.0, 4.0]
    yobs2 = odeint(funcp, y0_2, times, args = (theta,) )
    
    # make a plot
    plt.close()  # close any existing
    plt.figure(num=1, figsize=(10,5))

    plt.subplot(121)
    plt.plot( times, yobs1[:,0], label='u' )
    plt.plot( times, yobs1[:,1], label='v' )
    plt.legend( loc=2 ) # loc=1 places at top right, loc=2 places at top left 
    plt.xlabel('time')
    plt.ylabel('concentration')

    plt.subplot(122)
    plt.plot( times, yobs2[:,0], label='u' )
    plt.plot( times, yobs2[:,1], label='v' )
    plt.legend( loc=2 ) # loc=1 places at top right, loc=2 places at top left 
    plt.xlabel('time')
    plt.ylabel('concentration')
    plt.show()
    plt.savefig('gardner-toggle-ts.png')
    #plt.show() # display


    # do some analysis
    x,info,ret,msg = fsolve(funcp, yobs1[-1,:], args = (0,theta,), full_output=True)
    if ret == 1:
        print(x)
    else:
        print(msg)
        
main()

