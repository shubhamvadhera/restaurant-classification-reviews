import json
import re

source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/original_data/'
target_dir = source_dir + 'processed/'
filename = 'relevant_business_ids_and_reviews.json'

dict = {}
with open(target_dir + filename) as f:
    json_obect = json.load(f)
    print("file read complete")
    for js in json_obect:
        review = js['review']
        words = review.split()
        review_clean = []
        for word in words:
            # remove numbers and symbols
            word = word.lower()
            word = re.sub(r'[\W_]+', '', word)
            word = re.sub(r'[0-9]+', '', word)
            # ignore one letter words
            if len(word) < 2:
                continue
            review_clean.append(word)
        businessid = js['business_id']
        if businessid in dict:
            # append all reviews under same business_id
            dict[businessid].extend(review_clean)
        else:
            dict[businessid] = review_clean

output_file = open(target_dir + filename[:-5] + "_combined.json", 'w+')
back_json = json.dumps(dict, output_file, indent=2)
output_file.write(back_json)
output_file.close()
