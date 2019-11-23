import random
import numpy as np
import pandas as pd
import pandas.io.sql as psql
import psycopg2 as pg
from sqlalchemy import create_engine
from sklearn.base import TransformerMixin
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


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
    new_df = pd.DataFrame(modified) #Change % of data to NA in the dataset
    columns = ['race',
         'gender',
         'age',
         'admission_type_id',
         'time_in_hospital',
         'num_lab_procedures',
         'num_procedures',
         'num_medications',
         'number_outpatient',
         'number_emergency',
         'number_inpatient',
         'diag_1',
         'number_diagnoses',
         'insulin',
         'change',
         'readmitted']
    new_df.columns = columns
    return new_df

def missing_data_attr(db, percentage, seed):
    df = db.copy()
    data = df.values
    modified = dropout(data, percentage, seed)
    new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
    columns = ['race', 'gender', 'age', 'admission_type_id', 'discharge_disposition_id','diag_1',
        'insulin', 'change']
    new_df.columns = columns
    return new_df

def missing_data_measure(db, percentage, seed):
    df = db.copy()
    data = df.values
    modified = dropout(data, percentage, seed)
    new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
    columns = ['time_in_hospital', 'num_lab_procedures', 'num_procedures',
        'num_medications', 'number_outpatient', 'number_emergency',
        'number_inpatient', 'number_diagnoses']
    new_df.columns = columns
    return new_df


table_name = 'diabetes'
connection = pg.connect("dbname=small_experiment_no_missing_predicate user=postgres password=zenvisage")
db = psql.read_sql("SELECT * FROM " + table_name, connection)
db.drop(db.columns[[0]], axis=1, inplace=True)


mlist = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]


print("Data missing export to Postgre")
for i in mlist:
    for j in range(90):
        #print(int(i * 100), j)
        x = int(i * 100)
        #print(df)
        #print(df.columns.to_series().groupby(df.dtypes).groups)
        # db missing is db with row contains missing drop 
        # db NaN is db with row contain missing keep 
        table_name1 = "db_" + str(x) + "rand_missing_attr" + str(j+11)
        table_name2 = "db_" + str(x) + "rand_missing_measure" + str(j + 11)
        #table_name3 = "db_" + str(x) + "rand_missing_a_m" + str(j + 1)

        #table_namea = "db_" + str(x) + "dropnan_attr" + str(j+1)
        #table_nameb = "db_" + str(x) + "dropnan_measure" + str(j + 1)
        #table_namec = "db_" + str(x) + "dropnan_a_m" + str(j + 1)

        df = db.copy()
        new_df_a_m = db.copy()
        df_attr = df.select_dtypes(['object'])
        #df_float = df.select_dtypes(['float'])
        df_measure = df.select_dtypes(['int64']).astype(float)
        df_attr = df_attr.drop('readmitted', 1)
        df_attr_missing = missing_data_attr(df_attr, i, j)
        df_attr_missing['readmitted'] = df['readmitted'].values
        new_df_attr = pd.concat([df_attr_missing, df_measure], axis=1, ignore_index=False, sort=False)
        df_measure_missing = missing_data_measure(df_measure, i, j)
        new_df_measure = pd.concat([df.select_dtypes(['object']), df_measure_missing], axis=1, ignore_index=False, sort=False)
        #new_df_a_m = missing_data(new_df_a_m, i, j)
        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/small_experiment_no_missing_predicate')
        c = engine.connect()
        conn = c.connection

        print("Exporting...", table_name1)
        new_df_attr.to_sql(table_name1, engine)
 


        print("Exporting...", table_name2)
        
        new_df_measure.to_sql(table_name2, engine)
     

        # print("Exporting...", table_name3)
        
        # new_df_a_m.to_sql(table_name3, engine)
        # 