import json
import numpy as np
from sklearn import random_projection
from pprint import pprint


input_file = "/home/raghu/Documents/Fall-16/239/project/yelp/data/Project Data/ProcessedData_stopRemoval/relevant_business_ids_and_reviews_clean.json"
oytput_file =  "/home/raghu/Documents/Fall-16/239/project/yelp/data/Project Data/ProcessedData_stopRemoval/cleanParseMatrix.csr"

dataDict = {}
wordList = {}
wordCount = 0

f = open(oytput_file,'w')


with open(input_file) as data_file:
    data = json.load(data_file)

for d in data:

    if d["business_id"] in dataDict:
        dataDict[d["business_id"]].extend(d["review"])
    else:
        list = d["review"]
        dataDict[d["business_id"]] = list

for key, value in dataDict.items():

    for eachword in value:
        if eachword not in wordList:
            wordCount += 1
            wordList[eachword] = wordCount

i = 0
for key, value in dataDict.items():
    wc = {}
    for word in value:
        if word in wc:
            wc[word] = wc[word]+1
        else:
            wc[word] = 1

    for k, v in wc.items():
        f.write(str(wordList[k])+' '+str(v)+' ')

    f.write('\n')
    i += 1

f.close()


