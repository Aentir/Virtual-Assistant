from database_connection.connectiondb import connection
from formatter_voice_input.formatter_rec import formatter

def insert_database(info):
    info = formatter(info)
    print(info)
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO learning (description) VALUES ('{0}')".format(info))
        conn.commit()
    except:
        print("Database connection error")        
    finally:
        conn.close()