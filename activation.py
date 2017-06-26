# -*- coding: utf-8 -*-

import numpy as np

class Activation:
    
    def __init__(self):
        self.hoge = 3
        
    def relu(self, x):
        y = np.maximum(0, x)
        return y
    
    def sigmoid(self, x):
        y = 1/(1 + np.exp(-x))
        return y
    
    def step(self, x):
        if x <= 0:
            y = 0
        else:
            y = 1
        return y
    
    