"""
Modulo - Nomes de grupo de arquivos em python
"""


print(50*"===============")


def primo(numero):
    if numero > 1:
        for x in range(2, numero):
            if(numero % x) == 0:
                print("Esse Numero nao é Primo")
                break
            else:
                print(f"Esse numero é Primo {numero}")
    else:
            print("Esse numeor nao é primo: Numero menor ou igaul a 1")



print(50*"===============")
