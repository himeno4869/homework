# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def potential(z, a, v0, gamma):
    
    return v0*(z+(a**2)/z) + np.complex(0, (gamma/(2*np.pi))*np.log(z))

if __name__ == "__main__":
    a = 0.7
    v0 = 1.0
    gamma = 5.0
    c = 0.6
    x = np.arange(-10.1, 10.1, 0.1)
    y = np.arange(-10.1, 10.1, 0.1)
    X, Y = np.meshgrid(x,y)
    '''z = np.zeros([202, 202], dtype=np.complex)
    for i in range(202):
        for j in range(202):
            z[j][i] = np.complex(x[i], y[j])
            z[101][101] = np.complex(0.1, 0.1)
    x = (z+(c**2)/z).real
    y = (z+(c**2)/z).imag
    '''
    zz = np.zeros([202, 202], dtype=np.complex)
    for i in range(202):
        for j in range(202):
            zz[j][i] = potential(np.complex(x[i], y[j]), a, v0, gamma)
            if abs(zz[j][i]) > 100:
                zz[j][i] = 0
            if x[i]**2 + y[j]**2 < a**2:
                zz[j][i] = 0
    z = np.zeros([202, 202], dtype=np.complex)
    for i in range(202):
        for j in range(202):
            z[j][i] = np.complex(x[i], y[j])
            z[101][101] = np.complex(0.1, 0.1)
    x = (z+(c**2)/z).real
    y = (z+(c**2)/z).imag
    plt.figure(figsize=(5,4))
    plt.contour(x, y, zz.imag, 100)
    plt.colorbar()