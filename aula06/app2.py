familia = ["Madalena","Gildenei","Gustavo","Mayara","Guilherme"]

#print(familia)
# substituindo o index(3) por outro nome, de Mayara por Yasmin
#familia[3] = "Yasmin"
#familia[3] = "Mayara"
print(familia)

# adiciona um item a lista selecionada
familia.append("Yasmin")
print(familia)

# adiciona um item no local selecionado da lista
familia.insert(0,"Yasmin")
print(familia)

# extende a lista adicionando outra lista para com ela
familia.extend(["Dori","Jubart"])
print(familia)

# remove o ultimo index da lista 
familia.pop()

#remove o item selecionado da lista
familia.remove("Gustavo")
print(familia)


# limpar lista 
familia.clear()
print(familia)