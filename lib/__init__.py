import sqlite3

# Establish a connection to the music.db database
CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()
