import psycopg
conn = psycopg.connect("dbname=study_report")
cur = conn.cursor()
cur.execute("""SELECT topic, ROUND(SUM(minutes) / 60.0, 1) AS hours
FROM study_log
GROUP BY topic
ORDER BY hours DESC;""")
rows = cur.fetchall()
for topic, hours in rows:
    print(f"{topic}: {hours}")
conn.close()