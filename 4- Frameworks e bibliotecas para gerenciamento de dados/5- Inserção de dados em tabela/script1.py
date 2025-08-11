import sqlite3 as conector
from  modelo import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()   

# Execução de um comando SELECT... CREAT
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    VALUES (12345678900, 'Joaquim', '2000-01-01', 1);'''

cursor.execute(comando)


# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()