# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class lorentz(object):
    
    def __init__(self, sigma, beta, rho, init_state, dlt = 0.01, time = 100):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.init_state = init_state
        self.dlt = dlt
        self.time = time
        self.T = np.arange(0,self.time, self.dlt)
        self.N = self.T.shape[0]        
        
    def euler(self):
        X = np.zeros((self.N, 3))
        X[0] = self.init_state 
        for i in np.arange(self.N-1):
            X[i+1][0] = X[i][0] + self.dlt*self.sigma*(X[i][1]-X[i][0])
            X[i+1][1] = X[i][1] + self.dlt*(X[i][0]*(self.rho-X[i][2]) - X[i][1])
            X[i+1][2] = X[i][2] + self.dlt*(X[i][0]*X[i][1] - self.beta*X[i][2])
            
        return X
        
    def modified_euler(self):
        X = np.zeros((self.N, 3))
        X[0] = self.init_state
        K = np.zeros((3,2))
        for i in np.arange(self.N-1):
            K[0][0] = self.sigma*(X[i][1]-X[i][0])
            K[1][0] = X[i][0]*(self.rho-X[i][2]) - X[i][1]
            K[2][0] = X[i][0]*X[i][1] - self.beta*X[i][2]
            K[0][1] = self.sigma*((X[i][1]+0.5*self.dlt*K[1][0])-(X[i][0]+0.5*self.dlt*K[0][0]))
            K[1][1] = (X[i][0]+0.5*self.dlt*K[0][0])*(self.rho-(X[i][2]+0.5*self.dlt*K[2][0])) - (X[i][1]+0.5*self.dlt*K[1][0])
            K[2][1] = (X[i][0]+0.5*self.dlt*K[0][0])*(X[i][1]+0.5*self.dlt*K[1][0]) - self.beta*(X[i][2]+0.5*self.dlt*K[2][0])
            X[i+1][0] = X[i][0] + 0.5*self.dlt*(K[0][0]+K[0][1])
            X[i+1][1] = X[i][1] + 0.5*self.dlt*(K[1][0]+K[1][1])
            X[i+1][2] = X[i][2] + 0.5*self.dlt*(K[2][0]+K[2][1])
            
        return X
            
    def heun(self):
        X = np.zeros((self.N, 3))
        X[0] = self.init_state
        K = np.zeros((3,2))
        for i in np.arange(self.N-1):
            K[0][0] = self.sigma*(X[i][1]-X[i][0])
            K[1][0] = X[i][0]*(self.rho-X[i][2]) - X[i][1]
            K[2][0] = X[i][0]*X[i][1] - self.beta*X[i][2]
            
            K[0][1] = self.sigma*((X[i][1]+self.dlt*K[1][0])-(X[i][0]+self.dlt*K[0][0]))
            K[1][1] = (X[i][0]+self.dlt*K[0][0])*(self.rho-(X[i][2]+self.dlt*K[2][0])) - (X[i][1]+self.dlt*K[1][0])
            K[2][1] = (X[i][0]+self.dlt*K[0][0])*(X[i][1]+self.dlt*K[1][0]) - self.beta*(X[i][2]+self.dlt*K[2][0])
            
            X[i+1][0] = X[i][0] + 0.5*self.dlt*(K[0][0]+K[0][1])
            X[i+1][1] = X[i][1] + 0.5*self.dlt*(K[1][0]+K[1][1])
            X[i+1][2] = X[i][2] + 0.5*self.dlt*(K[2][0]+K[2][1])
        return X
    
    def runge_kutta(self):
        X = np.zeros((self.N, 3))
        X[0] = self.init_state
        K = np.zeros((3,4))
        for i in np.arange(self.N-1): 
            K[0][0] = self.sigma*(X[i][1]-X[i][0])
            K[1][0] = X[i][0]*(self.rho-X[i][2]) - X[i][1]
            K[2][0] = X[i][0]*X[i][1] - self.beta*X[i][2]
            
            K[0][1] = self.sigma*((X[i][1]+0.5*self.dlt*K[1][0])-(X[i][0]+0.5*self.dlt*K[0][0]))
            K[1][1] = (X[i][0]+0.5*self.dlt*K[0][0])*(self.rho-(X[i][2]+0.5*self.dlt*K[2][0])) - (X[i][1]+0.5*self.dlt*K[1][0])
            K[2][1] = (X[i][0]+0.5*self.dlt*K[0][0])*(X[i][1]+0.5*self.dlt*K[1][0]) - self.beta*(X[i][2]+0.5*self.dlt*K[2][0])
            
            K[0][2] = self.sigma*((X[i][1]+0.5*self.dlt*K[1][1])-(X[i][0]+0.5*self.dlt*K[0][1]))
            K[1][2] = (X[i][0]+0.5*self.dlt*K[0][1])*(self.rho-(X[i][2]+0.5*self.dlt*K[2][1])) - (X[i][1]+0.5*self.dlt*K[1][1])
            K[2][2] = (X[i][0]+0.5*self.dlt*K[0][1])*(X[i][1]+0.5*self.dlt*K[1][1]) - self.beta*(X[i][2]+0.5*self.dlt*K[2][1])
            
            K[0][3] = self.sigma*((X[i][1]+self.dlt*K[1][2])-(X[i][0]+self.dlt*K[0][2]))
            K[1][3] = (X[i][0]+self.dlt*K[0][2])*(self.rho-(X[i][2]+self.dlt*K[2][2])) - (X[i][1]+self.dlt*K[1][2])
            K[2][3] = (X[i][0]+self.dlt*K[0][2])*(X[i][1]+self.dlt*K[1][2]) - self.beta*(X[i][2]+self.dlt*K[2][2])
            
            for j in range(3):
                X[i+1][j] = X[i][j] + self.dlt*(K[j][0]+2*K[j][1]+2*K[j][2]+K[j][3])/6
                
        return X

def main():
    sigma = 10
    beta = 8/3
    rho = 28
    init_state = np.array([12,12,12])
    func = lorentz(sigma, beta, rho, init_state, 0.001)
    X = func.runge_kutta()
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X[:,0], X[:,1], X[:,2])

if __name__ == "__main__":
    main()
        


