import csv
import os
import shutil

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
    counter = 0


for k in range(len(subdir)):
    name = os.listdir(path + subdir[k])

    for i in range(len(name)):
        if os.path.isfile(path + subdir[k] + "/" + name[i]):
            try:
                counter += 1
                shutil.copy(path + subdir[k] + "/" + name[i], '/home/evolyuta/Coursework/Music/' + str(counter) + ".mp3")
                ID.append(counter)
                print(counter)
                Class.append('1' + str(subdir[k]))
            except Exception as e:
                print('Error in ', name[i])

with open('/home/evolyuta/Coursework/Music/train.csv', mode='a') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(len(Class)):
        employee_writer.writerow([int(ID[i]), Class[i]])

print(Class)
print(ID)
