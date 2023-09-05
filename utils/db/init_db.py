import sqlite3
import logging

sqliteConnection = sqlite3.connect('./utils/db/iris.db')
cursor = sqliteConnection.cursor()
logging.info("Database created and Successfully Connected to SQLite")
sqlite_select_Query = "select sqlite_version();"
cursor.execute(sqlite_select_Query)
record = cursor.fetchall()
logging.info("SQLite Database Version is: ", record)
cursor.close()