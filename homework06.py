# -*- coding: utf-8 -*-

import numpy as np

class trans_prob(object):

    def __init__(self, T_array, init_array):
        self.T_array = T_array
        self.init_array = init_array
        
    def normal_method(self, delta):
        P_array = self.init_array
        d_norm = np.linalg.norm(P_array) 
        while d_norm > delta:
            pri_array = P_array
            P_array = self.T_array.dot(P_array)
            d_norm = np.linalg.norm(P_array-pri_array)
        
        print('定常状態まで遷移させた結果')
        print(P_array)
        
    def monte_carlo_method(self, number): 
        sum_array = np.zeros(9)
        for j in range(10000):
            for i in range(9):    
                r = np.random.rand(9)
                r_array = r/r.sum()
                sum_array = sum_array + self.T_array.dot(self.T_array.dot(self.T_array.dot(self.T_array.dot(r_array)))
            
        array = sum_array/sum_array.sum()
        print('モンテカルロ法で計算した結果')
        print(array)


def main():
    init_Parray = np.array([1,0,0,0,0,0,0,0,0])
    T_array = np.array([
           [1/3,1/4,0,1/4,0,0,0,0,0],
           [1/3,1/4,1/3,0,1/5,0,0,0,0],
           [0,1/4,1/3,0,0,1/4,0,0,0],
           [1/3,0,0,1/4,1/5,0,1/3,0,0],
           [0,1/4,0,1/4,1/5,1/4,0,1/4,0],
           [0,0,1/3,0,1/5,1/4,0,0,1/3],
           [0,0,0,1/4,0,0,1/3,1/4,0],
           [0,0,0,0,1/5,0,1/3,1/4,1/3],
           [0,0,0,0,0,1/4,0,1/4,1/3]])
    delta = 0.00000000001
    Transition = trans_prob(T_array, init_Parray)
    Transition.normal_method(delta)
    Transition.monte_carlo_method(0.02)

if __name__ == "__main__":
    main()