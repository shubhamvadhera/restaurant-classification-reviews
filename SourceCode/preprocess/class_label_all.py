import json
from collections import Counter

output_file = open('category_full.txt', 'w')

with open('category.json') as f:
    data = json.load(f)
total = [dic['category'] for dic in data]
total = [cat for sublist in total for cat in sublist]
x = Counter(total)
x.most_common()
back_json = json.dumps(x.most_common(), output_file, indent=2)
output_file.write(back_json)
output_file.close()
