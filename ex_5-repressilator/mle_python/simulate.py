# simulate the repressilator model

from scipy.integrate import ode

import numpy


# theta = { alpha0, n, beta, alpha }

def funcp(y,t,theta):
    m1=y[0]
    p1=y[1]
    m2=y[2]
    p2=y[3]
    m3=y[4]
    p3=y[5]

    dy = [0,0,0,0,0,0]
    dy[0] = -m1 + theta[3]/(1 + pow(p3,theta[1]) ) + theta[0]
    dy[1] = -theta[2]*( p1 - m1 )
    dy[2] = -m2 + theta[3]/(1 + pow(p1,theta[1]) ) + theta[0]
    dy[3] = -theta[2]*( p2 - m2 )
    dy[4] = -m3 + theta[3]/(1 + pow(p2,theta[1]) ) + theta[0]
    dy[5] = -theta[2]*( p3 - m3 )

    #print 'alg:', dy

    return dy

def main():
    t = numpy.arange(0,51,1)

    def func(t,y):
        theta = [1,2,5,1000]
        return funcp(y,t,theta) 

    y0 = [0,2,0,1,0,3]

    r = ode(func).set_integrator('vode', with_jacobian=False).set_initial_value(y0, t[0])
    dt = 0.1
    
    for i in range(1,len(t)):
        while r.successful() and r.t < t[i]:
            r.integrate(r.t+dt)
        print(r.t, r.y)

    #def func(y,t):
    #    theta = [1,2,5,1000]
    #    return funcp(y,t,theta)

    #y = odeint(func, y0, t)
    #fout = open('sims.txt','w')
    #for j in range(len(t)):
    #    print >>fout, t[j], y[j,0], y[j,2], y[j,4]
    #fout.close()

main()

