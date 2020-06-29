import matplotlib.pyplot as plt
import numpy as np

def dP(S, Km, Vmax):
    return Vmax * (S/(Km+S))

#dP = lambda S, Km, Vmax: Vmax *(S/(Km+S))


S = np.arange(0, 10, 0.1)

plt.figure()
plt.plot(S, dP(S, 0.1, 10), label = '$k_m = 0.1$')
plt.plot(S, dP(S, 1., 10), label = '$k_m = 1$')
plt.plot(S, dP(S, 10, 10), label = '$k_m = 10$')
plt.legend()
plt.xlabel('[S]')
plt.ylabel('[P]')
plt.savefig('Michaelis_Menten.png')


# defining Km, Vmax as functions of the rate constants
def Km(k1, km1, k2):
    return (km1+k2)/k1

#Km = lambda k1, km1, k2: (km1 + k2)/k1

def Vmax(k2, e0):
    return k2*e0

#Vmax = lambda k2, e0: k2*e0

plt.figure()
plt.plot(S, dP(S,Km(0.010,0.003,0.030),Vmax(0.003,4.0)), label = '$k_2=0.003$')
plt.plot(S, dP( S,Km(0.010,0.003,0.060),Vmax(0.006,4.0)), label = '$k_2=0.006$')

plt.legend()
plt.xlabel('[S]')
plt.ylabel('[P]')
plt.savefig('rate_to_MM.png')

# Hill equations

def hill(S, Km, Vmax, n):
    return Vmax * (S**n / (Km + S**n))


plt.figure()
plt.plot(S, hill(S, 1, 10, 1), label = '$n = 1$')
plt.plot(S, hill(S, 1., 10, 2), label = '$n = 2$')
plt.plot(S, hill(S, 1, 10, 5), label = '$n = 5$')
plt.legend()
plt.xlabel('[S]')
plt.ylabel('[P]')
plt.savefig('hill_cooperativity.png')

plt.figure()
plt.plot(S, hill(S, 0.1, 10, 3), label = '$k_m = 0.1$')
plt.plot(S, hill(S, 2, 10, 3), label = '$k_m = 2$')
plt.plot(S, hill(S, 8, 10, 3), label = '$k_m = 8$')
plt.legend()
plt.xlabel('[S]')
plt.ylabel('[P]')
plt.savefig('hill_k_m.png')

plt.show()