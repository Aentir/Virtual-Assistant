from contextlib import nullcontext
from database_connection.connection_db import connection
from voice_config.talk_feature import talk

def get_all_notes(rec = nullcontext):
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM learning")
        result = cursor.fetchall()
        if len(result) != 0:
            for row in result:
                print(row)  
                talk(row[1])
        else:
            talk("No tienes notas guardadas")
    except:
        print("Database connection error")
    finally:
        cursor.close()
        conn.close()
    return row


def get_last_note(rec = nullcontext):
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT description FROM learning ORDER BY idlearning DESC LIMIT 1")
        result = cursor.fetchone()
        if len(result) != 0:
            for row in result:
                print(row)  
                talk(row)
        else:
            talk("No tienes notas guardadas")
    except:
        print("Database connection error")
    finally:
        cursor.close()
        conn.close()
    return result