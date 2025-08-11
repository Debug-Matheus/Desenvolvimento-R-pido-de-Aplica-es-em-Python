import os

arquivo = open("dados1.txt", "r", encoding="utf8")

conteudo = arquivo.read()

print('Tipo do conteudo', type(conteudo))
print('Conteudo retornado pelo read:')
print(repr(conteudo))
arquivo.close()
