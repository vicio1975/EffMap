# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:37:23 2018

@author: bmusammartanoV
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:53:08 2018

@author: bmusammartanoV
"""

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')
from scipy import interpolate
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

#Plotting the results
omega_ = [2500,2800,3000] #omega values to be considered for the plot and data interpolation 
col = ["red","blue","green"]
#Figure for the Efficiency maps
colormaps = ["viridis","plasma","inferno","magma"]
fig1 = plt.figure()
for n,j in enumerate(omega_):
    if j in omega:
        print (j)
        ind = [indx for (indx,x) in enumerate(omega) if x == j  ]
        QQ = Q[ind[0]:ind[-1]+1]
        Tp = TotP[ind[0]:ind[-1]+1]
        plt.plot(QQ,Tp,"-",label=j,color=col[n])
        plt.legend()
        ind = []
        ql = len(QQ)
        QQ = []
        ES = []
    else:
        print("the speed is not on the list!!! moving forward in the list!")

plt.ioff()
ngridx = 300
ngridy = 300

#interpolation
xp = np.asarray(Q) 
yp = np.asarray(TotP)
zp = np.asarray(EffStat)
#zp = zp.reshape(ql,len(omega_))

x1 = np.linspace(min(xp),max(xp),ngridx)
y1 = np.linspace(1500,max(yp),ngridy)

fig2 = plt.figure(figsize=plt.figaspect(0.5))

ax = fig2.add_subplot(1, 2, 1, projection='3d')

z1 = griddata((xp, yp), zp, (x1[None,:], y1[None,:]), method='cubic')

CS = plt.contour(x1,y1,z1,15,linewidths=0.5,color='k')
ax = fig2.add_subplot(1, 2, 2, projection='3d')

xig, yig = np.meshgrid(x1, y1)

surf = ax.plot_surface(xig, yig, z1,
        linewidth=0)
plt.show(fig2)



"""
cmaps = [('Perceptually Uniform Sequential', [
            'viridis', 'plasma', 'inferno', 'magma']),
         ('Sequential', [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         ('Sequential (2)', [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']),
         ('Diverging', [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ('Miscellaneous', [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]
    
"""

