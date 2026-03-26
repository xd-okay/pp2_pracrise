import psycopg2


db_db="prac7"
db_user="postgres"
db_pass="Aldiyar"

conn = psycopg2.connect(f"dbname={db_db} user={db_user} password={db_pass}")

cur = conn.cursor()

cur.execute("CREATE TABLE GRP (id serial PRIMARY KEY, FIRST_NAME VARCHAR, LAST_NAME varchar, AGE integer)")

cur.execute("INSERT INTO GRP (ID,FIRST_NAME, LAST_NAME, AGE) VALUES (1,'ALDIYAR', 'JUMADIL', 17)")
cur.execute("INSERT INTO GRP (ID,FIRST_NAME, LAST_NAME, AGE) VALUES (2,'ALIMZHAN', 'RAEV', 17)")


cur.execute("SELECT * FROM GRP;")


# line1=cur.fetchone()
# line2=cur.fetchone()
rows=cur.fetchall()
print(rows)
cur.execute("UPDATE GRP SET AGE=18 WHERE FIRST_NAME='ALDIYAR'")
cur.execute("SELECT * FROM GRP;")
rows=cur.fetchall()
print(rows)

cur.execute("DELETE FROM GRP;")

cur.execute("DROP TABLE GRP;")
conn.commit()


# print(line1)
# print(line2)
cur.close()
conn.close()