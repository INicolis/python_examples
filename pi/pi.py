#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 17:14:29 2019
@author: Ioannis Nicolis
"""

from numpy import random 
from matplotlib import pyplot
from math import sqrt, pi 

class tirecarre:
    def __init__(self):
        self.x = 2*random.random()-1
        self.y = 2*random.random()-1
        self.r2 = self.x**2+self.y**2
    
    def incercle(self):
        return (self.r2<=1)

n = 10**3
totalincercle = 0
x = []
y = []
inc = []
for i in range(n):
    P = tirecarre()
    if (P.incercle()):
        pyplot.plot(P.x,P.y,'ro')
        totalincercle += 1
    else:
        pyplot.plot(P.x,P.y,'go')
        
pihat = 4*totalincercle/n
    
print('Pi est approché par {0:f}' .format(pihat))


x = [i/n for i in range(-n,n+1)]
y = [sqrt(1-x**2) for x in x];

pyplot.plot(x,y,'b')
pyplot.plot(x,[-y for y in y],'b')
axes = pyplot.gca()
axes.set_aspect('equal', adjustable='box')
pyplot.show()

print('erreur commise = {0:f}' .format(abs(pihat-pi)))
print('erreur attendue <= {0:f}' .format(3/sqrt(n)))

