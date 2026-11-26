import psycopg
def get_hours_per_topic():    
    conn = psycopg.connect("dbname=study_report")
    cur = conn.cursor()
    cur.execute("""SELECT topic, ROUND(SUM(minutes) / 60.0, 1) AS hours
    FROM study_log
    GROUP BY topic
    ORDER BY hours DESC;""")
    rows = cur.fetchall()
    conn.close()
    return rows
if __name__ == "__main__":
    rows = get_hours_per_topic()
    for topic, hours in rows:
        print(f"{topic}: {hours}")
