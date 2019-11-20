# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 8:47:10 2019

@author: hameem
"""

import numpy as np
import matplotlib.pyplot as plot
import math
import cmath

def my_dft(signal_array):
    len1= np.shape(signal_array)[0]
    
    real_array = np.zeros(len1)
    imag_array = np.zeros(len1)
    
    for i in range(len1):
        theta_array = np.linspace(0,math.pi*i*2,len1)
        sin_array = np.sin(theta_array)
        cos_array = np.cos(theta_array)
        
        real_array[i] = np.dot(cos_array,signal_array)
        imag_array[i] = np.dot(sin_array,signal_array)
    
    complex_array = np.vectorize(complex)(real_array, imag_array)
    return complex_array

len1 = 10000#length

#theta array
theta_array = np.linspace(0,math.pi*2,len1)

cosin_array1 = np.sin(theta_array*50)
cosin_array2 = np.sin(theta_array*150)
cosin_array = cosin_array1 + cosin_array2 #+ np.random.normal(0,1,len1)


fft_1= np.fft.fft(cosin_array)
#fft_1= my_dft(sin_array)

mag_only = np.zeros(len1)
phase_only = np.zeros(len1)

for i in range(len1):
    mag_only[i] = cmath.polar(fft_1[i])[0]
    phase_only[i] = cmath.polar(fft_1[i])[1]


plot.plot(mag_only/1000)
#plot.plot(phase_only)

