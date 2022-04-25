from connectiondb import connection


def selectDatabase(keyword):
    #id = id
    try:
        conn = connection()
        cursor = conn.cursor()
        #cursor.execute("SELECT * FROM learning WHERE idlearning=" + str(id) + ";")  #Necesaria conversión de int a str
        #cursor.execute("SELECT * FROM learning WHERE key_word='macarrones';")
        cursor.execute("SELECT * FROM learning WHERE key_word='{0}'".format(keyword))
        result = cursor.fetchall()
        for row in result:
            print(row[1])
        #print(id)
    except:
        print("Database connection error")
    finally:
        conn.close()
    return row[1]
    
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
    