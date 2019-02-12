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


def format_time(x, pos=None):
    global duration, nframes, k, mins
    progress = int(x / float(nframes) * duration * k)
    mins, secs = divmod(progress, 60)
    hours, mins = divmod(mins, 60)
    out = "%d:%02d" % (mins, secs)
    if hours > 0:
        out = "%d:" % hours
    return out


def format_db(x, pos=None):
    if pos == 0:
        return ""
    global peak
    if x == 0:
        return "-∞"

    db = 20 * math.log10(abs(x) / float(peak))
    return int(db)


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

for i in range(len(name)):
    wav = wave.open(path + "/" + name[i], mode="r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    # число каналов, число байт на сэмпл, число вреймов в секунду, общее число фреймов, тип сжатия, имя типа сжатия

    # print(nchannels, sampwidth, framerate, nframes, comptype, compname)

    content = wav.readframes(nframes)
    samples = np.fromstring(content, dtype=types[sampwidth])

    duration = nframes / framerate
    w = 800
    k = int(nframes / w / 32)
    peak = 256 ** sampwidth / 2

    max = 0
    min = 0

    positivedb = []
    negativedb = []

    amplitude = []

    for n in range(nchannels):
        channel = samples[n::nchannels]
        if nchannels == 1:
            channel = channel - peak
        channel = channel[0::k]
        for l in range(len(channel)):
            amplitude.append(channel[l])

    for l in range(len(amplitude)):
        if abs(amplitude[l]) < 1e-303:
            amplitude[l] = 1e-304
        if l != 0:
            currdb = 20 * math.log10((abs(amplitude[l]) / abs(amplitude[l - 1])))
            if abs(currdb)<1000:
                if currdb < 0:
                    negativedb.append(currdb)
                else:
                    positivedb.append(currdb)

    for l in range(len(positivedb)):
        if positivedb[l] > max:
            max = positivedb[l]

    for l in range(len(negativedb)):
        if negativedb[l] < min:
            min = negativedb[l]

    print('max db =', max)
    print('min db =', min)

    print('mean pdb =', np.mean(positivedb))
    print('mean ndb =', np.mean(negativedb))

    filename = re.sub('[.]', '', name[i].rsplit('.', 1)[0])
    print(str(i + 1) + '. ' + filename + ' is ready\n')
