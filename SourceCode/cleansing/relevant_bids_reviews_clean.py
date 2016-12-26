import json
from nltk.corpus import stopwords
import re

source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/original_data/'
target_dir = source_dir + 'processed/'
filename = 'relevant_business_ids_and_reviews.json'

# stop words taken from nltk library
stop_words = set(stopwords.words("english"))
common_words_file = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/common_words/common_words.txt'
common_words = set()

with open (common_words_file) as words:
    for word in words:
        common_words.add(word.rstrip())

result=[]

with open(target_dir + filename) as f:
    json_obect = json.load(f)
    print("file read complete")
    for js in json_obect:
        review = js['review']
        words = review.split()
        review_clean = []
        for word in words:
            word = word.lower()
            word = re.sub(r'[\W_]+', '', word)
            word = re.sub(r'[0-9]+', '', word)
            # ignore single letter words, stop words, common words
            if len(word) < 2 or word in stop_words or word in common_words:
                continue
            review_clean.append(word)
        my_dict={}
        my_dict['business_id'] = js['business_id']
        my_dict['review'] = review_clean
        result.append(my_dict)

output_file = open(target_dir+filename[:-5]+"_clean.json", 'w+')
back_json=json.dumps(result, output_file, indent =2)
output_file.write(back_json)
output_file.close()