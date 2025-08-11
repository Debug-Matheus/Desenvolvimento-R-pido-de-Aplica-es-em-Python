import sqlite3 as conector

# Abertura da conexão
conexao = conector.connect("URL SQLite")

#Aquisição do cursor
cursor = conexao.cursor()

# Execução comandos SELECT.. CREAT..
cursor.execute("...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()