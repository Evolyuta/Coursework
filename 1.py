from pydub import AudioSegment
import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import os
import tkinter
from tkinter import *

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
        splitmusic = name[i].rsplit('.',1)
        if splitmusic[-1] == "mp3":
            sound = AudioSegment.from_mp3(path + "/" + name[i])
            sound.export(path + "/" + splitmusic[0] + ".wav", format="wav")



"""Removing mp3 files"""

name = os.listdir(path)

for i in range(len(name)):
    if os.path.isfile(path + "/" + name[i]):
        splitmusic = name[i].rsplit('.',1)
        if splitmusic[1] == "mp3":
            os.remove('Music/'+name[i])





name = os.listdir(path)

print("Content of Music directory:\n")
for i in range(len(name)):
    print(name[i])
print('\n')





for i in range(len(name)):
    wav = wave.open(path + "/" + name[i], mode="r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

    print(nchannels, sampwidth, framerate, nframes, comptype, compname)

    duration = nframes / framerate
    w, h = 800, 450
    k = int(nframes / w / 32)
    DPI = 72
    peak = 256 ** sampwidth / 2

    content = wav.readframes(nframes)
    samples = np.fromstring(content, dtype=types[sampwidth])

    plt.figure(1, figsize=(float(w) / DPI, float(h) / DPI), dpi=DPI)
    plt.subplots_adjust(left=0.03, bottom=0.05, right=1, top=0.98,
                        wspace=0.0, hspace=0.0)

    for n in range(nchannels):
        channel = samples[n::nchannels]

        channel = channel[0::k]
        if nchannels == 1:
            channel = channel - peak

        axes = plt.subplot(2, 1, n + 1, axisbg="k")
        axes.plot(channel, "#00ced1")
        axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
        plt.grid(True, color='#e0ffff')
        axes.xaxis.set_major_formatter(ticker.NullFormatter())

    axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))

    filenamepng=name[i].rsplit('.')[0];
    plt.savefig(os.getcwd() + "/Visualization/" + filenamepng, dpi=400)
    plt.cla()
    plt.clf()
    plt.close()
    # plt.show()

for i in range(len(name)):
    if os.path.isfile(path + "/" + name[i]):
        splitmusic = name[i].rsplit('.',1)
        if splitmusic[1] == "wav":
            os.remove('Music/'+name[i])
