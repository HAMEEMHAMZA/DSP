# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:06:25 2019

@author: hameem
"""

import numpy as np
import matplotlib.pyplot as plot

length = 100
start1 = 30
end1 = 70

f1 = np.zeros(length)
g1 = np.zeros(length)

for i in range(length):
    if ( start1<=i<=end1 ):
        f1[i] = 1*(end1-start1)
        g1[i] = end1 - i

f3 = np.copy(f1)
g3 = np.copy(g1)

g1 = np.concatenate((np.zeros(int(length)),g1))


#correlation
conv1 = np.zeros(length*2)
temp1 = np.zeros(length)
f2 = np.concatenate((f1,temp1))
zero_temp = np.zeros(length)
for i in range(length*2):
    f2 = np.roll(f2,1)
    f2[length*2-1] = 0
    conv1[i] = np.dot(f2,g1)


plot.plot(conv1)

#for comparing- numpy function
plot.plot(np.convolve(f3,g3))