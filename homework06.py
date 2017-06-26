# -*- coding: utf-8 -*-

import numpy as np

class trans_prob(object):

    def __init__(self, T_array, init_array):
        self.T_array = T_array
        self.init_array = init_array
        
    def normal_method(self, delta):
        '''ノルムの変化がdelta以下になるまで遷移させる方法'''
        P_array = self.init_array
        d_norm = np.linalg.norm(P_array) 
        while d_norm > delta:
            pri_array = P_array
            P_array = self.T_array.dot(P_array)
            d_norm = np.linalg.norm(P_array-pri_array)
        
        print('定常状態まで遷移させた結果')
        print(P_array)
        
    def eigenvalue_method(self):
        '''固有値を使って求める方法'''
        eig_array = np.linalg.eig(self.T_array)[0]
        for x,y in enumerate(eig_array): #要素１のインデックスeig_one_indexを求める
            if y==1:
                eig_one_index = x
            else:
                pass
        
        eig_vector = np.linalg.eig(self.T_array)[1][:,eig_one_index]
        print('固有値１の固有ベクトルを正規化したベクトル')
        print(eig_vector/sum(eig_vector)) #正規化
        
        
    def monte_carlo_method(self, number): 
        '''モンテカルロ法　ランダムに遷移させる'''
        for x,y in enumerate(self.init_array): #要素１のインデックスeig_one_indexを求める
            if y==1:
                init_condition = x
        condition = init_condition #最初の位置
        sum_array = np.zeros(len(self.init_array)) #ある位置に何回いたかをカウントする配列
        sum_array[condition] = sum_array[condition] + 1
        for i in range(number):
            T_vector = self.T_array[:,condition]
            random = np.random.rand()
            T = T_vector[0]
            for j in range(len(T_vector)):
                if random < T:
                    condition = j
                    break
                else:
                    T = T + T_vector[j+1]
            sum_array[condition] = sum_array[condition] + 1
        print('モンテカルロ法で計算した結果')
        print(sum_array/sum(sum_array))


def main():
    init_Parray = np.array([1,0,0,0,0,0,0,0,0])
    T_array = np.array([
           [1/3,1/4,  0,1/4,  0,  0,  0,  0,  0],
           [1/3,1/4,1/3,  0,1/5,  0,  0,  0,  0],
           [  0,1/4,1/3,  0,  0,1/4,  0,  0,  0],
           [1/3,  0,  0,1/4,1/5,  0,1/3,  0,  0],
           [  0,1/4,  0,1/4,1/5,1/4,  0,1/4,  0],
           [  0,  0,1/3,  0,1/5,1/4,  0,  0,1/3],
           [  0,  0,  0,1/4,  0,  0,1/3,1/4,  0],
           [  0,  0,  0,  0,1/5,  0,1/3,1/4,1/3],
           [  0,  0,  0,  0,  0,1/4,  0,1/4,1/3]])
    delta = 0.00000000001 #ノルムの誤差
    transit_number = 10000000 #モンテカルロ法においてランダムに遷移させる回数
    Transition = trans_prob(T_array, init_Parray) #クラスの初期化
    Transition.normal_method(delta) 
    print()
    Transition.eigenvalue_method()
    print()
    Transition.monte_carlo_method(transit_number)

if __name__ == "__main__":
    main()