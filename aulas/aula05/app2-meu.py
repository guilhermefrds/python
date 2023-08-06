#importando biblioteca de time, para utilizar a funcao "sleep"
import time

# informando o usuario oque o script faz
print("""Este e um script de calculadora, ele ira calcular todas 
as operacoes com os numeros que forem disponibilizado a ele""")


time.sleep(2)
# coleta de dados do usuario
print("--------------------------------------------------")
num1 = int(input("Digite um numero para ser calculado: "))
num2 = int(input("Digite o segundo numero para ser calculado: "))
print("--------------------------------------------------")
print(f"Os numeros escolhidos foram: {num1} e {num2}!")
print("--------------------------------------------------")

# campo de operacoes
resmenos = num1 - num2
resmais = num1 + num2
resx = num1 * num2
resdiv = num1 / num2
time.sleep(2)

# informando ao usuario, todas as operacoes possiveis
print(f"Subtraindo:         {num1} - {num2} = {resmenos}")
print(f"Adicionando:        {num1} + {num2} = {resmais}")
print(f"Multiplicando:      {num1} x {num2} = {resx}")
print(f"Dividindo:          {num1} / {num2} = {resdiv}")
print("--------------------------------------------------")