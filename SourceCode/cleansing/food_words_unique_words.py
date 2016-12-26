import time

stime = time.time()
from nltk.corpus import stopwords

source_dir = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/food_words/'
target_dir = source_dir + 'processed/'
filename = 'foods_all_unique.txt'

stop_words = set(stopwords.words("english"))
common_words_file = '/home/svadhera/Documents/yelp_dataset_challenge_academic_dataset/common_words/common_words.txt'
common_words = set()

with open(common_words_file) as words:
    for word in words:
        common_words.add(word.rstrip())

foods = set()

with open(target_dir + filename) as dishes:
    for dish in dishes:
        dish = dish.rstrip()
        # split recipe into words
        words = dish.split('-')
        for word in words:
            # ignore single letter, common and stop words
            if len(word) < 2 or word in stop_words or word in common_words:
                continue
            foods.add(word)

output_file = open(target_dir + filename[:-4] + "_words.txt", 'w+')

for food in foods:
    output_file.write(food + '\n')

output_file.close()
print("--- %s seconds ---" % (time.time() - stime))
