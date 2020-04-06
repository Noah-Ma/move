import json
path = 0
paths = []
while path!='k' and path!= 'K':
    if len(paths)=0:
        path = input("Enter the path (or 'k' if finished): ")
    else:
        path = input("Enter the path: ")
    if path != 'k' and path != 'K':
        paths.append(path)
dest = input("Enter the destination: ")

variables = {'path':paths, "dest":dest}

with open("vars.json", "w") as file:
    json.dump(variables, file)