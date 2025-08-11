with open ('dados.txt', 'r', encoding="utf-8") as arquivo:
    texto = arquivo.read()
    contador = texto.count('Olá')
    print("Total de Ola: ", contador)