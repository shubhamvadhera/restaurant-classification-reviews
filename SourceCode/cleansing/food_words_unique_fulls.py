source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/food_words/'
target_dir = source_dir + 'processed/'
filename = 'foods_all_raw.txt'

dishes = set()

with open(source_dir + filename) as words:
    for word in words:
        # add dishes to set so that only unizue ones remain
        dishes.add(word.rstrip())

output_file = open(target_dir + filename[:-8] + "_unique.txt", 'w+')

for dish in dishes:
    output_file.write(dish + '\n')

output_file.close()
print("script finished")
