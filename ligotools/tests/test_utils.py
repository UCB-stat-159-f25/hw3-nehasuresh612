# imports
import pytest
from ligotools import utils as ut
import numpy as np
import os
from scipy.io import wavfile

def test_whiten():
    # get some fake data to simulate the results
    fs = 1024   # sample rate
    dt = 1.0 / fs
    t = np.linspace(0, 1, fs)
    strain = np.sin(2 * np.pi * 50 * t) + 0.5 * np.random.randn(fs)
    
    # fake PSD values
    freqs = np.fft.rfftfreq(len(strain), dt)
    fake_psd = np.ones_like(freqs) + 0.1 * freqs
    interp_psd = lambda f: np.interp(f, freqs, fake_psd)
    
    # run whitening function to test
    whitened = ut.whiten(strain, interp_psd, dt)
    
    # assert length should stay the same
    assert len(whitened) == len(strain)

def test_write_wavfile():
    # create a short audio that follows a sine equation
    fs = 44100
    t = np.linspace(0, 1, fs)
    data = 0.8 * np.sin(2 * np.pi * 440 * t)  # 440 Hz = A note

    filename = "test_chirp.wav"

    # write to wav file
    ut.write_wavfile(filename, fs, data)

    # make sure the file is created
    assert os.path.exists(filename)

    # read file and do  some checks
    rate, d = wavfile.read(filename)
    assert rate == fs  # should have same sampling rate (fs)
    assert len(d) == len(data)

    # cleanup to remove excess
    os.remove(filename)
