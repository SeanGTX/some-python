import keyboard
import os
import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

i = 0

while not keyboard.is_pressed('`'):

    if keyboard.is_pressed('='):
        i += 1
        sql_request = "SELECT * FROM mariam WHERE id = " + str(i)
        link = cursor.execute("SELECT * FROM mariam WHERE id = " + str(i)).fetchall()[0][3]
        os.system("start chrome " + link)

    if keyboard.is_pressed('-'):
        i -= 1
        sql_request = "SELECT * FROM mariam WHERE id = " + str(i)
        link = cursor.execute("SELECT * FROM mariam WHERE id = " + str(i)).fetchall()[0][3]
        os.system("start chrome " + link)
