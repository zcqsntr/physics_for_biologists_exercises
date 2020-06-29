# script for numerical integration of the dimerisation example
from numpy import *
import matplotlib.pyplot as plt

def func(t, p):  
    N0 = p[0]
    r0 = p[1]
    K  = p[2]    
    N = K*N0*exp(r0*t)/(K - N0 + N0*exp(r0*t))
    return N

# define the parameters
p = [10, 1, 1000]

# define the time range that we want to integrate
times = arange(0,10,0.1)
ntimes = len(times)

y = zeros([ntimes])
for i in range(ntimes):
    y[i] = func(times[i], p)
     
# make a plot
plt.plot( times, y, label='u' )
plt.xlabel('time')
plt.ylabel('number of cells')
plt.savefig('bacterial-growth.pdf')
plt.show()
        

