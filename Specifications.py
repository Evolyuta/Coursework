from pydub import AudioSegment
import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import os
import tkinter
from tkinter import *
import re

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

path = os.getcwd() + "/Music"
name = os.listdir(path)

"""Convert from mp3 to wav"""

tempname = []

for i in range(len(name)):
    if os.path.isfile(path + "/" + name[i]):
        split = name[i].rsplit('.', 1)
        if split[-1] == "mp3":
            sound = AudioSegment.from_mp3(path + "/" + name[i])
            sound.export(path + "/" + split[0] + ".wav", format="wav")

name = os.listdir(path)

"""Removing mp3 files"""

for i in range(len(name)):
    if os.path.isfile(path + "/" + name[i]):
        split = name[i].rsplit('.', 1)
        if split[1] == "mp3":
            os.remove('Music/' + name[i])

name = os.listdir(path)

"""Display on music content"""

print("Content of Music directory:\n")
for i in range(len(name)):
    print(str(i + 1) + '. ' + name[i])
print('\n\n')

maxdirdb = []
mindirdb = []
meandirdb = []

for i in range(len(name)):

    filename = re.sub('[.]', '', name[i].rsplit('.', 1)[0])
    print('\n\n' + str(i + 1) + '. ' + filename + ':\n')

    wav = wave.open(path + "/" + name[i], mode="r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    # число каналов, число байт на сэмпл, число вреймов в секунду, общее число фреймов, тип сжатия, имя типа сжатия
    # print(nchannels, sampwidth, framerate, nframes, comptype, compname)

    content = wav.readframes(nframes)
    samples = np.fromstring(content, dtype=types[sampwidth])

    duration = nframes / framerate
    countsamples = 61000
    k = int(nframes / countsamples)
    #peak = 32768.0
    peak = 256 ** sampwidth / 2

    maxdb = []
    mindb = []

    db = []

    amplitude = []

    for n in range(nchannels):

        channel = samples[n::nchannels]

        # if nchannels == 1:
        # channel = channel - peak

        channel = channel[0::k]

        for sample in channel:
            amplitude.append(sample)

    for l in range(len(amplitude)):
        if abs(amplitude[l]) < 1e-303:
            amplitude[l] = 1e-304
        currdb = 20 * math.log10(abs(amplitude[l]) / float(peak))
        if abs(currdb) < 6000:
            db.append(currdb)

    db.sort()

    for l in range(len(db)):
        if l > countsamples * 0.8:
            maxdb.append(db[l])
        elif l <= countsamples * 0.2:
            mindb.append(db[l])


    print('Maximum db =', np.mean(maxdb))
    print('Minimum db =', np.mean(mindb))

    print('Mean db =', np.mean(db))

    maxdirdb.append(np.mean(maxdb))
    mindirdb.append(np.mean(mindb))
    meandirdb.append(np.mean(db))

print('\n\n\nDirectory specifications:\n')

print('Maximum db =', np.mean(maxdirdb))
print('Minimum db =', np.mean(mindirdb))

print('Mean db =', np.mean(meandirdb))
