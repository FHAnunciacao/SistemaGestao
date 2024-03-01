import sqlite3
# Conexão com o banco de dados e coloquei o CPF como unico.
conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    CPF TEXT NOT NULL UNIQUE,    
    Usuario TEXT NOT NULL UNIQUE,
    Senha TEXT NOT NULL
)
""")

print('Conectado com o Banco de dados')