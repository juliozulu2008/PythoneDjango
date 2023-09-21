"""
Polimorfismo
"""
"""
é uma caracteristica da herança
é a Forma de executar o mesmo metodo, de diferentes maneiras
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

    def trabalhar(self):  # Um Metodo com pass na Super class
        pass


class Administrador(Pessoa):
    def trabalhar(self):  # Metodos com nome igual na sub-classe
        nome_classe = self.__class__.__name__  # Referenciando a classe a qual o metodo esta alocado
        return f"Classe  {nome_classe} Supervisionando..."  # polimorfismo


def estudar():
    return "Estudando..."


class Aluno(Pessoa):  # Modo de fazer a herança( extends )
    # Quem vai herdar recebe o nome de subclasse

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = None
        print("Classe aluno")


class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []

    def trabalhar(self):  # Metodos com nome igual na sub-classe
        nome_classe = self.__class__.__name__  # Referenciando a classe a qual o metodo esta alocado
        return f"Classe  {nome_classe} Ensinando..."  # polimorfismo


aluno1 = Aluno("JULIO")
professor1 = Professor("Xavier")
adm = Administrador("Joao")
print(professor1.trabalhar())
print(adm.trabalhar())
