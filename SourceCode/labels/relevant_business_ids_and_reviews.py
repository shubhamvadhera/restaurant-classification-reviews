import json

source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/original_data/'
target_dir = source_dir + 'processed/'

relevant_ids = set()
with open(target_dir + 'relevant_business_ids.txt') as ids:
    for id in ids:
        relevant_ids.add(id.rstrip())
data = []

# file containing all the reviews
with open(source_dir + 'yelp_academic_dataset_review.json') as f:
    for line in f:
        data.append(json.loads(line))

result = []

for d in data:
    businessid = d.get('business_id')
    if businessid in relevant_ids:
        my_dict = {}
        my_dict['business_id'] = d.get('business_id')
        my_dict['review'] = d.get('text')
        result.append(my_dict)

output_file = open(target_dir + 'relevant_business_ids_and_reviews_v2.json', 'w+')
back_json = json.dumps(result, output_file, indent=2)
output_file.write(back_json)
output_file.close()
