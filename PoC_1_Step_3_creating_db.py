import sqlite3

#Creating sqlite table
def creating_database(database_name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
