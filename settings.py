import json
path = 0
paths = []
while path!='k' and path!= 'K':
    
    path = input("Enter the path: ")
    if path != 'k' and path != 'K':
        paths.append(path)
dest = input("Enter the destination: ")

variables = {'path':paths, "dest":dest}

with open("vars.json", "w") as file:
    json.dump(variables, file)