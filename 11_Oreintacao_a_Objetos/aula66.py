"""
Getters e Setters
"""

# Forma basica de fazer getter e setter
class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self._idade = idade
        self.__matricula = matricula
        self.__notas = None

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return  self._idade

    def set_idade(self, idade):
        self._idade = idade

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_notas(self):
        return self.__notas

    def set_notas(self, notas):
        self.__notas = notas



aluno1 = Aluno("José", 15, 122)
print(aluno1.get_nome())

