# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


time_array = np.arange(0, 80, 0.01)
u_array = np.zeros_like(time_array)
w_array = np.zeros_like(time_array)

#x = [u, w, x, z, psi, gamma]

def dynamical_system(x, t):
    
    rho = 0.736
    alfa = 0.0506
    T = 20800
    m = 7500
    g = 9.8
    S = 27.9
    Cd0 = 0.0548
    Cla = 4.3
    K = 3.02
    omega = 2*np.pi/40
    psi0 = np.pi/6
    L = 0.5*rho*(x[0]**2)*S*Cla*alfa
    D = 0.5*rho*(x[0]**2)*S*(Cd0+K*(alfa**2))
    d_u = (-D+T*np.cos(alfa))/m - g*np.sin(x[4])
    psi = psi0*np.sin(omega*(t-20)) if 20 < t < 60 else 0
    d_gamma = (((L+T*np.sin(alfa))/m)*np.cos(psi)-g*np.cos(x[4]))/x[0]
    
    
    return [d_u, -d_u*np.sin(x[4]), x[0], x[0]*np.sin(x[4]), d_gamma]
    
x0 = [180, 0, 0, 5000, 0]

X = sp.integrate.odeint(dynamical_system, x0, time_array)

print(X)
plt.plot(time_array, X[:, 3])
plt.show()