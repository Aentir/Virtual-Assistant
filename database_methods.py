from database_connection.connectiondb import connection

def updateDatabase(descript):
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE learning SET description = '{0}' WHERE key_word = 'macarrones'".format(descript))    # .format da formato de "tupla", necesario para el INSERT
        conn.commit()
    except:
        print("Database connection error")
    finally:
        conn.close()
        
        
def setKeyWordDatabase(info):
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO learning (key_word) VALUES ('{0}')".format(info))
        conn.commit()
    except:
        print("Database connection error")
    finally:
        conn.close()
        

    