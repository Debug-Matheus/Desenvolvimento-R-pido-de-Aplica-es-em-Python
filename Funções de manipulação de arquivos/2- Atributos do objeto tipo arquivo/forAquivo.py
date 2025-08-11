arquivo = open("dados1.txt", "r", encoding="utf8")

for linha in arquivo:
    print(repr(linha))
arquivo.close    