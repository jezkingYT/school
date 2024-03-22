import json 

with open("data/grid_04.json","r") as file:
    grid = json.load(file)
    print(grid)