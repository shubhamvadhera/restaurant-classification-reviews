# Classification of Restaurants from Customer Reviews

## Classification of Restaurants from Customer Reviews in Yelp Dataset
Currently, classification of restaurants is done by what restaurants say.

We should be able to classify a restaurant based on customer reviews.

A restaurant may be American by classification but people mostly like it for its Noodles - thus its Chinese as per the customer reviews.

Example - Cheesecake factory serves amazing Pasta but classified as Desserts - should be classified as Italian as well.

### Steps to run

The dataset is Yelp academic dataset downloaded from Yelp website:
https://www.yelp.com/dataset_challenge/dataset

It contains the following files relevant to our project:
  1. yelp_academic_dataset_business.json
    * Contains a list of restaurants, and their categories
    * Sample record format:
    ```json
    {
	"business_id": "5UmKMjUEUNdYWqANhGckJw",
	"full_address": "4734 Lebanon Church Rd\nDravosburg, PA 15034",
	"hours": {
		"Friday": {
			"close": "21:00",
			"open": "11:00"
		},
		"Tuesday": {
			"close": "21:00",
			"open": "11:00"
		},
		"Thursday": {
			"close": "21:00",
			"open": "11:00"
		},
		"Wednesday": {
			"close": "21:00",
			"open": "11:00"
		},
		"Monday": {
			"close": "21:00",
			"open": "11:00"
		}
	},
	"open": true,
	"categories": [
		"Fast Food",
		"Restaurants"
	],
	"city": "Dravosburg",
	"review_count": 7,
	"name": "Mr Hoagie",
	"neighborhoods": [],
	"longitude": -79.9007057,
	"state": "PA",
	"stars": 3.5,
	"latitude": 40.3543266,
	"attributes": {
		"Take-out": true,
		"Drive-Thru": false,
		"Good For": {
			"dessert": false,
			"latenight": false,
			"lunch": false,
			"dinner": false,
			"brunch": false,
			"breakfast": false
		},
		"Caters": false,
		"Noise Level": "average",
		"Takes Reservations": false,
		"Delivery": false,
		"Ambience": {
			"romantic": false,
			"intimate": false,
			"classy": false,
			"hipster": false,
			"divey": false,
			"touristy": false,
			"trendy": false,
			"upscale": false,
			"casual": false
		},
		"Parking": {
			"garage": false,
			"street": false,
			"validated": false,
			"lot": false,
			"valet": false
		},
		"Has TV": false,
		"Outdoor Seating": false,
		"Attire": "casual",
		"Alcohol": "none",
		"Waiter Service": false,
		"Accepts Credit Cards": true,
		"Good for Kids": true,
		"Good For Groups": true,
		"Price Range": 1
	},
	"type": "business"
}
    ```

  2. yelp_academic_dataset_review.json
    * Contains the reviews of the restaurants
    * Format:

    ```json
    {"votes": {"funny": 0, "useful": 0, "cool": 0}, "user_id": "PUFPaY9KxDAcGqfsorJp3Q", "review_id": "Ya85v4eqdd6k9Od8HbQjyA", "stars": 4, "date": "2012-08-01", "text": "Mr Hoagie is an institution. Walking in, it does seem like a throwback to 30 years ago, old fashioned menu board, booths out of the 70s, and a large selection of food. Their speciality is the Italian Hoagie, and it is voted the best in the area year after year. I usually order the burger, while the patties are obviously cooked from frozen, all of the other ingredients are very fresh. Overall, its a good alternative to Subway, which is down the road.", "type": "review", "business_id": "5UmKMjUEUNdYWqANhGckJw"}

    ```

