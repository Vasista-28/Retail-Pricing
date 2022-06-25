import json
import requests
import numpy as np

 
with open('data1.json') as json_file:
    data = json.load(json_file)

# aList = json.dumps("data1.json")

# json_data = [] # your list with json objects (dicts)

# a = []

for item in data:
    global a 
    a = item['cost']
    print(a)


        # print(a)
    # b = str(a).split(",")
    # c = a.split()
    # c = b.split(",")
    # print(c)
    # print(type(b))
    # print(c)
    # print(b)
    # print(np.(a).tolist())
    # print(list(map(int, b.strip().split())))
    # print(list(item["OPEX"]))

    # for data_item in item['data']:

# req = requests.get("data1.json")