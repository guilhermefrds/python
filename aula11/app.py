try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError:
    print("Divizao por 0 nao e possivel")
except ValueError:
    print("Digite um valor valido")
except:
    print("Erro inesperado")
finally:
    print("Sempre executa")