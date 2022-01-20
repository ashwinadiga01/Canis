import json
from os import path
from tokenize import Double

filename = 'niftySW.json'
listObj = []

with open(filename) as fp:
  listObj = json.load(fp)

def scriptWeightage(TK,SW):
    listObj.append({
    "TK": TK,
    "SW": SW
    })
    
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))


TK = int(input("Enter token value : "))
SW = float(input("Enter script weightage : "))

scriptWeightage(TK,SW)