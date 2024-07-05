import psycopg2 as pg
import pandas as pd
import json
import os
import pandas as pd

def getData():
    conn = pg.connect(host="localhost", dbname='postgres', user='postgres', password='p3800mhz')
    try:
        cur = conn.cursor()
        print("Connection Established")
    except (Exception, pg.DatabaseError) as error:
        print(error)

    try:
        qCmd = 'SELECT * FROM Machines'
        cur.execute(qCmd)
        records = cur.fetchall()

        #qCmd = f'SELECT * FROM pmachines WHERE timestamp > {start} AND timestamp <= {end} ORDER BY timestamp DESC LIMIT 200;'
        df = pd.read_sql_query(qCmd, conn)

        if df.empty:
            qCmd = f'SELECT * FROM machines ORDER BY Timestamp DESC LIMIT 200'
            df = pd.read_sql_query(qCmd, conn)
   
    
    except (Exception, pg.DatabaseError) as error:
        print(error)

    return df