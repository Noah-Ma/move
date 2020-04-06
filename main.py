import json
import os
import random
import time
def rename(file):
    a = random.randint(0, 1000000)
    i = file.split(".")[0] + '-{}-'.format(str(a))+'.{}'.format(file.split(".")[1])
    return i 
# Load variables
with open("vars.json", "r") as file:
    vars = json.load(file)
paths = vars["path"]
dest = vars["dest"]

# check for simularities and move
while True:
    for path in paths:
        for fle in os.listdir(path):
            for File in os.listdir(dest):
                while fle==File:
                    i = rename(fle)
                    os.rename(path+'\\'+fle ,path+'\\'+ i)
                    fle = i
            if path[-1] == '\\':
                pathy = path+fle
            else:
                pathy = path+'\\'+fle
            if dest[-1] == '\\':
                desty = dest+fle
            else:
                desty = dest+'\\'+fle
            os.rename(pathy, desty)
    time.sleep(10)