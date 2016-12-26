import requests
import numpy as np
import time

# url to ping
base_url = 'http://allrecipes.com/recipe/'

startTime = time.time()


def getRecipe(num):
    print("request number: ", num)
    secs = np.random.uniform(0.05, 0.1)
    print("delay: ", secs)
    # wait randomly between each request for 0.05 to 0.1 seconds
    time.sleep(secs)
    url = base_url + str(num)
    response = requests.get(url, timeout=5)
    words = response.url.rsplit('/')[5]
    if (len(words) < 1):
        # no recipe on this url
        print("empty")
        return
    print(words)
    # append recipe to file
    with open("foods_all_raw.txt", "a") as foodfile:
        foodfile.write(words + '\n')


i = 1
while i < 300001:
    try:
        getRecipe(i)
        print("--- %s Elapsed Time ---" % (time.time() - startTime))
    except Exception:
        print("exception occured. will try again")
        i = i - 1
    i = i + 1
print("***********************SCRIPT FINISHED***************************************")
