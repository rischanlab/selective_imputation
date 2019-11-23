import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import random
import csv
import aggregate_insight as ag


def dropout(a, percent, seed):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    random.seed(seed)
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    np.put(mat, mask, [np.NaN]*len(mask))
    return mat

def randZipf(n, alpha, numSamples, seed):
    # Calculate Zeta values from 1 to n:
    tmp = np.power( np.arange(1, n+1), -alpha )
    zeta = np.r_[0.0, np.cumsum(tmp)]
    # Store the translation map:
    distMap = [x / zeta[-1] for x in zeta]
    # Generate an array of uniform 0-1 pseudo-random values:
    np.random.seed(seed)
    u = np.random.random(numSamples)
    # bisect them with distMap
    v = np.searchsorted(distMap, u)
    samples = [t-1 for t in v]
    return samples

def percentage_missing_zipf(N_samples, alpha, seed):

    s = randZipf(10, alpha, N_samples, seed)
    unique, counts = np.unique(s, return_counts=True)
    d = dict(zip(unique, counts / N_samples))
    return d

def missing_data(db, N_samples, alpha, seed, percent):

    rank = percentage_missing_zipf(N_samples, alpha, seed)
    #print(rank)
    df = db.copy()

    age = df['age'].values
    age = dropout(age, percent*rank[0], seed)

    bmi = df['bmi'].values
    bmi = dropout(bmi, percent*rank[1], seed)

    bp = df['bp'].values
    bp = dropout(bp, percent*rank[2], seed)

    s1 = df['s1'].values
    s1 = dropout(s1, percent*rank[3], seed)

    s2 = df['s2'].values
    s2 = dropout(s2, percent*rank[4], seed)

    s3 = df['s3'].values
    s3 = dropout(s3, percent*rank[5], seed)

    s4 = df['s4'].values
    s4 = dropout(s4, percent*rank[6], seed)

    s5 = df['s5'].values
    s5 = dropout(s5, percent*rank[7], seed)

    s6 = df['s6'].values
    s6 = dropout(s6, percent*rank[8], seed)

    sex = df['sex'].values
    sex = dropout(sex, percent*rank[9], seed)


    frame = { 'age': age, 
            'bmi': bmi, 'bp': bp,
             's1': s1, 's2': s2,
             's3': s3, 's4': s4,
             's5': s5, 's6': s6, 
             'sex': sex   
            } 

    missing_zipf = pd.DataFrame(frame)
    return missing_zipf

diab_bunch = load_diabetes()

df = pd.DataFrame(diab_bunch.data, columns = diab_bunch.feature_names)
columns = ['age',
           'bmi',
           'bp',
           's1',
           's2',
           's3',
           's4',
           's5',
           's6',
          'sex']
df = df.reindex(columns=columns)

db_ideal = df.copy()

#print(db_ideal)
ideal_topk = ag.generate_correlation_insights(db_ideal)
#print(ideal_topk, len(ideal_topk))

N_samples = 4420

k_list = [5,10,15,20,25,30,35,40,45] #5,10,15,20,25,30,35,40,45
mlist = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] #0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9
a_list = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7] #, 

for a in a_list:
  for k in k_list:
    topk = ideal_topk[:k]
    for i in mlist:
      for j in range(100):
        data = missing_data(df, N_samples, a, j, i)
        #print(data)

        temp_topk = ag.generate_correlation_insights(data)
        missing_topk = temp_topk[:k]
        with open('results/missing_vs_ideal_zipf.csv', 'a', newline='') as f:
          #print(missing_topk, len(missing_topk))
          #print(topk, len(topk))
          fields = [i*100, a, k, ag.rboresult(missing_topk, topk), ag.jaccard_similarity(missing_topk, topk)]
          print(fields)
          writer = csv.writer(f)
          writer.writerow(fields)

        