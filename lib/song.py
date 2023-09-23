import sqlite3

conn = sqlite3.connect("music.db")
CURSOR = conn.cursor()

class Song:
    def __init__(self, name, album):
        self.id = None  
        self.name = name
        self.album = album

    def save(self):
        CURSOR.execute("INSERT INTO songs (name, album) VALUES (?, ?)", (self.name, self.album))
        conn.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        ''')
        conn.commit()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
