arquivo= open("dados1.txt", "r", encoding="utf8")

conteudo = arquivo.read()
print("Todo conteudo do arquivo:")
print(repr(conteudo), "\n")

arquivo.close