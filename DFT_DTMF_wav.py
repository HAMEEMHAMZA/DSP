# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 2:19:50 2019

@author: hameem
"""

import numpy as np
import matplotlib.pyplot as plot
import math
import cmath
import wave
from scipy.io import wavfile

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

#read wav file
samplingFrequency, signalData = np.array( wavfile.read('press_9.wav') )

#find length of wav data
len1 = np.shape(signalData)[0]

fft_1= np.fft.fft(signalData)
#fft_1= my_dft(sin_array)

#half length
len1 = int(len1/2)

#initialise FFT output array
mag_only = np.zeros(len1)
phase_only = np.zeros(len1)

#calculate FFT and convert to POLAR form
for i in range(len1):
    mag_only[i] = cmath.polar(fft_1[i])[0]
    phase_only[i] = cmath.polar(fft_1[i])[1]

x_list = np.linspace(0,int(samplingFrequency/2),len1)

#Plot magnitude only
plot.plot(x_list, mag_only/1000)

