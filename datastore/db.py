import sqlite3
from datetime import datetime,date
import pathlib

DATASTORE_PATH = pathlib.Path(__file__).parent.absolute()
class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATASTORE_PATH / 'database.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        table = """ CREATE TABLE  IF NOT EXISTS servers (
            ip TEXT NOT NULL,
            date timestamp
        ); """
        self.cursor.execute(table)

    def insert_into(self,ip):
        self.cursor.execute("INSERT INTO servers VALUES (?,?);", (ip, date.today()))
        self.conn.commit()

    def list_servers(self):
        rows = self.cursor.execute("SELECT * FROM servers;")
        return rows.fetchall()