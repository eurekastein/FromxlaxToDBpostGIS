import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

base_dir = '/home/eurekastein/Documentos/censo_agropecuario_2007/CensoAgropecuario2007_DatosOriginales'
conn = psycopg2.connect(host='192.168.18.22', database='censo_agro', user='postgres', password='postgres')

user = 'postgres'
psw = 'postgres'
serv = '192.168.18.22'
db = 'censo_agro'

engine = create_engine('postgresql://{}:{}@{}:5432/{}'.format(user,psw,serv,db))

xlsx_list = [] 
for path, dirs, files in os.walk(base_dir):   
    for xlsx in files:
        if xlsx.endswith('.xlsx'): 
            xlsx_path = os.path.join(path, xlsx)
            xlsx_list.append(xlsx_path)

data_frame_list = [] 
for xls in xlsx_list:
    data_frame_list.append(pd.read_excel(xls))

for df in data_frame_list:
    todos = df.to_sql(df, engine)

