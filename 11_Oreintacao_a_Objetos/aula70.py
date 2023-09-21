"""
Classes Abstratas
"""

from abc import ABC, abstractmethod


# Classe abstrata

# para um aclasse ser considerada abtsrara ela deve ter metotos abstratos
class Pessoa(ABC):  # não se deve criar Objetos de Classe Abstrata.
    def __init__(self, nome, idade=None, cpf=None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @abstractmethod  # Com esse metodo não é mais possivel instanciar a classe
    def trabalhar(self):
        pass


# Classe Concreta
class Trabalhador(Pessoa):
    def __init__(self, nome, idade, cpf, trabalho):
        super().__init__(nome, idade, cpf)
        self.trabalho = trabalho

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        return f" Eu {nome_classe} estou trabalhando"


t1 = Trabalhador("Julio o Brabo", 70, "000", "Desenvolvedor")
print(t1.nome)
print(t1.idade)
print(t1.cpf)
print(t1.trabalho)
print(t1.trabalhar())
print(30*"_________")
t1.trabalhar()
