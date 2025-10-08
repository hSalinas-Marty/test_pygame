import pygame
import sqlite3

class Database:
    DB_file = "sauvegardes.db"

    def __init__(self):
        conn = sqlite3.connect(self.DB_file)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS parties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pseudo TEXT NOT NULL,
                score INTEGER,
                niveau INTEGER,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def sauvegarder_partie(self, pseudo, score, niveau):
        conn = sqlite3.connect(self.DB_file)
        c = conn.cursor()
        c.execute("INSERT INTO parties (pseudo, score, niveau) VALUES (?, ?, ?)",
                (pseudo, score, niveau))
        conn.commit()
        conn.close()
    
    def charger_partie(self, pseudo):
        conn = sqlite3.connect(self.DB_file)
        c = conn.cursor()
        c.execute("SELECT score, niveau FROM parties WHERE pseudo=? ORDER BY date DESC LIMIT 1", (pseudo,))
        row = c.fetchone()
        conn.close()
        return row