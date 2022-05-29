from database_connection.connection_db import connection
from formatter_voice_input.formatter_rec import formatter
from voice_config.talk_feature import talk

def insert_database(info):
    info = formatter(info)
    print(info)
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO learning (description) VALUES ('{0}')".format(info))
        conn.commit()
        talk("He apuntado" + info)
    except:
        print("Database connection error")        
    finally:
        cursor.close()
        conn.close()