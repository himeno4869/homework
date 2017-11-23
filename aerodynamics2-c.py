# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def main():
    
    #initialization
    rho0 = 1.225
    t0 = 293.0
    visc = 1.458e-6*(t0**1.5)/(t0+110.4)
    width = 0.5
    v0 = 20.0
    re0 = rho0*v0*width/visc
    blt = width*5.3/(re0)**0.5
    nx = 50000
    dx = width/nx
    ny = 200
    ymax = blt*2.0
    dy = ymax/ny
    xy = np.zeros([nx, ny+1])
    u = np.zeros_like(xy)
    v = np.zeros_like(xy)
    
    #state of start
    for j in range(ny):
        u[0][j] = v0
        v[0][j] = 0
         
    #calculation of velocity
    for i in range(nx-1):
        u[i][0] = 0
        v[i][0] = 0
        u[i][ny] = v0
        
        for j in range(ny-1):
            
            dudy1 = (u[i][j+2]-u[i][j])/(2.0*dy)
            dudy2 = (u[i][j+2]-2.0*u[i][j+1]+u[i][j])/(dy**2)
            dudx = (dudy2*visc/rho0-v[i][j+1]*dudy1)/u[i][j+1]
            u[i+1][j+1] = u[i][j+1]+dx*dudx
             
            dudx1 = (u[i+1][j]-u[i][j])/dx
            dudx2 = (u[i+1][j+1]-u[i][j+1])/dx
            v[i+1][j+1] = v[i+1][j]-(dudx1+dudx2)*dy/2.0
            
    u[nx-1][ny] = 20

    #calculation of the boundary layer
    boundary_layer = np.zeros_like(u[:, 0])
    for i in range(nx):
        for j in range(ny+1):
            if u[i][j] > 0.995*v0:
                boundary_layer[i] = j*dy
                break
    
    #calculation of the efficiency of viscosity
    u_wallb = u[:, 1]
    u_wall = np.zeros_like(u_wallb)
    dudy_wall = (u_wallb-u_wall)/dy
    tau = visc*dudy_wall
    Cf = tau/(0.5*rho0*u_wallb**2)
    
    #calculation of the displacement thickness
    thick_d = np.zeros_like(u[:, 0])
    for i in range(nx):     
        for j in range(ny+1):
            thick_d[i] = thick_d[i]+(1-u[i][j]/v0)*dy
                   
    #calculation of the momentum thickness
    thick_m = np.zeros_like(u[:, 0])
    for i in range(nx):     
        for j in range(ny+1):
            thick_m[i] = thick_m[i]+(u[i][j]/v0)*(1-u[i][j]/v0)*dy
    
    #calculation of the energy thickness
    thick_e = np.zeros_like(u[:, 0])
    for i in range(nx):     
        for j in range(ny+1):
            thick_e[i] = thick_e[i]+(u[i][j]/v0)*(1-(u[i][j]/v0)**2)*dy
    
        
    #plot
    x = np.arange(0, nx)*dx
    y = np.arange(0, ny+1)*dy
    plt.style.use('ggplot')
    #plt.title('velocity')
    #plt.xlabel('y')
    #plt.plot(u[nx-1], y)
    
    #integral equation
    Rex = rho0*v0*x/visc
    boundary_layer_i = 5.2*x/Rex**0.5
    thick_d_i = 1.72*x/Rex**0.5
    thick_m_i = 0.664*x/Rex**0.5
    
    '''
    plt.title('viscosity efficiency')
    plt.xlabel('x')
    plt.plot(x, Cf)
    '''
    
    plt.title('(_i) means integral equation')
    plt.plot(x, boundary_layer, 'b')
    plt.plot(x, thick_d, 'g')
    plt.plot(x, thick_m, 'r')
    plt.plot(x, thick_e, 'c')
    plt.plot(x, boundary_layer_i, 'k')
    plt.plot(x, thick_d_i, 'm')
    plt.plot(x, thick_m_i, 'y')

    plt.legend(['boundary layer', 'displacement thickness', 'momentum thickness', 'energy thickness', 'boundary layer_i', 'displacement thickness_i', 'momentum thickness_i'])
    
    '''    
    #velocity at the trailing edge
    plt.subplot(6, 1, 1)
    plt.title('velocity')
    plt.xlabel('y')
    plt.plot(y, u[nx-1])
    
    #boundary layer
    plt.subplot(6, 1, 2)
    plt.title('boundary layer')
    plt.xlabel('x')
    plt.plot(x, boundary_layer)
    
    #displacement thickness
    plt.subplot(6, 1, 3)
    plt.title('displacement thickness')
    plt.xlabel('x')
    plt.plot(x, thick_d)
    
    #momentum thickness
    plt.subplot(6, 1, 4)
    plt.title('momentum thickness')
    plt.xlabel('x')
    plt.plot(x, thick_m)
    
    #energy thickness
    plt.subplot(6, 1, 5)
    plt.title('energy thickness')
    plt.xlabel('x')
    plt.plot(x, thick_e)
    
    #viscosity efficiency at wall
    plt.subplot(6, 1, 6)
    plt.title('viscosity efficiency')
    plt.xlabel('x')
    plt.plot(x, Cf)

    
    plt.tight_layout()
'''    
       
    
if __name__ == "__main__":
    main()