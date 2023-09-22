"""
Herança Múltipla
"""


class Funcionario:
    def trabalhar(self):
        print("Trabalhando")


class FrontEnd(Funcionario):
    def trabalhar(self):
        print("FrontEnd")


class BackEnd(Funcionario):
    def trabalhar(self):
        print("Backend")


class FullStack(FrontEnd, BackEnd): # por padrao ele busca o construtor mas caso nao encontre ele utiliza o 1 indice
    pass


julio = FullStack()
julio.trabalhar()
