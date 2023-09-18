"""
Kwargs # argumentos nomeados
"""


def nomes(**nomes):
    print(f"{nomes}")


nomes(nomes="Julio", sobrenome="Dias", idade=27) # ele permite que se passe mais argmentos e salva em um dicionario