#### Here is the sequence of scripts to run to get the finished files:

  1. First, we need only business_id and relevant categories from the file A. The category would be our class label. For this, we need to extract all the categories for this dataset and check what all categories we are relevant and their counts.
  2. preprocess/category_all.py
    * Input file: yelp_academic_dataset_business.json
    * Output file: category.json
    * Format:
    ```json
    [
	{
		"category": [
			"Fast Food",
			"Restaurants"
		]
	},
	{
		"category": [
			"Nightlife"
		]
	},
	{
		"category": [
			"Active Life",
			"Mini Golf",
			"Golf"
		]
	},
	{
		"category": [
			"Bars",
			"American (New)",
			"Nightlife",
			"Lounges",
			"Restaurants"
		]
	}]
  ```
    
    As we see, many of these are not restaurants. So we need a list of all the unique categories.

  3. preprocess/class_label_all.py
    * Input: category.json
    * Output: category_full.txt
    * Format:
    ```json
    [
  [
    "Restaurants",
    26729
  ],
  [
    "Shopping",
    12444
  ],
  [
    "Food",
    10143
  ],
  [
    "Beauty & Spas",
    7490
  ],
  [
    "Health & Medical",
    6106
  ]]
```
    * Since, there were around only 1000 different categories, we had to look at each of them and decide which category belongs to a restaurant or a place that serves food.
    * So, we manually went through the list and prepared a list of categories that are relevant to our requirement.
    * File: relevant_labels_raw.txt
    * Format:
    ```
    Mexican
American (Traditional)
Italian
Chinese
American (New)
Japanese       
Seafood        
Mediterranean  
Asian Fusion   
Thai          
French         
Indian
```
    * These all labels are related to restaurants
  4. Next, we will only keep the data that is related to restaurants and only the reviews related to those restaurants
    * labels/relevant_business_ids_and_categories.py
      * Input: yelp_academic_dataset_business.json
      * Output: relevant_business_ids_and_categories.json
  5. Similarly, we only keep reviews of those business units that have relevant categories
    * First, we extract the list of business_ids that we are interested in.
    * labels/relevant_business_ids.py
      * Input: relevant_labels_raw.txt, yelp_academic_dataset_business.json
      * Output: relevant_business_ids.txt
    * Now, we use these business_id to keep only the reviews related to these business_id
    * labels/relevant_business_ids_and_reviews.py
      * Input: relevant_business_ids.txt, yelp_academic_dataset_review.json
      * Output: relevant_business_ids_and_reviews.json
      * Format:
      ```json
      [
  {
    "business_id": "5UmKMjUEUNdYWqANhGckJw",
    "review": "Mr Hoagie is an institution. Walking in, it does seem like a throwback to 30 years ago, old fashioned menu board, booths out of the 70s, and a large selection of food. Their speciality is the Italian Hoagie, and it is voted the best in the area year after year. I usually order the burger, while the patties are obviously cooked from frozen, all of the other ingredients are very fresh. Overall, its a good alternative to Subway, which is down the road."
  }]
```
  6. Now, some of the restaurants have more than one relevant category, but since this is a class label, we must restrict each restaurant to just one category. For this, we will see which category of the restaurant is more popular among the reviews.
    * First, we combine all the reviews of a business_id under one business_id. During this process, we remove any numbers and symbols and convert each word to lowercase, so that comparison is uniform.
    * labels/relevant_business_ids_and_reviews_combined.py
      * Input: relevant_business_ids_and_reviews.json
      * Output: relevant_business_ids_and_reviews_combined.json
      * Format:
      ```json
      {
  "sgBl3UDEcNYKwuUb92CYdA": [
    "this",
    "is",
    "the",
    "best",
    "dim",
    "sum",
    "in",
    "entire",
    "arizona",
    "the",
    "owner",
    "was",
    "the",
    "cookers",
    "of",
    "great",
    "wall",
    "on",
    "th",
    "ave",
    "phoenix",
    "they",
    "moved",
    "to",
    "chandler",
    "and",
    "start",
    "their",
    "own",
    "restaurant",
    "if",
    "you",
    "want",
    "the",
    "best"]}
    ```
  7. Now, we will process the file with relevant business_id to keep only one label per business_id.
    * labels/only_one_category_business_ids.py
      * Input: relevant_business_ids_and_reviews_combined.json
      * Output: relevant_business_ids_and_categories_only_one.json
      * Format:
      ```json
      [
  {
    "category": "Fast Food",
    "business_id": "5UmKMjUEUNdYWqANhGckJw"
  },
  {
    "category": "American (New)",
    "business_id": "mVHrayjG3uZ_RLHkLj-AMg"
  },
  {
    "category": "American (Traditional)",
    "business_id": "KayYbHCt-RkbGcPdGOThNg"
  }]
```
  8. Now, we clean our reviews file and keep it ready to be used further in the process.
    * For this, there would be two approaches. The first approach removes all the common words, stop words, numbers, symbols and converts all reviews into lowercase words, so that comparison is uniform.
    * We have gathered a list of common words combined from 2 sources:
      * 5000 words free list from http://www.wordfrequency.info/free.asp
      * 6000 most frequent english words: http://www.insightin.com/esl/
      * Our list contains a total of 6994 unique words
      * common_words.txt
    * cleansing/relevant_bids_reviews_clean.py
      * Input: relevant_business_ids_and_reviews.json
      * Output: relevant_business_ids_and_reviews_clean.json
    * For the second approach, we only keep food related words in our reviews. To gather food related words, we scrapped the website http://allrecipes.com/ for all the world’s recipies.
    * scrap/food_scrapper.py
      * The script scrap the website and pings about 300,000 different URLs to get all the recipes.
      Output: foods_all_raw.txt
      * Output: foods_all_raw.txt
      * We gathered about 218,924 recipes.
      * Next, we remove the duplicates and keep only unique recipes.
      * cleansing/food_words_unique_fulls.py
        * Input: foods_all_raw.txt
        * Output: foods_all_raw_unique.txt
        * We got 77,830 unique recipes
      * Next step is to extract only food words out of these recipes. We remove common words and stopwords.
      * cleansing/food_words_unique_words.py
        * Input: foods_all_raw_unique.txt
        * Output: foods_all_raw_words.txt
        * We get 11,033 unique food words, which covers all the cuisines on allrecipes.com
  9. Now, we process our reviews file and keep only food words in the reviews
    * cleansing/relevant_bids_reviews_foodclean.py
      * Input: relevant_business_ids_and_reviews_clean.json, foods_all_raw_words.txt
      * Output: relevant_business_ids_and_reviews_clean_food.json
  10. In the next step is creating the BOW(Bag of words). We generate two different files, one is with each business and the concatenation of all the reviews without filtering any words for that business and second file is the business id associated with all the review words which are related to food.  These files are generated by the script
    * Name: preprocessing_one_cat.py
    * Input:  relevant_business_ids_and_categories_only_one.json
   relevant_business_ids_and_categories_only_one.json
   * Output: Preprocessed_one_cat_bow.tsv
  11. The final step is to build the classifier model and validate it. We have followed the approach of KNN classification with 10-fold validation.
    * Name: preprocessing_one_cat.py
    * Input: preprocessed_one_cat_bow.tsv
  12. The other approach is running our classification model on data set of reduced dimensionality.  So we extracted the random features from both the files generated in step 10.

### Credits:
Raghavendra Guru

Navit Gaur

Shubham Vadhera
