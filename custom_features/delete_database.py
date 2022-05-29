from contextlib import nullcontext
from database_connection.connection_db import connection

def delete_database_info(rec = nullcontext):
    try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("TRUNCATE TABLE learning")
            conn.commit()
    except:
        print("Database connection error")
    finally:
        cursor.close()
        conn.close()