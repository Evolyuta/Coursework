import os
from pydub import AudioSegment

path = '/home/evolyuta/Coursework/Music/Punk/'
name = os.listdir(path)

"""Convert from mp3 to wav"""

for i in range(len(name)):
    if os.path.isfile(path + "/" + name[i]):
        split = name[i].rsplit('.', 1)
        if split[-1] == "mp3":
            sound = AudioSegment.from_mp3(path + "/" + name[i])
            sound.export(path + "/" + split[0] + ".wav", format="wav")

"""Removing mp3 files"""

for i in range(len(name)):
    if os.path.isfile(path + "/" + name[i]):
        split = name[i].rsplit('.', 1)
        if split[1] == "mp3":
            os.remove(path + "/" + name[i])
