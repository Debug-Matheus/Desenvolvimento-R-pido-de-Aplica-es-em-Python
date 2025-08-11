import sqlite3 as conector

# Abertura de conexão e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()

# Definição  dos comandos
comando = '''DELETE FROM Pessoa WHERE cpf = 12345678900'''
cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()

