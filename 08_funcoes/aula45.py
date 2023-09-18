"""
Parametros de uma função
"""


def nome_da_funcao(parametro):  # Parametro é o nome dado aos valores Utilizados nas definição de uma funçao
    # Corpo da Função
    print(parametro)


nome_da_funcao("JULIO")  # Argumento é o nome dado aos valores utilizados na chamada de uma função

def nova(nome,sobrenome,idade):
    return print(f"Ola {nome} {sobrenome}, voçe tem {idade}")

nova("julio", "cesar", 27)
