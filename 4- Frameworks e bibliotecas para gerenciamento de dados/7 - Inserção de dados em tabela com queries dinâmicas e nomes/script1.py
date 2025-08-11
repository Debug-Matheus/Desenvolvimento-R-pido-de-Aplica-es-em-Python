import sqlite3 as conector
from  modelo import Pessoa

# Abertura da conexão e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()   

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(24355978901, 'Danielle', '1990-01-01', False)

# Definição de uma comando com query parameter
comando = '''
INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''
cursor.execute(comando,{"cpf": pessoa.cpf,  "nome": pessoa.nome,  "data_nascimento": pessoa.data_nascimento,  "usa_oculos": pessoa.usa_oculos})

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
