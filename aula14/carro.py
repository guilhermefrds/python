class Carro:
    def __init__(self,marca,modelo,cor,combustivel):
        self.marca          = marca
        self.modelo         = modelo
        self.cor            = cor
        self.combustivel    = combustivel
        
        self.ligado         = False    
        self.velocidade     = 0
    
    def ligar(self):
        if self.ligado:
            print(f"{self.modelo} ja esta ligado, nada acontece")
        else:
            print(f"{self.modelo} Ligado")
            self.ligado     = True    
        
    def desligar(self):
        if self.ligado:
            print(f"{self.modelo} Desligado")
            self.ligado     = False
        else:
            print(f"{self.modelo} ja esta desligado, nada acontece")
            
    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade}km/h")
        else:
            print("Nao e possivel acelerar, carro esta desligado.")
            
    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade}km/h")
        else:
            print("Nao e possivel frear, carro esta desligado.")
        