# r - leitura
# a - append - adicionar
# w - escrita 
# x - criar arquivo
# r+ - leitura e escrita

#open("caminho","r")

arquivo = open("./aula12/text.txt","r")

print(arquivo.readable())
print(arquivo.read())
print(arquivo.readline())

lista = arquivo.readlines()

print(lista)

print(lista[3])

arquivo.close()