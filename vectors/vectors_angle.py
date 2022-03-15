#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:37:33 2022

@author: Ioannis Nicolis
"""

from math import sqrt

# A function to manually compute the cosine of the angle between 
# tow plane vectors AB and AC given A,B and C coordinates

def cosabc(xa,ya,xb,yb,xc,yc):
    coordABx=xb-xa
    coordABy=yb-ya
    coordACx=xc-xa
    coordACy=yc-ya
    ABscalAC=coordABx*coordACx+coordABy*coordACy
    normeAB=sqrt(coordABx**2+coordABy**2)
    normeAC=sqrt(coordACx**2+coordACy**2)
    cosBAC=ABscalAC/(normeAB*normeAC)
    return(cosBAC)
    
angle=cosabc(3,4,-2,6,8,9)
print("Le cosinus vaut",angle)

# Same computation but using numpy this time
import numpy as np
def cosabc_np(xa,ya,xb,yb,xc,yc):
    A=np.array([xa,ya])
    B=np.array([xb,yb])
    C=np.array([xc,yc])
    AB=B-A
    AC=C-A
    normeAB=np.linalg.norm(AB)
    normeAC=np.linalg.norm(AC)
    ABscalAC=np.dot(AB,AC)
    cosBAC=ABscalAC/(normeAB*normeAC)
    return(cosBAC)

angle=cosabc_np(3,4,-2,6,8,9)
print("Le cosinus vaut",angle)

# And using matplotlib to create a plot
import matplotlib.pyplot as plt
def trace(xa,ya,xb,yb,xc,yc):
    plt.arrow(xa,ya,xb-xa,yb-ya,head_width=0.5, head_length=0.5)
    plt.arrow(xa,ya,xc-xa,yc-ya,head_width=0.5, head_length=0.5)
    plt.grid()
    plt.xlim(min([xa,xb,xc])-1,max([xa,xb,xc])+1)
    plt.ylim(min([ya,yb,yc])-1,max([ya,yb,yc])+1)
    plt.text(xa,ya,'A',fontsize=16)
    plt.text(xb,yb,'B',fontsize=16)
    plt.text(xc,yc,'C',fontsize=16)
    plt.show()

trace(3,4,-2,6,8,9)