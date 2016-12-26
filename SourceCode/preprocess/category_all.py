import json

# holds the source data file
data = []

# open source file
with open('/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json') as f:
    for line in f:
        data.append(json.loads(line))
output_file = open('category.json', 'w')

# holds the results
result = []
for review in data:
    my_dict = {}

    # keep only categories
    my_dict['category'] = review.get('categories')
    result.append(my_dict)
back_json = json.dumps(result, output_file)
output_file.write(back_json)
output_file.close()
