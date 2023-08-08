# r - leitura
# a - append - adicionar
# w - escrita 
# x - criar arquivo
# r+ - leitura e escrita

#open("caminho","r")

import os

if os.path.exists("./aula12/text2.txt"):
    os.remove("./aula12/text2.txt")
else:
    print("Arquivo nao existe")