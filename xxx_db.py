import pandas as pd
from sqlalchemy import create_engine


conn_string = ('postgresql+psycopg2://postgres:016645@localhost:5432/xxx')
db = create_engine(conn_string)
conn = db.connect()



files = ['cardbase','customerbase','fraudbase','transactionbase']

for file in files:
    df = pd.read_csv(f'D:\\SQL techtfq\\Datasets\\Datasets\\Credit_Card_Data\\table\\{file}.csv')
    df.to_sql(file, con= conn , if_exists= 'replace')                 