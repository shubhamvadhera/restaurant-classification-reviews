import json
import re
import operator

result = []
datar = {}
source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/original_data/'
target_dir = source_dir + 'processed/'

# load all reviews in datar dictionary
with open(target_dir + 'relevant_business_ids_and_reviews_v2_combined.json') as f:
    datar = json.load(f)
    print("review file loaded")


# returns the list of words in the category
def categoryWords(stringCategory):
    words = stringCategory.split()
    words_clean = []
    for word in words:
        word = word.lower()
        word = re.sub(r'[\W_]+', '', word)
        word = re.sub(r'[0-9]+', '', word)
        if len(word) < 2:
            continue
        words_clean.append(word)
    return words_clean


with open(target_dir + 'relevant_business_ids_and_categories_v2.json') as f:
    json_obect = json.load(f)
    # for each business id
    for js in json_obect:
        categories = js.get('categories')
        businessid = js.get('business_id')
        reviews = datar.get(businessid)

        # skip processing if there are no reviews for the given business_id
        if reviews == None:
            continue
        # if there is already one catogory for this business_id, we just add it and continue
        if len(categories) < 2:
            my_dict = {}
            my_dict['business_id'] = businessid
            my_dict['category'] = categories[0]
            result.append(my_dict)
            continue

        # if there are multiple categories for the class lable
        new_categories = []
        original_cat_and_words = {}
        for category in categories:
            words = categoryWords(category)
            new_categories.append(words)
            # keep track of the original category and its splitted words
            original_cat_and_words[category] = words
        category_counts = {}
        for newcategory in new_categories:
            for word in newcategory:
                i = 0
                for w in reviews:
                    # if the category word is found in review, increase its count
                    if w == word:
                        i = i + 1
                category_counts[word] = i
        # get the most populat category word
        max_category = max(category_counts.items(), key=operator.itemgetter(1))[0]
        for orig_cat in original_cat_and_words:
            list = original_cat_and_words[orig_cat]
            # get the original category corresponding to most populat category word
            if max_category in list:
                my_dict = {}
                my_dict['business_id'] = businessid
                my_dict['category'] = orig_cat
                # keep the most populat category
                result.append(my_dict)

output_file = open(target_dir + 'relevant_business_ids_and_categories_only_one.json', 'w+')
back_json = json.dumps(result, output_file, indent=2)
output_file.write(back_json)
output_file.close()
