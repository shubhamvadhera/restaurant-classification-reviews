import json

relevant_labels = set()

# open relevant labels
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
    keep = False
    for category in categories:
        # if category is among relevant categories
        if category in relevant_labels:
            keep = True
            break
    if keep:
        # keep business id
        result.append(d.get('business_id'))

output_file = open(target_dir + 'relevant_business_ids.txt', 'w+')

for res in result:
    output_file.write(res + '\n')

output_file.close()
