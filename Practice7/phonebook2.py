import psycopg2

db_db="prac7"
db_user="postgres"
db_pass="Aldiyar"

conn = psycopg2.connect(f"dbname={db_db} user={db_user} password={db_pass}")

cur = conn.cursor()

cur.execute("SELECT MAX(ID) FROM phonebook1")

id = cur.fetchone()[0] +1

print(id)

name=input()
phone_number=input()

cur.execute("INSERT INTO phonebook1 (id, name, number_ph) VALUES (%s, %s, %s)", (id, name, phone_number))

conn.commit()
