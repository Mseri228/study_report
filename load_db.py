import pandas as pd 
import psycopg
df = pd.read_csv("clean_log.csv")
conn = psycopg.connect("dbname=study_report")
cur = conn.cursor()
cur.execute("DELETE FROM study_log;")
for row in df.itertuples(index=False):
    
    cur.execute("INSERT INTO study_log VALUES (%s, %s, %s, %s, %s)", row)
conn.commit()
cur.execute("SELECT COUNT(*) FROM study_log;")
print(cur.fetchone())
conn.close()
