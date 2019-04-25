import csv
import os
from pydub import AudioSegment

path = 'Music_mp3/'
subdir = os.listdir(path)
Class = []
ID = []

if os.path.isfile('/home/evolyuta/Coursework/Music/train.csv'):

    with open('/home/evolyuta/Coursework/Music/train.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
    counter = line_count
else:
    with open('/home/evolyuta/Coursework/Music/train.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['ID', 'Class'])
    counter=0


# print(subdir)

for k in range(len(subdir)):
    name = os.listdir(path + subdir[k])
    # print(name)

    """Convert from mp3 to wav"""

    for i in range(len(name)):
        if os.path.isfile(path + subdir[k] + "/" + name[i]):
            split = name[i].rsplit('.', 1)
            if split[-1] == "mp3":
                sound = AudioSegment.from_mp3(path + subdir[k] + "/" + name[i])
                sound.export('/home/evolyuta/Coursework/Music/' + str(counter) + ".wav", format="wav")
            ID.append(counter)
            counter += 1
            Class.append(subdir[k])

"""Removing mp3 files"""

for k in range(len(subdir)):
    name = os.listdir(path + subdir[k])

    for i in range(len(name)):
        if os.path.isfile(path + subdir[k] + "/" + name[i]):
            split = name[i].rsplit('.', 1)
            if split[-1] == "mp3":
                os.remove(path + subdir[k] + "/" + name[i])


with open('/home/evolyuta/Coursework/Music/train.csv', mode='a') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    for i in range(len(Class)):
        employee_writer.writerow([int(ID[i]),Class[i]])



print(Class)
print(ID)
