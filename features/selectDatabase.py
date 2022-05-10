from database_connection.connectiondb import connection
from features.talk_feature import talk
from formatter_voice_input.formatter_rec import formatter

def selectDatabase(keyword):
    keyword = formatter(keyword)
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
        talk(row[1])
    except:
        print("Database connection error")
    finally:
        conn.close()
    return row[1]