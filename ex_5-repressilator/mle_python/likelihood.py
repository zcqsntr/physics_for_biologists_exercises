# simulate the repressilator model
import numpy
from scipy.optimize import fmin
from scipy.integrate import ode

# theta = { alpha0, n, beta, alpha }
# true values are {1,2,5,1000}

# assumes we have data on m1,m2,m3
# data is 3x16 matrix

def dnorm(p,mean,scale):
    x = numpy.exp( -0.5*(p-mean)*(p-mean)/(scale*scale) )
    x = x/( scale*numpy.sqrt(2*numpy.pi) )
    return x

def funcp(y,t,theta):
    m1=y[0]
    p1=y[1]
    m2=y[2]
    p2=y[3]
    m3=y[4]
    p3=y[5]

    #print "funcp", theta

    dy = [0,0,0,0,0,0]
    dy[0] = -m1 + theta[3]/(1 + pow(p3,theta[1]) ) + theta[0]
    dy[1] = -theta[2]*( p1 - m1 )
    dy[2] = -m2 + theta[3]/(1 + pow(p1,theta[1]) ) + theta[0]
    dy[3] = -theta[2]*( p2 - m2 )
    dy[4] = -m3 + theta[3]/(1 + pow(p2,theta[1]) ) + theta[0]
    dy[5] = -theta[2]*( p3 - m3 )

    return dy

def integrate_repressilator( theta ):
    t = [ 0, 3.3, 6.6, 9.9, 13.2, 16.5, 19.8, 23.1, 26.4, 29.7, 33, 36.3, 39.6, 42.9, 46.2, 49.5 ]
    y0 = [0,2,0,1,0,3]

    #def func(y,t):
    #    return funcp(y,t,theta) 
    #y = odeint(func, y0, t, atol=0.001, rtol=0.001, hmax=1.0)

    def func(t,y):
        return funcp(y,t,theta)
    r = ode(func).set_integrator('vode', method='bdf', order=15, nsteps=3000).set_initial_value(y0, t[0])
    dt = 1.0
    res = numpy.zeros([16,3])
    res[0,:] = [y0[0], y0[2], y0[4]]
    for i in range(1,16):
        while r.successful() and r.t < t[i]:
            r.integrate(r.t+dt)
        res[i,:] = [r.y[0], r.y[2], r.y[4]]

    return res

def logL(theta, data):

    #print "logL", theta
    x = integrate_repressilator( theta[0:4] )

    logL = 0
    for j in range(16):
        logL += dnorm( data[j,0], mean=x[j,0], scale=theta[4] )
        logL += dnorm( data[j,1], mean=x[j,1], scale=theta[4] )
        logL += dnorm( data[j,2], mean=x[j,2], scale=theta[4] )
    return logL

def main():
    # read the data
    d = numpy.zeros([3,16])
    fin = open('../abc-sysbio-ana/simulated_data.txt','r')
    sp = 0
    
    for line in fin.readlines():
        l = line.split()
        for j in range(16):
            d[sp,j] = float(l[j])
        sp+= 1
    fin.close()

    d = numpy.transpose(d)
    ##x0 = [0.9,2.1,4.9,1001,1.1]

    def do_single_scan(p,min, max, delta, fname):
        fout = open(fname,'w')
        for i in numpy.arange(min,max,delta):
            theta = [ 1 , 2, 5, 1000, 1 ]
            theta[p] = i
            #print >>fout, i, logL(theta, d)
            print >>fout, i, numpy.exp(logL(theta,d))
        fout.close()

    do_single_scan(0, 0.0, 10, 0.01, "single_scan_alpha0.txt")
    do_single_scan(1, 1.0, 10, 0.01, "single_scan_n.txt")
    do_single_scan(2, 1.0, 20.0, 0.01, "single_scan_beta.txt")
    do_single_scan(3, 500, 2000, 1, "single_scan_alpha.txt")
    #do_single_scan(4, 0.1, 1.5, 0.01, "single_scan_var.txt")
    
    def do_double_scan(p1, min1, max1, delta1, p2, min2, max2, delta2, fname):
        fout = open(fname,'w')
        for i in numpy.arange(min1,max1,delta1):
            for j in numpy.arange(min2,max2,delta2):
                theta = [ 1, 2, 5, 1000, 1 ]
                theta[p1] = i
                theta[p2] = i
                print(fout, i, j, logL(theta, d))
        fout.close()

    ## do minimisation
    def funcmin(param):
            return logL(param,d)

    if 0:
        start = [1.0, 2.0, 5.0, 1000, 2.0]
        obj = fmin( func=funcmin, x0=start, xtol=1.0, ftol=1.0, maxiter=10000, maxfun=10000, full_output=True)#,disp=True, retall=True )
        print(obj[4], obj[1], obj[0])

    if 0:
        ntry = 2
        res = numpy.zeros([ntry,7])
        for j in range(ntry):
            start = [ numpy.random.uniform(0,2),
                      numpy.random.uniform(0,10),
                      numpy.random.uniform(0,20),
                      numpy.random.uniform(500,1500),
                      numpy.random.uniform(0.5,3.0) ]

            obj = fmin( func=funcmin, x0=start, xtol=1.0, ftol=1.0, maxiter=10000, maxfun=10000, full_output=True)#,disp=True, retall=True )
            print(obj)
            res[j,0] = obj[4]
            res[j,1] = obj[1]
            res[j,2:7] = obj[0]

        for i in range(ntry):
            for j in range(7):
                print(res[i,j])
            print("")
        
main()

