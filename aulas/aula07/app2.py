def fazer_big_mac(nome):
    print(f"Sanduiche Big Mac {nome}")

#fazer_big_mac("Guilherme")
#fazer_big_mac("Madalena")
#fazer_big_mac("Gildenei")
#fazer_big_mac("Gustavo")
#fazer_big_mac("Mayara")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo, tamanho):
    print(f"Refrigerante {tipo}, {tamanho}.")
def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri) 

def soma_numeros(num1, num2):
    return num1 + num2


resultado = soma_numeros(15, 20)
print(resultado)

def maior_numero(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_numero = lista_num[0]
    return maior_numero

resultado = maior_numero([234324,43,4,3,4345,646436,-643643,6436])

print(resultado)