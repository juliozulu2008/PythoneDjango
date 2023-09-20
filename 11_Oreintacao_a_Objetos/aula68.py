"""
Herança Simples
"""


class Pessoa:

    # Classe base na herança recebe o nome de superclasse
    def __init__(self, nome, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Classe pessoa")

    def imprimir_nome(self):
        return self.nome


class Aluno(Pessoa):  # Modo de fazer a herança( extends )
    # Quem vai herdar recebe o nome de subclasse

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = None
        print("Classe aluno")

    @staticmethod
    def estudar():
        return "Estudando..."


class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []

    @staticmethod
    def lecionar():
        return "Ensinando..."


aluno1 = Aluno("JULIO")
professor1 = Professor("Xavier")
print(aluno1.estudar())
print(professor1.lecionar())

print(aluno1.nome)
print(professor1.nome)
