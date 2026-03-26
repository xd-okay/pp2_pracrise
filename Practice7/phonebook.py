        
import psycopg2

db_db="prac7"
db_user="postgres"
db_pass="Aldiyar"

conn = psycopg2.connect(f"dbname={db_db} user={db_user} password={db_pass}")

cur = conn.cursor()
cur.execute("CREATE TABLE phonebook1 (id serial PRIMARY KEY, name VARCHAR, number_ph VARCHAR)")

id=0

with open('contacts.csv', 'r', encoding='utf-8') as f:
    for line in f:
        line1=line.strip()
        id+=1
        a=list(line1.split(";"))
        print(f"{a[0]} | {a[1]}")
        
        cur.execute("INSERT INTO phonebook1 (id, name, number_ph) VALUES (%s, %s, %s)", (id, a[0], a[1]))
        
cur.execute("SELECT * FROM phonebook1")

rows=cur.fetchall()

print(rows)        
        
conn.commit()