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
    columns = ['age',
               'sex',
               'bmi',
               'bp',
               's1',
               's2',
               's3',
               's4',
               's5',
               's6']
    new_df.columns = columns
    return new_df

diab_bunch = load_diabetes()

df = pd.DataFrame(diab_bunch.data, columns = diab_bunch.feature_names)
db_ideal = df.copy()

ideal_topk = ag.generate_correlation_insights(db_ideal)
print(ideal_topk, len(ideal_topk))


k_list = [5,10,15,20,25,30,35,40,45] #5,10,15,20,25,30,35,40,45
mlist = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] #0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9

for k in k_list:
	topk = ideal_topk[:k]
	for i in mlist:
	    for j in range(100):
	    	data = missing_data(df, i, j)
	    	temp_topk = ag.generate_correlation_insights(data)
	    	missing_topk = temp_topk[:k]
	    	with open('results/missing_vs_ideal.csv', 'a', newline='') as f:
	    		#print(missing_topk, len(missing_topk))
	    		#print(topk, len(topk))
	    		fields = [i*100, k, ag.rboresult(missing_topk, topk), ag.jaccard_similarity(missing_topk, topk)]
	    		print(fields)
	    		writer = csv.writer(f)
	    		writer.writerow(fields)

        