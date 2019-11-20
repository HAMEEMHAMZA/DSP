# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:35:04 2019

@author: hameem
"""
import numpy as np
import struct
from scipy.io import wavfile
import wave


def signal_to_wav(signal, fname, Fs):
    data = struct.pack('<' + ('h'*len(signal)), *signal)
    wav_file = wave.open(fname, 'wb')
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(Fs)
    wav_file.writeframes(data)
    wav_file.close()
    
    
samplingFrequency, signalData = np.array( wavfile.read('tone_plus_hello.wav') )
band_stop = signal.firwin(1111, [900, 1100], fs=samplingFrequency, pass_zero=True)#bandstop
filtered_data = np.convolve(signalData, band_stop)

#save wave file
signal_to_wav(filtered_data.astype(int),'temp_save.wav', samplingFrequency)

plot.plot(signalData)
plot.plot(filtered_data)