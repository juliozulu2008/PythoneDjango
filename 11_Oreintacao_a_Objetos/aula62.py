"""
Abstração

Abstraçao é a ideia de generalizar as caracteristicas que os objetos tem em comum
"""

"""
Classe - Um conjuto de objetos com as mesma cracteristicas
Objeto - Representaçao do mundo real como um tipo de dado da classe
Construtor - Construtor é uma funçao com o mesmo nome da classe criado internamente pelo python
             Toda vez quq é chamado o construtor é criado um Objeto
             Estanciar um objeto é passar o valor do objeto para uma variavel
Atrubuto - Variaveis de uma Classe 
"""
"""
CLASSE

Classe é uma estrutura que abstrai um conjunto de objetos com caracteriosticas
similares. definindo o comportamento dos seus objetos atraves das estruturas:

1- Atributos
2- Metodos

A classe define um tipo de dado Abstato

"""
"""
Conseitos Fundamentais

-Abstração

Processo pelo qual se isolam atributos de umm objeto,
considerando os que certos grupos de objetos tenham em comum.

-Reuso

Não exixte pior pratica em programaçao do que repetir codigo.


"""



class Paciente:
    def __init__(self, nome, idade, cpf, email):  # Construtor # self faz referencia aos atributos da propria classe
        self.nome = nome # em outras lingugens seria a Palavra THIS
        self.idade = idade  # self.(nome) atributos e do outro lado a as variaveis
        self.cpf = cpf
        self.email = email