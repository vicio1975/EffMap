# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:53:08 2018

@author: bmusammartanoV
"""

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')
from scipy import interpolate
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
from scipy.interpolate import griddata
    
#import os
#import shutil

#data acquisition
file = "data.csv"
fid = open(file,"r+")
omega = []
Q = []
StatP = []
TotP = []
EffStat = []
EffTot  = []
next(fid) #skip the header file
for line in fid:
    line = line.split(",") #remove the commas
    omega.append(float(line[0]))
    Q.append(float(line[1]))    
    StatP.append(float(line[2]))
    TotP.append(float(line[3]))    
    EffStat.append(float(line[4]))
    EffTot.append(float(line[5]))    
fid.close()
#Figure for the Efficiency maps
colormaps = ["viridis","plasma","inferno","magma"]
omega_ = [2500,2800,3000] #omega values to be considered for the plot and data interpolation 
for n,j in enumerate(omega_):
    if j in omega:
        ind = [indx for (indx,x) in enumerate(omega) if x == j  ]
        QQ = Q[ind[0]:ind[-1]+1]
        Tp = TotP[ind[0]:ind[-1]+1]
        ind = []
        ql = len(QQ)
        QQ = []
        ES = []
    else:
        print("the speed is not on the list!!! moving forward in the list!")
#Plotting the results
omega_ = [2500,2800,3000] #omega values to be considered for the plot and data interpolation 
col = ["red","blue","green"]
#Figure for the Efficiency maps

ngridx = 300
ngridy = 300

xp = np.asarray(Q) 
yp = np.asarray(TotP)
zp = np.asarray(EffStat)
#zp = zp.reshape(ql,len(omega_))

#define grid
x1 = np.linspace(min(Q),max(Q),ngridx)
y1 = np.linspace(1500,max(TotP),ngridy)
#grid data
z1 =  griddata((xp,yp), zp,(x1[None,:],y1[:,None]),method="cubic",fill_value=0, rescale=False)
# contour the gridded data, plotting dots at the randomly spaced data points.
fig1 = plt.figure()
CS = plt.contour(x1,y1,z1,15,cmap=plt.cm.jet)
plt.xlim(min(Q),max(Q))
plt.ylim(1500,max(TotP))
plt.title('griddata test')
plt.show(fig1)

