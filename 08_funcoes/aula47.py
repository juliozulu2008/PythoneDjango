"""
Parametro padrao
"""


def imprimir_nome(nome=None, sobrenome=None, idade=None):
    if nome != None:
        print(f"Nome: {nome}")
        print(f"sobrenome: {sobrenome}")
        print(f"idade: {idade}")
    else:
        print("digite argumentos Validos!!!")


imprimir_nome()
