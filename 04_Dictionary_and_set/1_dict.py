myDict = { "Keys": "Values",
    "Abhi": "student",
    "Marks": "77",
    "List": "[7, 79, 89]", 
    "list": {'Abhi':'Pawar'}
}
print(myDict["Keys"])
print(myDict["Abhi"])
print(myDict["Marks"])

# It Can Be Change or Muttable 
myDict["List"] = [10, 20, 30]
print(myDict["List"])

print(myDict['list'])
print(myDict['list']['Abhi'])
