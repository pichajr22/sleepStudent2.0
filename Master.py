import os
from urllib import robotparser
import psycopg2
try:
    conn = psycopg2.connect(database="vdtlugyl", user="vdtlugyl", password="MtgLesCauzESzl9MzklRMh2mzS7OZLzS", host="satao.db.elephantsql.com", port="5432")
    base=conn.cursor()
    base.execute("select version()")
    row = base.fetchone()
    print("row",row)
    rows=base.fetchall()

    base.execute('Select * from "Master"')
    rows=base.fetchall()
    nombre=""
    id=0
    for row in rows:
        nombre=row[1]
        id=row[0]
        print(id," Nombre: ",nombre)
        
except Exception as ex:
    print(ex)