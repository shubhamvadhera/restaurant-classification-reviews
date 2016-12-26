import json
import random

rev_input_file = "/home/raghu/Documents/Fall-16/239/project/yelp/raghu/data/relevant_business_ids_and_reviews_clean_food.json"
cat_input_file = "/home/raghu/Documents/Fall-16/239/project/yelp/raghu/data/relevant_business_ids_and_categories_only_one.json"
output_file =  "/home/raghu/Documents/Fall-16/239/project/yelp/raghu/data/preprocessed_only_food_one_cat_bow.tsv"

dataDict = {}
catDict = {}

f = open(output_file,'w')

with open(rev_input_file) as data_file:
    data = json.load(data_file)

for d in data:

    if d["business_id"] in dataDict:
        dataDict[d["business_id"]].extend(d["review"])
    else:
        l = d["review"]
        dataDict[d["business_id"]] = l


with open(cat_input_file) as data_file:
    data = json.load(data_file)

for d in data:
    catDict[d["business_id"]] = d["category"]


for key, val in dataDict.items():
    cat = catDict[key]
    rev = ' '.join(val)
    f.write(cat+'\t'+rev+"\n")


