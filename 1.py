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


"""Список wav файлов"""
pathmusic = "/home/evolyuta/PycharmProjects/Coursework/Music"
namemusic = os.listdir(pathmusic)
tempnamemusic = []
for i in range(len(namemusic)):
    if os.path.isfile(pathmusic + "/" + namemusic[i]):
        splitmusicname = namemusic[i].split('.')
        if splitmusicname[-1] == "mp3":
            sound = AudioSegment.from_mp3(pathmusic + "/" + namemusic[i])
            sound.export(pathmusic + "/" + splitmusicname[0] + ".wav", format="wav")
for i in range(len(namemusic)):
    if os.path.isfile(pathmusic + "/" + namemusic[i]):
        splitmusicname = namemusic[i].split('.')
        if splitmusicname[-1] == "wav":
            tempnamemusic.append(namemusic[i])
namemusic = tempnamemusic
for i in range(len(namemusic)):
    splitmusicname = namemusic[i].split('.')
    namemusic[i] = splitmusicname[0]
del (tempnamemusic)
del (splitmusicname)
print(namemusic)
for i in range(len(namemusic)):
    wav = wave.open(pathmusic + "/" + namemusic[i] + ".wav", mode="r")
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

    plt.savefig(os.getcwd() + "/Visualization/" + namemusic[i], dpi=400)
    plt.cla()
    plt.clf()
    plt.close()
    # plt.show()
