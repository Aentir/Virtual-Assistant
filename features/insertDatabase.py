from database_connection.connectiondb import connection
from formatter_voice_input.formatter_rec import formatter

def insertDatabase(info):
    info = formatter(info)
    print(info)
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO learning (descripcion) VALUES ('{0}')".format(info))
    except:
        print("Database connection error")        
    finally:
        conn.close()