from datetime import date

class Paciente:
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome 
        self.idade = idade 
        self.cpf = cpf 
        self.email = email

    
    @classmethod
    def IdadeAnoNascimento(cls, nome, anoNacimento, cpf, email):
        idade = date.today().year - anoNacimento
        return cls(nome, idade, cpf, email)

class Medico:
    pass
       

p1 = Paciente.IdadeAnoNascimento("Mona lisa", 1994,"000-000-000-00", "mona@gmail.com")
print(p1.__dict__)
print(p1.IdadeAnoNascimento)