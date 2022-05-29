import mysql.connector

def connection():
    connDb = mysql.connector.connect(
        user='root',
        password='freebord2912',
        host='127.0.0.1',
        database='virtual_assistant',
        port='3306')
    return connDb