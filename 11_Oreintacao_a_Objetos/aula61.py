"""
Paradigma imperativo - ex Fortran - Sequencia , Decisão e Iteração
Paradigma Estruturado - C - Estrutura de dados.
Paradigma Procedural - Python - Funções
"""

# paradigma iperadtivo
def registrar(nome, idade, cpf, email):
    paciente = {
        "nome" : nome,
        "idadde" : idade,
        "Cpf" : cpf,
        "email" : email
    }
    return print(paciente)


registrar()

# paradigma orintado a Objetos
"""
Classe - Um conjuto de objetos com as mesma cracteristicas
Objeto - Representaçao do mundo real como um tipo de dado da classe
Construtor - Construtor é uma funçao com o mesmo nome da classe criado internamente pelo python
             Toda vez quq é chamado o construtor é criado um Objeto
             Estanciar um objeto é passar o valor do objeto para uma variavel
Atrubuto - Variaveis de uma Classe 
"""


class Paciente:
    def __init__(self, nome, idade, cpf, email):  # Construtor # self faz referencia aos atributos da propria classe
        self.nome = nome # em outras lingugens seria a Palavra THIS
        self.idade = idade  # self.(nome) atributos e do outro lado a as variaveis
        self.cpf = cpf
        self.email = email


#Reuso e coesão
# Acoplamento, herança, polimorfismo Gap semantico