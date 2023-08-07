# for dentro de outro for

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for linha in matrix_numeros:
    #print(linha)
    print("---")
    for coluna in linha:
        print(coluna)