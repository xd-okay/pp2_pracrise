import config
import psycopg2



conn = psycopg2.connect(f"dbname={config.db_db} user={config.db_user} password={config.db_pass}")
