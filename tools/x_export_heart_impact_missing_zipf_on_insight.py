import random
import numpy as np
import pandas as pd
import pandas.io.sql as psql
import psycopg2 as pg
from sqlalchemy import create_engine



def dropout(a, percent, seed):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(size * percent)
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

def percentage_missing_zipf(col, N_samples, alpha, seed):

    s = randZipf(col, alpha, N_samples, seed)
    unique, counts = np.unique(s, return_counts=True)
    d = dict(zip(unique, counts / N_samples))
    return d

def missing_data_attr(db, N_samples, alpha, seed, percent):
    col = 7
    rank = percentage_missing_zipf(col, N_samples, alpha, seed)
    df = db.copy()

    cp = df['cp'].values
    cp = dropout(cp, percent*rank[0], seed)

    thal = df['thal'].values
    thal = dropout(thal, percent*rank[1], seed)

    slope = df['slope'].values
    slope = dropout(slope, percent*rank[2], seed)

    exang = df['exang'].values
    exang = dropout(exang, percent*rank[3], seed)
    
    restecg = df['restecg'].values
    restecg = dropout(restecg, percent*rank[4], seed)

    sex = df['sex'].values
    sex = dropout(sex, percent*rank[5], seed)

    fbs = df['fbs'].values
    fbs = dropout(fbs, percent*rank[6], seed)


    #num = df['num'].values
    #readmitted = dropout(readmitted, percent*rank[7], seed)

    #['cp', 'thal', 'slope', 'exang', 'restecg', 'sex', 'fbs']

    frame = { 'cp': cp, 'thal': thal, 
            'slope': slope,
             'exang': exang, 'exang': exang,
             'restecg': restecg,
             'sex': sex,
             'fbs': fbs
            #'num': num       
            } 

    missing_attr = pd.DataFrame(frame)

    return missing_attr

def missing_data_measure(db, N_samples, alpha, seed, percent):
    col = 6
    rank = percentage_missing_zipf(col, N_samples, alpha, seed)
    df = db.copy()

    age = df['age'].values
    age = dropout(age, percent*rank[0], seed)

    restbp = df['restbp'].values
    restbp = dropout(restbp, percent*rank[1], seed)

    chol = df['chol'].values
    chol = dropout(chol, percent*rank[2], seed)

    thalach = df['thalach'].values
    thalach = dropout(thalach, percent*rank[3], seed)

    ca = df['ca'].values
    ca = dropout(ca, percent*rank[4], seed)

    oldpeak = df['oldpeak'].values
    oldpeak = dropout(oldpeak, percent*rank[5], seed)


    frame = { 'age': age, 'restbp': restbp, 
            'chol': chol, 'thalach': thalach,
             'ca': ca, 'oldpeak': oldpeak
            } 

    missing_measure = pd.DataFrame(frame)
    return missing_measure


#a_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
#m_columns = ['age', 'restbp', 'chol', 'thalach', 'ca', 'oldpeak']

table_name = 'heart'
connection = pg.connect("dbname=heart_dataset_zipf user=postgres password=zenvisage")
db = psql.read_sql("SELECT * FROM " + table_name, connection)
db.drop(db.columns[[0]], axis=1, inplace=True)




mlist = [0.01, 0.03, 0.05, 0.1]#[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
a_list = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
size = 4186

print("Data missing export to Postgre")
for i in mlist:
    for a in a_list:
        for j in range(100):
            x = int(i * 100)
            #print(int(i * 100), j)
            #print(df)
            #print(df.columns.to_series().groupby(df.dtypes).groups)
            # db missing is db with row contains missing drop
            # db NaN is db with row contain missing keep
            y = int(a * 100)
            table_name1 = "db_" + str(x) + "zipf" + str(y) + "_missing_attr" + str(j+1)
            table_name2 = "db_" + str(x) + "zipf" + str(y) + "_missing_measure" + str(j + 1)

            df = db.copy()
            df_attr = df.select_dtypes(['object'])
            df_float = df.select_dtypes(['float'])
            df_measure = df.select_dtypes(['int64']).astype(float)
            df_measure['oldpeak'] = df_float['oldpeak']

            df_attr = df_attr.drop('num', 1)
            df_attr_missing = missing_data_attr(df_attr, size, a, j, i)
            df_attr_missing['num'] = df['num'].values
            new_df_attr = pd.concat([df_attr_missing, df_measure], axis=1, ignore_index=False, sort=False)
            

            df_measure_missing = missing_data_measure(df_measure, size, a, j, i)
            new_df_measure = pd.concat([df.select_dtypes(['object']), df_measure_missing], axis=1, ignore_index=False, sort=False)

            engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/heart_dataset_zipf')
            c = engine.connect()
            conn = c.connection

            print("Exporting...", table_name1)
            new_df_attr.to_sql(table_name1, engine)

            print("Exporting...", table_name2)
            new_df_measure.to_sql(table_name2, engine)

