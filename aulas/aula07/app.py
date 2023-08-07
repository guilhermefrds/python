#def big_mac():
#    print("sanduiche big mac")

#print("Inicio")
#big_mac()
#print("Fim")

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

fazer_big_mac("Gui")
fazer_batata("Grande")
preparar_refrigerante("Soda", "Grande")

print("----------------------------------------------------------------")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri) 

fazer_combo_big_mac("Guilherme","Grande","Soda","Media")