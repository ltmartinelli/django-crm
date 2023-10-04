import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="djangocrm",
    user="postgres",
    password="12345678")

cur = conn.cursor()

conn.commit()
cur.close()
conn.close()

