import json

source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/original_data/'
target_dir = source_dir + 'processed/'
filename = 'relevant_business_ids_and_reviews_v2_clean_v2.json'

food_words_file = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/food_words/processed/foods_all_unique_words.txt'
food_words = set()

with open(food_words_file) as words:
    for word in words:
        food_words.add(word.rstrip())

result = []
with open(target_dir + filename) as f:
    json_obect = json.load(f)
    print("file read complete")
    for js in json_obect:
        reviewwords = js['review']
        review_food = []
        for word in reviewwords:
            if word in food_words:
                # only keep food words
                review_food.append(word)
        my_dict = {}
        my_dict['business_id'] = js['business_id']
        my_dict['review'] = review_food
        result.append(my_dict)

output_file = open(target_dir + filename[:-5] + "_food.json", 'w+')
back_json = json.dumps(result, output_file, indent=2)
output_file.write(back_json)
output_file.close()
