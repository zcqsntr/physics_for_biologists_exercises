# simulate the repressilator model
import time, numpy, string, csv

from scipy.integrate import odeint
from scipy.optimize import fsolve

def funcp(y,t,theta):
    m1=y[0]
    m2=y[1]
    m3=y[2]
    p1=y[3]
    p2=y[4]
    p3=y[5]

    #print "funcp", theta

    dy = [0,0,0,0,0,0]
    dy[0] = -m1 + theta[3]/(1 + pow(p3,theta[1]) ) + theta[0]
    dy[1] = -m2 + theta[3]/(1 + pow(p1,theta[1]) ) + theta[0]
    dy[2] = -m3 + theta[3]/(1 + pow(p2,theta[1]) ) + theta[0]
    dy[3] = -theta[2]*( p1 - m1 )
    dy[4] = -theta[2]*( p2 - m2 )
    dy[5] = -theta[2]*( p3 - m3 )

    return dy

t = numpy.arange(0,30.1,0.1)
y0 = [0,0,0,2,1,3]
theta_base = [1,2,5,10]


def jacobian( y, theta ):
    ret = numpy.zeros( [6,6] )
    ## fill in the non zero terms

    p1 = y[3]
    p2 = y[4]
    p3 = y[5]

    ret[0,0] = -1
    ret[1,1] = -1
    ret[2,2] = -1
    ret[3,3] = -theta[2]
    ret[4,4] = -theta[2]
    ret[5,5] = -theta[2]

    ret[3,0] = theta[2]
    ret[4,1] = theta[2]
    ret[5,2] = theta[2]

    ret[0,5] = -theta[3]/((1+p3)*(1+p3))
    ret[1,3] = -theta[3]/((1+p1)*(1+p1))
    ret[2,4] = -theta[3]/((1+p2)*(1+p2))
    return ret
    

fout = open('res.txt','w')

for ia in numpy.arange(1,100,1):

    theta = [theta_base[0],theta_base[1],theta_base[2],ia]

    y0 = [0,0,0,2,1,3]
    
    def func_int(y,t):
        return funcp(y,t,theta)
    y = odeint(func_int, y0, t, atol=0.001, rtol=0.001, hmax=1.0)
    ##print y[-1,:]

    def func_sol(y):
        return funcp(y,0,theta)

    v = fsolve(func_sol, y[-1,:], full_output=True)
    ss = v[0]
    ##print 'ss:', v[0]
    J = jacobian( ss, theta )
    e = numpy.linalg.eigvals(J)
    ##print J
    print(ia, numpy.real(e[0]),numpy.imag(e[0]), numpy.real(e[2]),numpy.imag(e[2]), numpy.real(e[4]), numpy.imag(e[4]))
    print(fout, ia, ss[0], numpy.real(e[0]),numpy.imag(e[0]))
