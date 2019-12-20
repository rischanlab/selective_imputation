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

def generate_skewness_insights(data, k):
    topk = data.skew(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk.columns = ['atr', 'skew']
    minskew = topk.tail(1)['skew'].tolist()[0]
    topk['new_score'] = topk['skew'] + abs(minskew)
    topk.drop(['skew'], axis = 1, inplace = True)
    topk = topk.head(k)
    return topk['new_score'].sum()
