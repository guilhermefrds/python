# for

print("-----------------------")

criancas = ["Guilherme", "Mayara", "Gustavo"]

for index in range(5):
    if index == 0:
        print("Primeira linha")
    else:
        print(f"outras linhas {index}")

print("-----------------------")

for item in criancas:
    print(item)
    
print("-----------------------")

for index in range(len(criancas)):
    print(criancas[index],index)
    

print("-----------------------")

canal = "Refatorando"

for letra in canal:
    print(letra)

print("-----------------------")

for index in range(0,20,2):
    print(index)

print("-----------------------")
