"""
Emcapsulamento
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
        self.__historico = [saldo]

    def extrato(self):
        print("_________EXTRATO__________")
        print(f"___CONTA: {self.titular} _____")
        for saldo in self.__historico:
            print(f"Saldo: R${saldo}")

    def transacao(self, saldo):
        self.__historico.append(saldo)

    def saldo(self):
        print(f"Saldo: R${self.__saldo}")
    def depositar(self, valor):
        self.__saldo += valor
        self.transacao(self.__saldo)

    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)

    def tranferencia(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)


cont1 = Conta(123, "Julio", 69, 100)
cont2 = Conta(456, "Kelly", 68, 7000)

cont1.extrato()
cont2.extrato()
print(30*"________________")
cont2.tranferencia(300, cont1)
cont1.saldo()
cont1.extrato()
cont2.saldo()
cont2.extrato()
print(30*"________________")
