import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()