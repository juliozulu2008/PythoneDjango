class Conta:
    #atributo de Classe
    taxa = 0.35
    #Metodo de classe
    @classmethod
    def CodicoBanco(cls):
        print("Codigo 899")

    #Metodo statico
    @staticmethod # Nao sabe nada da Classe
    def retornar_num_agencia():
        return "777"
    


    #Atributo de instancia - Sao presos ao metodo construtor.
    def __init__(self, numero, titular, agencia, saldo=0): # agora atribui um valor inical de 0 a Saldo se for mencionado o mesmo vai inicçao com o valor, se nao vai ser 0
        self.numero = numero
        self.titular = titular
        self.agencia = agencia
        self.saldo = saldo

    def extrato(self):
        self.saldo -= Conta.taxa # nome da classe e atributo quando for atributo de classe
        print(f"Saldo: R${self.saldo}")

    def depositar(self):
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor_deposito
        print(f"Foi depositado R${valor_deposito}, seu saldo agora é R${self.saldo}")

    def sacar(self):
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            print(f"Foi sacado R${valor_saque}, seu saldo agora é R${self.saldo}")
        else:
            print("Saldo insuficiente para o saque.")


# Instancia do Objeto
cont1 = Conta(123, "julio", 69)
cont2 = Conta(456, "Kelly", 68, 7000)

print(cont1.titular)
print(cont2.titular)
print(cont2.extrato())

# Atributo Dinamico
cont2.signo = "Peixes" # dinamicamente alocado a intancia da Conta 2 "cont2" só exixte m tempo de execução
print(cont1.__dict__)
print(cont2.__dict__)
del cont2.signo 
print(cont2.__dict__)

#Metodo da Classe
Conta.CodicoBanco() # Convenção --- Forma correta
# Tambem pode se fazer usnado um instancia da classe
cont1.CodicoBanco()

# Metodo Estatico
Conta.retornar_num_agencia() # Convenção --- Forma correta
# Tambem pode se fazer usnado um instancia da classe
cont1.retornar_num_agencia()