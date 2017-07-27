# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def potential(z, a, v0, gamma):
    
    return v0*(z+(a**2)/z) + np.complex(0, (gamma/(2*np.pi))*np.log(z))

if __name__ == "__main__":
    a = 0.6
    v0 = 1.0
    gamma = 5.0
    c = 0.8
    dr = 0.5
    thetar = 360
    xmin = -5
    xmax = 5
    rnge = xmax - xmin
    rrnge = int(rnge / (2*dr))
    dtheta = 2*np.pi / thetar
    x = np.zeros([rrnge, thetar], dtype=np.complex)
    y = np.zeros([rrnge, thetar], dtype=np.complex)
    for i in range(rrnge):
        for k in range(thetar):
            x[i][k] = ((a+dr*(i+1)) * np.exp(np.complex(0, dtheta*k))).real
            y[i][k] = ((a+dr*(i+1)) * np.exp(np.complex(0, dtheta*k))).imag
    
    zz = np.zeros([rrnge, thetar], dtype=np.complex)
    for i in range(rrnge):
        for k in range(thetar):
            zz[i][k] = potential(np.complex(x[i][k], y[i][k]), a, v0, gamma)
           
    z = np.zeros([rrnge, thetar], dtype=np.complex)
    for i in range(rrnge):
        for k in range(thetar):
            z[i][k] = np.complex(x[i][k], y[i][k])
            
    X = (z+(c**2)/z).real
    Y = (z+(c**2)/z).imag

    plt.figure(figsize=(5,4))
    plt.contour(X, Y, zz.imag, 50)
    plt.colorbar()