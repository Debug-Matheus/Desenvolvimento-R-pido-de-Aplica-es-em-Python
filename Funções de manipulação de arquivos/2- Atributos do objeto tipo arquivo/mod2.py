# Importação biblioteca sistema operacional
import os

arquivo1 = open("dados1.txt", "w", encoding="utf8")
print(os.path.abspath(arquivo1.name))
arquivo1.write("Olá, mundo!!!")

print(os.path.realpath(arquivo1.name))
print(arquivo1)
print(arquivo1.name)
arquivo1.close()
