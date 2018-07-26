# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:53:08 2018

@author: bmusammartanoV
"""

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')
from scipy import interpolate
#from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 

file = "data.csv"
fid = open(file,"r+")
omega = []
Q = []
StatP = []
TotP = []
EffStat = []
EffTot  = []

next(fid)
for line in fid:
    line = line.split(",")
    omega.append(float(line[0]))
    Q.append(float(line[1]))    
    StatP.append(float(line[2]))
    TotP.append(float(line[3]))    
    EffStat.append(float(line[4]))
    EffTot.append(float(line[5]))    
    
omega_ = [2500,2800,3000]
fig1 = plt.figure()
for j in omega_:
    
    if j in omega:
        print (j)
        ind = [indx for indx,x in enumerate(omega) if x == j  ]
        QQ = Q[ind[0]:ind[-1]+1]
        Tp = TotP[ind[0]:ind[-1]+1]
        plt.plot(QQ,Tp,"-",label=j)
        plt.legend()
        ind = []
        QQ = []
        ES = []
    else:
        print("the speed is not on the list!!! moving forward in the list!")

plt.ioff()
ngridx = 200
ngridy = 200

xp = np.asarray(Q) 
yp = np.asarray(TotP)
zp = np.asarray(EffStat)
zp = zp.reshape(6,2)
f = interpolate.interp2d(xp,yp,zp)
x1 = np.linspace(min(Q),max(Q),200)
y1 = np.linspace(0,max(TotP),200)
z1 = f(x1,y1)
CP = plt.contour(x1, y1, z1 )
plt.clabel(CP, inline=1, fontsize=10)
plt.show(fig1)

fig2 = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x1, y1, z1 , 50, cmap='binary')
ax.set_xlabel('Q(cms)')
ax.set_ylabel('Total Pressure(Pa)')
ax.set_zlabel('Eff(-)');
plt.show(fig2)

