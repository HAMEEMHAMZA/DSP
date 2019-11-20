# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 4:48:28 2019

@author: hameem
"""

import numpy as np
import matplotlib.pyplot as plot
import math
import cmath


len1 = 10000#length
start = 200
len2 = 4100

#theta array
theta_array = np.linspace(0,math.pi*2,len1)
theta_array = theta_array[start:start+len2]

cosin_array1 = np.sin(theta_array*40+0.8)
cosin_array2 = np.sin(theta_array*25+0.4)
cosin_array = cosin_array1 #+ cosin_array2 #+ np.random.normal(0,1,len2)

hanning = np.hanning(len2)
cosin_array = cosin_array * hanning


plot.plot(cosin_array)
