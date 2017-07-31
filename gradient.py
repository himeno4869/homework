# -*- coding: utf-8 -*-

import numpy as np

def numerical_gradient(f, x): #偏微分の計算
    h = 0.0001
    grad = np.zeros_like(x)

    for index in range(x.size):
        temp_value = x[index]
        x[index] = temp_value + h
        fxh1 = f(x)
        
        x[index] = temp_value - h
        fxh2 = f(x)
        
        grad[index] = (fxh1+fxh2)/(2*h)
        x[index] = temp_value
         
    return grad

