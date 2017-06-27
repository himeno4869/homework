# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class lorentz(object):
    
    def __init__(self, sigma, beta, rho):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.dlt = 0.01
        self.time = 100
        self.T = np.arange(0,self.time, self.dlt)
        self.N = self.T.shape[0]        
        
    def euler(self):
        X = np.zeros((self.N,3))
        X[0] = np.array([1,25,14]) #initial state
        for i in np.arange(self.N-1):
            X[i+1][0] = X[i][0] + self.dlt*self.sigma*(X[i][1]-X[i][0])
            X[i+1][1] = X[i][1] + self.dlt*(X[i][0]*(self.rho-X[i][2]) - X[i][1])
            X[i+1][2] = X[i][2] + self.dlt*(X[i][0]*X[i][1] - self.beta*X[i][2])
            
        return X
        
    def modified_euler(self):
        
    def heun(self):
        
    def runge_kutta(self):

def main():
    func = lorentz(10, 8/3, 28)
    X = func.euler()
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X[:,0], X[:,1], X[:,2])

if __name__ == "__main__":
    main()
        


