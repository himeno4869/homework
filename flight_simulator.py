# -*- coding: utf-8 -*-
import numpy as np
from scipy.integrate import odeint
from scipy.linalg import block_diag
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')

def Rotation_X(Psi): #x軸の変換行列（Ψ）
    R_x = np.array([[np.cos(Psi), np.sin(Psi), 0],
                    [-np.sin(Psi), np.cos(Psi), 0],
                    [0, 0, 1]])
    return R_x

def Rotation_Y(Theta): #y軸の変換行列（Θ）
    R_y = np.array([[np.cos(Theta), 0, -np.sin(Theta)],
                    [0, 1, 0],
                    [np.sin(Theta), 0, np.cos(Theta)]])
    return R_y
    
def Rotation_Z(Phi): #ｚ軸の変換行列（Φ）
    R_z = np.array([[1, 0, 0],
                    [0, np.cos(Phi), np.sin(Phi)],
                    [0, -np.sin(Phi), np.cos(Phi)]])
    return R_z
    
def dynamical_system(x, t, A, U0):
    # x = [u, alpha, q, theta, beta, p, r, phi, psi, x, y, z]
    dx = A.dot(x)
    u = x[0] + U0 #速度
    uvw = np.array([u, u*x[4], u*x[1]]) # 速度ベクトル
    Rotation = np.dot(Rotation_X(-x[8]), Rotation_Y(-x[3]), Rotation_Z(-x[7]))
    dX = np.dot(Rotation, uvw)
    dx[9] = dX[0]
    dx[10] = dX[1]
    dx[11] = dX[2]
    return dx
    
# 有次元安定微係数
STC = {'Xu' : -0.01,
       'Zu' : -0.1,
       'Mu' : 0.001,
       'Xa' : 30.0,
       'Za' : -200.0,
       'Ma' : -4.0,
       'Xq' : 0.3,
       'Zq' : -5.0,
       'Mq' : -1.0,
       'Yb' : -45.0,
       'Lb' : -2.0,
       'Nb' : 1.0,
       'Yp' : 0.5,
       'Lp' : -1.0,
       'Np' : -0.1,
       'Yr' : 3.0,
       'Lr' : 0.2,
       'Nr' : -0.2}
       
condition = {'W0' : 0.0,
             'U0' : 100.0,
             'theta0' : 0.05,
             'g' : 9.8}
             
# 縦のシステム
A_lat = np.array([[STC['Xu'], STC['Xa'], -condition['W0'], -condition['g']*np.cos(condition['theta0'])],
                  [(STC['Zu']/condition['U0']), (STC['Za']/condition['U0']), 1+(STC['Zq']/condition['U0']), -condition['g']*np.sin(condition['theta0'])/condition['U0']],
                  [STC['Mu'], STC['Ma'], STC['Mq'], 0],
                  [0, 0, 1, 0]])

# 横方向のシステム
A_lon = np.array([[STC['Yb'], condition['W0']+STC['Yp'], -condition['U0']+STC['Yr'], condition['g']*np.cos(condition['theta0']), 0],
                  [STC['Lb'], STC['Lp'], STC['Lr'], 0.0, 0.0],
                  [STC['Nb'], STC['Np'], STC['Nr'], 0.0, 0.0],
                  [0., 1., np.tan(condition['theta0']), 0., 0.],
                  [0., 0., 1./np.cos(condition['theta0']), 0., 0.]])

A = block_diag(A_lat, A_lon)

A = block_diag(A, np.zeros([3, 3]))

endurance = 500 #飛行時間
step = 10 #1secあたりの時間ステップ数
t = np.arange(0, endurance, 1/step)

#初期パラメータ x0 = [u, alpha, q, theta, beta, p, r, phi, psi]
x0_lat = np.array([10.0, 0.1, 0.4, 0.2]) # 縦の初期パラメータ
x0_lon = np.array([0.0, 0.6, 0.4, 0.2, 0.2]) # 横の初期パラメータ
x0_pos = np.array([0.0, 0.0, -1000.0]) #initial position of the airplane
x0 = np.hstack((x0_lat, x0_lon, x0_pos))

x = odeint(dynamical_system, x0, t, args=(A, condition['U0'])) 
print('run successfully')

plt.ion()
fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x[:,9], x[:,10], x[:,11])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim([-5000, 2000])
ax.set_ylim([-2000, 5000])
ax.set_zlim([-5000, 2000])
plt.show()
             
             
             