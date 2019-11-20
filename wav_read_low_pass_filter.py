# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:35:04 2019

@author: hameem
"""
import numpy as np
import struct
from scipy.io import wavfile
import wave
from scipy import signal


def signal_to_wav(signal, fname, Fs):
    data = struct.pack('<' + ('h'*len(signal)), *signal)
    wav_file = wave.open(fname, 'wb')
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(Fs)
    wav_file.writeframes(data)
    wav_file.close()
    
    
samplingFrequency, signalData = np.array( wavfile.read('hello1.wav') )
low_pass = signal.firwin(111, 1000, pass_zero=True, fs = samplingFrequency)#lowpass
filtered_data = np.convolve(signalData, low_pass)

#save wave file
signal_to_wav(filtered_data.astype(int),'temp_save.wav', samplingFrequency)

plot.plot(signalData)
plot.plot(filtered_data)