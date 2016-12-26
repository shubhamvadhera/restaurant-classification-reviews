import pandas as pd
from collections import Counter
from scipy.sparse import csr_matrix
import numpy as np
from numpy.linalg import norm
from random import randint
import math
import time

cosims = []

start_time = time.time()

df = pd.read_table('/home/raghu/Documents/Fall-16/239/project/yelp/raghu/data/preprocessed_one_cat_bow.tsv', header=None,
                   names=['class', 'review'])
size = len(df)

cosims = [[1.0] * size for _ in range(size)]  # cosine similarities between same elements is 1

nrows = len(df)
idx = {}
tid = 0
nnz = 0
for x in df.itertuples():
    nnz += len(set(x[1]))
    for w in x[1]:
        if w not in idx:
            idx[w] = tid
            tid += 1
ncols = len(idx)

# set up memory
ind = np.zeros(nnz, dtype=np.int)
val = np.zeros(nnz, dtype=np.double)
ptr = np.zeros(nrows + 1, dtype=np.int)
i = 0  # document ID / row counter
n = 0  # non-zero counter
# transfer values
for x in df.itertuples():
    cnt = Counter(x[1])
    keys = list(ke for ke, _ in cnt.most_common())
    l = len(keys)
    for j, ke in enumerate(keys):
        ind[j + n] = idx[ke]
        val[j + n] = cnt[ke]
    ptr[i + 1] = ptr[i] + l
    n += l
    i += 1

mat = csr_matrix((val, ind, ptr), shape=(nrows, ncols), dtype=np.double)
mat.sort_indices()
print('ind:', len(ind))
print('val:', len(val))
print('ptr:', len(ptr))


def predictClass(pClasses):
    wc = {}
    maxCt = 1
    ctClasses = {}
    ctClasses[1] = []

    for cls in pClasses:
        if cls in wc:
            wc[cls] = wc[cls] + 1
            if wc[cls] in ctClasses:
                ctClasses[wc[cls]].append(cls)
            else:
                ctClasses[wc[cls]] = [cls]
            if wc[cls] > maxCt:
                maxCt = wc[cls]
        else:
            wc[cls] = 1
            ctClasses[1].append(cls)

    listClasses = ctClasses[maxCt]

    if len(listClasses) == 1:
        return listClasses[0]

    # if len(listClasses) == 0:
    #     print("len 0")
    num = randint(0, len(listClasses)-1)
    # print('num - ',num)
    # print('len - ',len(listClasses))
    return listClasses[num]


folds = []
f = math.ceil(size / 10)
i = 0
folds.append(i)

while (i < size):
    i = i + f
    if (i > size):
        i = size
    folds.append(i)

cossin_start_time = time.time()
print('calculating cosine similarities...')
for i in range(0, size):
    print("cosim",i,"/",size)
    r1 = mat.getrow(i).toarray().reshape(-1)
    for j in range(i + 1, size):
        r2 = mat.getrow(j).toarray().reshape(-1)
        cosims[i][j] = r1.dot(r2.T) / (norm(r1) * norm(r2))
        cosims[j][i] = cosims[i][j]


def knnMeanAccuracy(k):
    j = 1
    accuracies = 0.0
    while (j < len(folds)):
        knearest = {}
        accuracy = 0.0
        for a in range(folds[j - 1], folds[j]):
            # print("Nearest Neighbours of " + str(df['row'][a]) + " are: ")
            for b in range(0, size):
                if b < folds[j - 1] or b >= folds[j]:
                    knearest[b] = cosims[a][b]
            i = 0
            pClasses = []
            for key in sorted(knearest, key=knearest.__getitem__, reverse=True):
                if i < k:
                    # print(str(df['row'][key]) + "," + str(df['class'][key]))
                    pClasses.append(str(df['class'][key]))
                    i += 1
            # print ("Predicted class: " + predictClass(pClasses))
            # print ("Actual class: " + str(df['class'][a]))
            pClass = predictClass(pClasses)
            if pClass == str(df['class'][a]):
                accuracy = accuracy + 1
        accuracy = accuracy / (folds[j] - folds[j - 1])
        # print("Accuracy: " + str(accuracy))
        accuracies = accuracies + accuracy
        j = j + 1
    # print(accuracies)
    accuracies = accuracies / (len(folds) - 1)
    return accuracies

print("k,Mean Accuracy: " + str(1) + "," + str(knnMeanAccuracy(1)))
print("k,Mean Accuracy: " + str(5) + "," + str(knnMeanAccuracy(5)))
print("k,Mean Accuracy: " + str(10) + "," + str(knnMeanAccuracy(10)))
print("k,Mean Accuracy: " + str(20) + "," + str(knnMeanAccuracy(20)))
print("k,Mean Accuracy: " + str(50) + "," + str(knnMeanAccuracy(50)))
print("k,Mean Accuracy: " + str(100) + "," + str(knnMeanAccuracy(100)))

print("total time", (time.time() - start_time))