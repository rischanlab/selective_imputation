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

def missing_data(db, percentage, seed):
    df = db.copy()
    data = df.values
    modified = dropout(data, percentage, seed)
    new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
    columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang',
       'oldpeak', 'slope', 'ca', 'thal']
    new_df.columns = columns
    return new_df

db = pd.read_csv('heart.csv')
df = db[db['target'] == 1]
#df.drop(df.columns[[0]], axis=1, inplace=True)
df.drop(['target'], axis=1, inplace=True)


db_ideal = df.copy()

#ideal_topk = ag.generate_kurtosis_insights(db_ideal)
#print(ideal_topk, len(ideal_topk))


k_list = [1,2,3,4,5,6,7,8,9,10,11,12,13] #5,10,15,20,25,30,35,40,45
mlist = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] #0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9

for k in k_list:
    topk = ag.generate_kurt_insights_cum(db_ideal,k)
    for i in mlist:
        for j in range(100):
            data = missing_data(df, i, j)
            data = missing_data(df, i, j)
            missing_topk = ag.generate_kurt_insights_cum(data,k)
            with open('results/cum_kurtosis_missing_vs_ideal_random.csv', 'a', newline='') as f:
                #print(missing_topk, len(missing_topk))
                #print(topk, len(topk))
                fields = [i*100, k, abs(topk - missing_topk)]
                print(fields)
                writer = csv.writer(f)
                writer.writerow(fields)

        