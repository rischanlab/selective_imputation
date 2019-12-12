# -*- coding: utf-8 -*-
import itertools


def data(table, atr, measure, func):
    db_name = 'heart_dataset_zipf_impact_alpha'
    table = table
    prod = list(itertools.product(func, measure))
    data_set = {i: prod for i in atr}
    
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)

# A = 34
# M = 8
# F = 3
# 816 views



