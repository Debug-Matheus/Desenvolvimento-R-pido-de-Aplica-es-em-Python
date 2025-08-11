# Importação biblioteca sistema operacional
import os
# Abrindo o arquivo
arquivo1 = open("dados1.txt", "w", encoding="utf8")

# Exibindo atributos do arquivo
print('Nome do arquivo: ',arquivo1.name)
print('Modo de abertura: ',arquivo1.mode)
print('Arquivo fechado: ',arquivo1.closed)

# Escrevendo no arquivo
arquivo1.write("Olá, mundo!!!")
exit()

# Fechando o arquivo
arquivo1.close()

# Exibindo atributos do arquivo
print('Arquivo fechado: ',arquivo1.closed)

# Caminho absoluto e relativo
print(os.path.abspath(arquivo1.name))
print(os.path.realpath(arquivo1.name))