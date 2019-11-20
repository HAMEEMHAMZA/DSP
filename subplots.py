# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 6:57:47 2019

@author: hameem
"""

import numpy as np
import matplotlib.pyplot as plot
import math
import cmath


len1 = 10000#length

num_plots = 10


#theta array
theta_array = np.linspace(0,math.pi*2,len1)



for j in range(num_plots):
    i = j+1
    plot.subplot(num_plots,1,i)
    plot.grid(color='b', linestyle='-', linewidth=0.2)
    cosin_array1 = np.cos(theta_array*i)
    sin_array1 = np.sin(theta_array*i)
    plot.plot(cosin_array1)
    plot.plot(sin_array1)

