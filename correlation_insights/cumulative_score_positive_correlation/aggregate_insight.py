import csv
import rbo_func as rbo
import pandas as pd

def rboresult(groundtruth, new, p=0.95):
    return rbo.rbo(groundtruth, new, p)['ext']


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

def convert_to_one(item):
    S = []
    for i in item:
        S.append(((''.join(i))))
    return S

def get_topk(k, file):
    df = pd.read_csv(file, index_col=0)
    df = df.head(k).values.tolist()
    x = convert_to_one(df)
    return x


def get_unique(k, file):
    df = pd.read_csv(file, index_col=0)
    df = df.head(k)
    uniq1 = df.level_0.unique().tolist()
    uniq2 = df.level_1.unique().tolist()
    uniq = set(uniq1 + uniq2)
    return list(uniq)

def generate_correlation_insights(data,k):
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0.01].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

    dataCorr.columns = ['a','b','score']
    topk = dataCorr.sort_values(by=['score'], ascending=False)
    topk['new_score'] = topk['score'] + 1
    topk.drop(['score'], axis = 1, inplace=True)
    topk = topk.sort_values(by=['new_score'], ascending=False)
    topk = topk.head(k)
    return topk['new_score'].sum()
    