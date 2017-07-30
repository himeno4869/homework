# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt

def potential(z, a, v0, gamma):

    return v0*(z+(a**2)/z) + gamma*np.log(z)

def main():
    
    a = 0.8

    v0 = 1.0

    c = 0.7
    
    rho = 1
    
    rad = np.pi/180

    alfa = 1*rad

    beta = 20*rad

    gamma = 4*np.pi*v0*a*np.sin(alfa+beta)

    cgama = np.complex(0, gamma/(2*np.pi))

    dr = 0.05

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


    z2 = np.zeros([rrnge, thetar], dtype=np.complex)

    z1 = np.zeros([rrnge, thetar], dtype=np.complex)

    

    for i in range(rrnge):

        for k in range(thetar):

            z2[i][k] = np.complex(x[i][k], y[i][k]) + center



    for i in range(rrnge):

        for k in range(thetar):

            z1[i][k] = (z2[i][k]-center)*np.exp(np.complex(0, -alfa))



    f = np.exp(np.complex(0, -alfa))*(v0*(1-(a**2)/(z1**2))+cgama/z1)/(1-(c**2)/(z2**2))

    f1 = 1-(f.real**2+f.imag**2)/v0**2

           

    for i in range(rrnge):

        for k in range(thetar):

            if abs(f1[i][k]) > 4:

                f1[i][k] = 0

                  

    cxp = 0

    cyp = 0
    
    ci = 0
    
    x0 = np.array([-0.8, -0.6, -0.4, -0.2, 0, 0.2])
    
    m = 0

    for i in range(thetar-1):

        dxw = X[0][i+1] - X[0][i]

        dyw = Y[0][i+1] - Y[0][i]

        dnx = dyw

        dny = -dxw

        cpm = (f1[0][i+1]+f1[0][i])/2

        cxp = cxp - cpm*dnx

        cyp = cyp - cpm*dny
        
        ci = ci + cpm*dny*(X[0][i+1]+X[0][i])/2 - cpm*dnx*(Y[0][i+1]+Y[0][i])/2
                          
        m = m + (x0-(X[0][i+1]+X[0][i])/2)*cpm*dnx + ((Y[0][i+1]+Y[0][i])/2)*cpm*dny
        
    xcp = -ci/cyp
    
    l = 4*c
    q = 0.5*rho*(v0**2)*(l**2)
    
    cm = m/q
    
    print("Cm = " + str(cm))
        

                          
    print("xcp = " + str(xcp))

    cxp = cxp/(4*c)

    cyp = cyp/(4*c)

    cdp = cxp*np.cos(alfa) + cyp*np.sin(alfa)

    clp = cyp*np.cos(alfa) - cxp*np.sin(alfa)

    print('Cd = ' + str(cdp))

    print('Cl = ' + str(clp))

    plt.figure(figsize=(10,2))

    plt.plot(X[0], Y[0])
    
    plt.title('wing shape')

    plt.figure(figsize=(5,4))

    plt.title('Cp')
    
    plt.contour(X, Y, f1, 100)
    
    plt.plot(X[0], Y[0])

    plt.colorbar()
    
    plt.figure(figsize=(5,4))

    plt.title('stream line')

    plt.contour(X, Y, zz.imag, 100)
    
    plt.plot(X[0], Y[0])

    plt.colorbar()
    
    plt.figure(figsize=(5, 4))

    plt.plot(x0, cm)
    
    plt.title('cm')
    
if __name__ == "__main__":
    main()