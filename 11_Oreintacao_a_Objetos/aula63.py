"""
Acoplamanto e Visibilidade
"""
"""
Visubilidade - Modificador de acesso

privada (private) - Restritiva -> definir que atributos e metodo so podem ser manipulados dentro
                    da classe que foram definidos
protejida (protected) - intermediara -> definir que tributos e metodos só podem ser manipulados 
                        nas classes que foram definidos e nas sub classes (herdado)
public (public) - mais aberta -> defini que os tributos ou metodos, podem ou sao acessiveis em 
                                 qualquer parte do codigo.
"""

class Conta:
    @classmethod
    def CodicoBanco(cls):
        print("Codigo 899")

    @staticmethod
    def retornar_num_agencia():
        return "777"

    def __init__(self, numero, titular, agencia, saldo=0):
        self._numero = numero
        self.titular = titular # Visibilidade Publica
        self._agencia = agencia # ao utilizara apenas 1 underline estou dizendo que o metodo é protegido
        self.__saldo = saldo  # ao utiliazr os dois underlines estou dizendo que o metodo é Privado

    def extrato(self):
        print(f"Saldo: R${self.__saldo}")

    def depositar(self):
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        self.__saldo += valor_deposito
        print(f"Foi depositado R${valor_deposito}, seu saldo agora é R${self.__saldo}")

    def sacar(self):
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            print(f"Foi sacado R${valor_saque}, seu saldo agora é R${self.__saldo}")
        else:
            print("Saldo insuficiente para o saque.")


cont1 = Conta(123, "julio", 69)
cont2 = Conta(456, "Kelly", 68, 7000)

print(cont1.titular)
print(cont2.titular)
print(cont2.extrato())

cont2.signo = "Peixes"
print(cont1.__dict__)
print(cont2.__dict__)
del cont2.signo
print(cont2.__dict__)

Conta.CodicoBanco()

cont1.CodicoBanco()

Conta.retornar_num_agencia()

cont1.retornar_num_agencia()
