import time

print("---------------------------------------------")
nome = input("digite seu nome: ")
end = input(f"{nome}, digite seu endereco: ")
idade = int(input(f"{nome}, digite sua idade: "))
cpf = int(input(f"{nome}, digite seu CPF: "))
print("---------------------------------------------")

nasc = 2023 - idade

time.sleep(2)

print(f"Seu nome: {nome}")
print(f"Seu endereco: {end}")
print(f"Sua idade: {idade}")
print(f"Seu nascimento: {nasc}")
print(f"Seu cpf: {cpf}")
print("---------------------------------------------")
