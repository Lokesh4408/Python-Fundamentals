import os
import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd
import librosa
import pandas as pd
#matplotlib inline

mp3_filename = 'C:\\Users\\ivanr\\OneDrive\\Desktop\\UpWork5e33-6e3e-4937-bd0a-a270a0a7f692.mp3'


def print_plot_play(x, Fs, text=''):
    """1. Prints information about an audio singal, 2. plots the waveform, and 3. Creates player
    
    Notebook: C1/B_PythonAudio.ipynb
    
    Args: 
        x: Input signal
        Fs: Sampling rate of x    
        text: Text to print
    """
    print('%s Fs = %d, x.shape = %s, x.dtype = %s' % (text, Fs, x.shape, x.dtype))
    plt.figure(figsize=(8, 2))
    plt.plot(x, color='gray')
    plt.xlim([0, x.shape[0]])
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
    ipd.display(ipd.Audio(data=x, rate=Fs))

# Read wav
#fn_wav = os.path.join('..', 'data', 'B', 'FMP_B_Note-C4_Piano.wav')
#x, Fs = librosa.load(fn_wav, sr=None)
#print_plot_play(x=x, Fs=Fs, text='WAV file: ')

# Read mp3
fn_mp3 = os.path.join('..', 'data', 'B', mp3_filename)
x, Fs = librosa.load(fn_mp3, sr=None)
print_plot_play(x=x, Fs=Fs, text='MP3 file: ')