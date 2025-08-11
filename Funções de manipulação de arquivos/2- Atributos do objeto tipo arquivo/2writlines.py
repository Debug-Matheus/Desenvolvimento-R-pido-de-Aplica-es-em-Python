linhas = ["Conteudo da primeira linha", " \n Conteudo da segunda linha"]

arquivo_escrita = open("dados_write.txt", "w", encoding="utf8")

arquivo_escrita.writelines(linhas)

arquivo_escrita.close