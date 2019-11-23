import random
import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


def dropout(a, percent):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    np.put(mat, mask, [np.NaN]*len(mask))
    return mat

class DataFrameImputer(TransformerMixin):

    def __init__(self):
        """Impute missing values.

        Columns of dtype object are imputed with the most frequent value
        in column.

        Columns of other types are imputed with mean of column.

        """
    def fit(self, X, y=None):

        self.fill = pd.Series([X[c].value_counts().index[0]
            if X[c].dtype == np.dtype('O') else X[c].median() for c in X],
            index=X.columns)

        return self

    def transform(self, X, y=None):
        return X.fillna(self.fill)

class DataFrameMICEImputer(TransformerMixin):

    def __init__(self):
        """Impute missing values.

        Columns of dtype object are imputed with the most frequent value
        in column.

        Columns of other types are imputed with mean of column.

        """
    def fit(self, X, y=None):

        self.fill = pd.Series([X[c].value_counts().index[0]
            if X[c].dtype == np.dtype('O') else np.NaN for c in X],
            index=X.columns)

        return self

    def transform(self, X, y=None):
        return X.fillna(self.fill)

def missing_data(db, percentage):
    df = db.copy()
    data = df.values
    modified = dropout(data, percentage)
    new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
    columns = ['race',
               'gender',
               'age',
               'time_in_hospital',
               'num_lab_procedures',
               'num_procedures',
               'num_medications',
               'number_outpatient',
               'number_emergency',
               'number_inpatient',
               'diag_1',
               'diag_2',
               'diag_3',
               'number_diagnoses',
               'max_glu_serum',
               'a1cresult',
               'metformin',
               'repaglinide',
               'nateglinide',
               'chlorpropamide',
               'glimepiride',
               'acetohexamide',
               'glipizide',
               'glyburide',
               'tolbutamide',
               'pioglitazone',
               'rosiglitazone',
               'acarbose',
               'miglitol',
               'troglitazone',
               'tolazamide',
               'examide',
               'citoglipton',
               'insulin',
               'glyburide_metformin',
               'glipizide_metformin',
               'glimepiride_pioglitazone',
               'metformin_rosiglitazone',
               'metformin_pioglitazone',
               'change',
               'diabetesmed',
               'readmitted']
    new_df.columns = columns
    return new_df

def median_impute(df):
    df = DataFrameImputer().fit_transform(df)
    return df

def mice_impute(df):
    MICE_imputer = IterativeImputer(max_iter=10, random_state=0)
    df.iloc[:, :] = MICE_imputer.fit_transform(df)
    return df
#
# def missing_impute_data(db, percentage):
#     df = db.copy()
#     data = df.values
#     modified = dropout(data, percentage)
#     new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
#     columns = ['race',
#                'gender',
#                'age',
#                'time_in_hospital',
#                'num_lab_procedures',
#                'num_procedures',
#                'num_medications',
#                'number_outpatient',
#                'number_emergency',
#                'number_inpatient',
#                'diag_1',
#                'diag_2',
#                'diag_3',
#                'number_diagnoses',
#                'max_glu_serum',
#                'a1cresult',
#                'metformin',
#                'repaglinide',
#                'nateglinide',
#                'chlorpropamide',
#                'glimepiride',
#                'acetohexamide',
#                'glipizide',
#                'glyburide',
#                'tolbutamide',
#                'pioglitazone',
#                'rosiglitazone',
#                'acarbose',
#                'miglitol',
#                'troglitazone',
#                'tolazamide',
#                'examide',
#                'citoglipton',
#                'insulin',
#                'glyburide_metformin',
#                'glipizide_metformin',
#                'glimepiride_pioglitazone',
#                'metformin_rosiglitazone',
#                'metformin_pioglitazone',
#                'change',
#                'diabetesmed',
#                'readmitted']
#     new_df.columns = columns
#     df = new_df
#     df = DataFrameImputer().fit_transform(df)
#     return df
#
# def mice_impute(db, percentage):
#     df = db.copy()
#     data = df.values
#     modified = dropout(data, percentage)
#     new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
#     columns = ['race',
#                'gender',
#                'age',
#                'time_in_hospital',
#                'num_lab_procedures',
#                'num_procedures',
#                'num_medications',
#                'number_outpatient',
#                'number_emergency',
#                'number_inpatient',
#                'diag_1',
#                'diag_2',
#                'diag_3',
#                'number_diagnoses',
#                'max_glu_serum',
#                'a1cresult',
#                'metformin',
#                'repaglinide',
#                'nateglinide',
#                'chlorpropamide',
#                'glimepiride',
#                'acetohexamide',
#                'glipizide',
#                'glyburide',
#                'tolbutamide',
#                'pioglitazone',
#                'rosiglitazone',
#                'acarbose',
#                'miglitol',
#                'troglitazone',
#                'tolazamide',
#                'examide',
#                'citoglipton',
#                'insulin',
#                'glyburide_metformin',
#                'glipizide_metformin',
#                'glimepiride_pioglitazone',
#                'metformin_rosiglitazone',
#                'metformin_pioglitazone',
#                'change',
#                'diabetesmed',
#                'readmitted']
#     new_df.columns = columns
#     df = new_df
#     MICE_imputer = IterativeImputer(max_iter=10, random_state=0)
#     df.iloc[:, :] = MICE_imputer.fit_transform(df)
#     return df