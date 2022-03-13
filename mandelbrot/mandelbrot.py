#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:32:06 2021

@author: ioannis
"""

import numpy as np
import matplotlib.pyplot as plt
taille=(5000,5000)
xlim=(-2,1)
ylim=(-1,1)
x = np.linspace(xlim[0],xlim[1],taille[0])
y = np.linspace(ylim[0],ylim[1],taille[1])

def mandelbrot_convergence(c):
    z = i = 0
    while (abs(z)<2) & (i<50):
        i+=1
        z = z**2 + c
    return i

def mandelbrot_set(x,y):
    taillex=len(x)
    tailley=len(y)
    couleurs = np.zeros([tailley,taillex])
    for i in range(taillex):
        for j in range(tailley):
            a = complex(x[i],y[j])
            couleurs[j,i] = mandelbrot_convergence(a)
    return couleurs
            
m=mandelbrot_set(x,y)
plt.pcolormesh(x,y,m,shading='auto')
plt.show()