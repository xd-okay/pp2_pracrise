import psycopg2
import connect


cur = connect.conn.cursor()

cur.execute("CALL upsert_contact('            Ильяс', '+7123456789');")

cur.execute("""CALL upsert_contacts(ARRAY[
        ('Adil', '+7890')::user_data, 
        ('Bekassyl', '+7654')::user_data, 
        ('Dimash', '+890890')::user_data
    ]);""")



cur.execute("SELECT * FROM public.phonebook1")
rows=cur.fetchall()
print(rows)

connect.conn.commit()

cur.close()
connect.conn.close()