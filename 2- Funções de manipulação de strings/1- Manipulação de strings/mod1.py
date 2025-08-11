arquivo = open('dados.txt', 'r', encoding="utf-8")

conteudo = arquivo.readline()

print("Tipo do Conteudo: ", type(conteudo))
print("Conteudo retornado pelo read: ", conteudo)
print(repr(conteudo))
proximo_conteudo = arquivo.readline()
print("proximo conteudo retornado:")
print(repr(proximo_conteudo))
arquivo.close()