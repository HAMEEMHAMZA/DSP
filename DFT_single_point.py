# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:35:04 2019

@author: hameem
"""
import numpy as np
import struct
from scipy.io import wavfile
import wave
import math
import cmath

def my_dft_single_point(signal_array,fs,freq):
    len1= np.shape(signal_array)[0]
    
    real_array = np.zeros(len1)
    imag_array = np.zeros(len1)
    
    freq_div = fs/freq
    points_per_freq = len1 / freq_div
    
    theta_array = np.linspace(0,math.pi*points_per_freq*2,len1)
    sin_array = np.sin(theta_array)
    cos_array = np.cos(theta_array)
        
    real_val = np.dot(cos_array,signal_array)
    imag_val = np.dot(sin_array,signal_array)
    
    complex_val = np.vectorize(complex)(real_val, imag_val)
    return complex_val


    
samplingFrequency, signalData = np.array( wavfile.read('press_1.wav') )
DFT1 = my_dft_single_point(signalData, samplingFrequency, 770)
mag_only = cmath.polar(DFT1)[0]
print(int(mag_only/1000))
