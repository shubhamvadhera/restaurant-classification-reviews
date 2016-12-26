import json

relevant_labels = set()

with open('relevant_labels_raw.txt') as labels:
    for label in labels:
        relevant_labels.add(label.rstrip())

data = []
source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/original_data/'
target_dir = source_dir + 'processed/'

with open(source_dir + 'yelp_academic_dataset_business.json') as f:
    for line in f:
        data.append(json.loads(line))

result = []

for d in data:
    categories = d.get('categories')
    new_categories = []
    for category in categories:
        if category in relevant_labels:
            # check that the category is relevant
            new_categories.append(category)
    if len(new_categories) > 0:
        my_dict = {}
        my_dict['business_id'] = d.get('business_id')
        my_dict['categories'] = new_categories
        result.append(my_dict)

output_file = open(target_dir + 'relevant_business_ids_and_categories_v2.json', 'w+')
back_json = json.dumps(result, output_file, indent=2)
output_file.write(back_json)
output_file.close()
