import psycopg
from psycopg.rows import dict_row
import dotenv
import os

dotenv.load_dotenv()
print(os.getenv("NEW_URL_SUPABASE"))
def get_db():
    conn = psycopg.connect(os.getenv("NEW_URL_SUPABASE"), row_factory=dict_row)
    try:
        yield conn
    finally:
        conn.close()
