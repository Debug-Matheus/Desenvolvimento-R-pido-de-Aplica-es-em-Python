arquivo = open("dados1.txt", "r", encoding="utf8")

conteudo = arquivo.readlines()

print("Tipo do conteudo", type(conteudo))

print("Conteudo retornado pelo readlines:")
print(repr(conteudo))

arquivo.close
