# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def x2_calculate(x, x1):
    '''微分方程式を元にして加速度の値を計算する関数'''
    return -2*gamma*x1 - omega_2*x
#以下は微分方程式の初期値
gamma = 0.3
omega_2 = 1.0
x = 1.0
x1 = 1.0
x2 = -1.6

#以下はオイラー法で微分方程式を解くための設定
dt = 0.01
t_array = np.arange(0,20,dt)
x_array = np.zeros_like(t_array)
x1_array = np.zeros_like(t_array)
x2_array = np.zeros_like(t_array)
x_array[0] = x
x1_array[0] = x1
x2_array[0] = x2_calculate(x, x1)

for i in np.arange(len(t_array)-1):
    x_array[i+1] = x_array[i] + x1_array[i]*dt #dt後のxの値の計算
    x1_array[i+1] = x1_array[i] + x2_array[i]*dt #dt後のvの値の計算
    x2_array[i+1] = x2_calculate(x_array[i+1], x1_array[i+1]) #dt後の加速度の値の更新
    
#以下は計算結果表示
plt.subplot(3, 1, 1)
plt.plot(t_array, x_array)
plt.xlabel('time')
plt.ylabel('x')
plt.title('displacement')

plt.subplot(3, 1, 2)
plt.plot(t_array, x1_array)
plt.xlabel('time')
plt.ylabel('v')
plt.title('velocity')

plt.subplot(3, 1, 3)
plt.plot(t_array, x2_array)
plt.xlabel('time')
plt.ylabel('a')
plt.title('acceleration')

plt.tight_layout()
plt.show()