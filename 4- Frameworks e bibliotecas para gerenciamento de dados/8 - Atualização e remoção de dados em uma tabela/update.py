import sqlite3 as conector

# Abertura de conexão e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()

# Definição dos comandos
# comando1 = '''UPDATE Pessoa SET oculos = 1'''
# cursor.execute(comando1)

# comando2 = '''UPDATE Pessoa SET oculos= ? WHERE cpf = 12345678900'''
# cursor.execute(comando2, (False,))

comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf = :cpf'''
cursor.execute(comando3, {"usa_oculos": True, "cpf": 12345678901})

# Efetivação do comando
conexao.commit()    

# Fechamento das conexões
cursor.close()
conexao.close()