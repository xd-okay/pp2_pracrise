import psycopg2

db_db="prac7"
db_user="postgres"
db_pass="Aldiyar"

conn = psycopg2.connect(f"dbname={db_db} user={db_user} password={db_pass}")

cur = conn.cursor()

name1=input()
name2=input("На что поменять?")
cur.execute("UPDATE phonebook1 SET name=%s WHERE name=%s", (name2,name1))

print(f"Изменено {cur.rowcount} строк")


# result=cur.fetchone()[0]
# print(result)
conn.commit()