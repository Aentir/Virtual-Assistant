import mysql.connector

def databaseInfo():

    connDb = mysql.connector.connect(
        user='root',
        password='freebord2912',
        host='127.0.0.1',
        database='virtual_assistant',
        port='3306')
    print(connDb)

    cursor = connDb.cursor()
    cursor.execute("SELECT * FROM learning WHERE idlearning='9'")


    for x in cursor:
        print(x[1])
    
    return x[1]



def insertDatabase():
    connDb = mysql.connector.connect(
        user='root',
        password='freebord2912',
        host='127.0.0.1',
        database='virtual_assistant',
        port='3306')
    
    cursor = connDb.cursor()
    cursor.execute("INSERT INTO learning (description) VALUES ('test')")
    connDb.commit()
    
#insertDatabase()
databaseInfo()