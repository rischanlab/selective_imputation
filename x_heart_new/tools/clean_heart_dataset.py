import numpy as np
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql

from sqlalchemy import create_engine

engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/new_heart_disease_random')

conn = pg.connect("dbname=seedb_data user=postgres password=zenvisage")
df = psql.read_sql("SELECT * FROM heart_disease", conn)

# read the file and create a pandas dataframe

#Export to postgre
print("exporting to postgre table")
c = engine.connect()
conn = c.connection
df.to_sql('heart', engine)

conn.close()

