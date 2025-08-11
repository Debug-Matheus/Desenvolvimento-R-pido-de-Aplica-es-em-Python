
arquivo = open ("dados1.txt", "r", encoding="utf8")

conteudo = arquivo.readline()

print('Tipo do conteudo', type(conteudo))

print("Conteudo retornado pelo readline:")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("ProximoConteudo retornado pelo readline:")
print(repr(proximo_conteudo))

arquivo.close