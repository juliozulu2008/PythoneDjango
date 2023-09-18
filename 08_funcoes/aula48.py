"""
ARGS - Argumento arbitrario
"""


# Urilizado args quando nao se sabe o num de agumentos que se vai receber *args - guarda tudo em uma tupla
def minha_funcao(ling, tipo, numvgas, *args):
    print(f"{ling}")
    print(f"{tipo}")
    print(f"{numvgas}")


minha_funcao(1, 2, 3, 6, 7, 8)


def f1(*sim):
    print(f"{sim}")


f1(*"dois", "tres", "quatro", "cenco") #permite mais argumentos e salva como uma tupla
