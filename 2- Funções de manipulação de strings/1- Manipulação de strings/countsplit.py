frase = "Eu amo comer amoras no Café da manhã"

# Resultado obtido utilizando o count
print ("Contagem direta: ", frase.count("amo"))

# Resultado obtido utilizando o split
contador = 0

lista_termos = frase.split()
for termo in lista_termos:
    if termo == "amo":
        contador += 1
print ("Contagem utilizando split: ", contador)