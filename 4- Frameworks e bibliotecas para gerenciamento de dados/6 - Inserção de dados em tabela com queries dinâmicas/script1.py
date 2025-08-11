import sqlite3 as conector
from  modelo import Pessoa

# Abertura da conexão e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()   

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(14345678901, 'Matheus', '2000-01-01', False)

# Definição de uma comando com query parameter
comando = '''
INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (?, ?, ?, ?);'''
cursor.execute(comando,(pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
