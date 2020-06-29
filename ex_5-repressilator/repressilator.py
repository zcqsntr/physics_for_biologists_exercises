
import numpy as np

from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def repressilator(y, t, alpha0, alpha, beta, n):
    m1 = -y[0] + alpha / (1 + y[5] ** n) + alpha0
    p1 = -beta * (y[1] - y[0])
    m2 = -y[2] + alpha / (1 + y[1] ** n) + alpha0
    p2 = -beta * (y[3] - y[2])
    m3 = -y[4] + alpha / (1 + y[3] ** n) + alpha0
    p3 = -beta * (y[5] - y[4])

    ydot = [m1, p1, m2 ,p2, m3, p3]
    return ydot


alpha0 = 1
n = 2.0
beta = 5
alpha = 1000

# steady state solutions
times = np.arange(0, 15, 0.01)
y0 = [0,1,0,1,0,1]

y = odeint(repressilator, y0, times, args = (alpha0, alpha, beta, n))
plt.figure()
plt.plot(times, y[:,0], label = '$m_1$')
plt.plot(times, y[:,1], label = '$p_1$')

plt.plot(times, y[:,2], label = '$m_2$')
plt.plot(times, y[:,3], label = '$p_2$')

plt.plot(times, y[:,4], label = '$m_3$')
plt.plot(times, y[:,5], label = '$p_3$')
plt.legend()
plt.ylabel('Amount')
plt.xlabel('Time')
plt.savefig('repr_ss.png')

plt.figure()
plt.plot(y[:,0], y[:,1])
plt.xlabel('Amount $m_1$')
plt.ylabel('Amount $p_1$')
plt.savefig('repr_ss_phase.png')


#oscillatory solutions
y0 = [0,1,0,2,0,5]

y = odeint(repressilator, y0, times, args = (alpha0, alpha, beta, n))

print(y.shape)
plt.figure()
plt.plot(times, y[:,0], label = '$m_1$')
plt.plot(times, y[:,1], label = '$p_1$')

plt.plot(times, y[:,2], label = '$m_2$')
plt.plot(times, y[:,3], label = '$p_2$')

plt.plot(times, y[:,4], label = '$m_3$')
plt.plot(times, y[:,5], label = '$p_3$')
plt.legend()
plt.ylabel('Amount')
plt.xlabel('Time')
plt.savefig('repr_osc.png')

plt.figure()
plt.plot(y[:,0], y[:,1])
plt.xlabel('Amount $m_1$')
plt.ylabel('Amount $p_1$')
plt.savefig('repr_osc_phase.png')


# changing parameters
y0 = [0,1,0,2,0,3]
params1 = [1, 1.75, 5, 5]
params2 = [1, 1.75, 5, 28]
params3 = [1, 1.75, 5, 1000]

all_params = [params1, params2, params3]

for i in range(3):
    y = odeint(repressilator, y0, times, args = tuple(all_params[i]))

    print(y.shape)
    plt.subplot(3,2,2*i+1)
    plt.plot(times, y[:,0], label = '$m_1$')
    plt.plot(times, y[:,1], label = '$p_1$')

    plt.plot(times, y[:,2], label = '$m_2$')
    plt.plot(times, y[:,3], label = '$p_2$')

    plt.plot(times, y[:,4], label = '$m_3$')
    plt.plot(times, y[:,5], label = '$p_3$')

    plt.ylabel('Amount')
    plt.xlabel('Time')

    plt.subplot(3,2,2*i+2)
    plt.plot(y[:, 0], y[:, 1])
    plt.xlabel('Amount $m_1$')
    plt.ylabel('Amount $p_1$')

plt.savefig('repr_params.png')



plt.show()