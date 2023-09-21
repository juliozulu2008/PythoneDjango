"""
Herança Múltipla
"""


class Pessoa:
    def __init__(self, nome, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Classe pessoa")

    def imprimir_nome(self):
        return self.nome

    def trabalhar(self):
        pass


class Administrador(Pessoa):
    def trabalhar(self):
        nome_classe = self.__class__.__name__
        return f"Classe  {nome_classe} Supervisionando..."


class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = None
        print("Classe aluno")

    def estudar(self):
        return "Estudando..."

class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        return f"Classe  {nome_classe} Ensinando..."


aluno1 = Aluno("JULIO")
professor1 = Professor("Xavier")
adm = Administrador("Joao")
print(professor1.trabalhar())
print(adm.trabalhar())
