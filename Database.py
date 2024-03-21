import sqlite3
# Conexão com o banco de dados e coloquei o CPF como unico.
conn = sqlite3.connect('DBLoja.db')
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
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    Código INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Referencia TEXT NOT NULL,
    [Descrição do Produto] TEXT NOT NULL,
    [Unidade de Medida] TEXT NOT NULL,
    Marca TEXT NOT NULL,
    [Tipo de Item] TEXT NOT NULL,
    NCM TEXT NOT NULL,
    GTIN TEXT,
    Grupo TEXT NOT NULL,
    SubGrupo TEXT NOT NULL,
    CST TEXT NOT NULL,
    [Alíquota de IPI] DECIMAL(3,2)
    
) 
""")


print('Conectado com o Banco de dados')
