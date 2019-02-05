import os

path = os.getcwd() + "/Music"

name = os.listdir(path)

print("Content of Music directory:\n")
for i in range(len(name)):
    print(name[i])