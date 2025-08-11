import sqlite3 as conector

# Abertura da conexão e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando SELECT... CREAT
comando = '''
ALTER TABLE Veiculo 
    ADD motor REAL;
'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()