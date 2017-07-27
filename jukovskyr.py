# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def potential(z, a, v0, gamma):
    
    return v0*(z+(a**2)/z) + gamma*np.log(z)

if __name__ == "__main__":
    a = 0.6
    v0 = 1.0
    c = 0.5
    alfa = 5.0*np.pi/180
    beta = 20*np.pi/180
    gamma = 4*np.pi*v0*a*np.sin(alfa+beta)
    cgama = np.complex(0, gamma/(2*np.pi))
    dr = 0.5
    thetar = 360
    xmin = -5
    xmax = 5
    rnge = xmax - xmin
    rrnge = int(rnge / (2*dr))
    dtheta = 2*np.pi / thetar
    center = np.complex(c, 0) + a*np.exp(np.complex(0, np.pi-beta))
    x = np.zeros([rrnge, thetar], dtype=np.complex)
    y = np.zeros([rrnge, thetar], dtype=np.complex)
    for i in range(rrnge):
        for k in range(thetar):
            x[i][k] = ((a+dr*i) * np.exp(np.complex(0, dtheta*k-beta))).real
            y[i][k] = ((a+dr*i) * np.exp(np.complex(0, dtheta*k-beta))).imag
    
    zz = np.zeros([rrnge, thetar], dtype=np.complex)
    for i in range(rrnge):
        for k in range(thetar):
            zz[i][k] = potential(np.complex(x[i][k], y[i][k])*np.exp(np.complex(0, -alfa)), a, v0, cgama)
           
    z = np.zeros([rrnge, thetar], dtype=np.complex)

    for i in range(rrnge):
        for k in range(thetar):
            z[i][k] = np.complex(x[i][k], y[i][k]) + center

    X = (z+(c**2)/z).real
    Y = (z+(c**2)/z).imag

    plt.figure(figsize=(5,4))
    plt.contour(X, Y, zz.imag, 40)
    plt.colorbar()