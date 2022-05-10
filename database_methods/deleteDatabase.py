from database_connection.connectiondb import connection

def deleteDatabaseInfo():
    try:
        if connection():
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM learning")
            conn.commit()
    except:
        print("Database connection error")
    finally:
        conn.close()