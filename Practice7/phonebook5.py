import psycopg2

db_db="prac7"
db_user="postgres"
db_pass="Aldiyar"

conn = psycopg2.connect(f"dbname={db_db} user={db_user} password={db_pass}")

cur = conn.cursor()
ask=int(input("1 - номер, 2 - имя"))

if( ask==2):
    name=input()
    cur.execute("DELETE * FROM phonebook1 WHERE NAME = %s", (name,))
    
elif(ask==1):
    phone=input()
    cur.execute("DELETE * FROM phonebook1 WHERE number_ph = %s", (phone,))


conn.commit()