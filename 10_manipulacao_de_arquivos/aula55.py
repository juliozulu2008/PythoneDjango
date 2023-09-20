"""
renomeado arquivos
"""


import os


os.mkdir("JULIO")
arquivo = "arquivo.txt"

with open(arquivo, 'w') as arquivo:
    pass

print(f"O arquivo {arquivo} foi crado com sucesso!")
os.rename("JULIO", "MAOIEEE") # nome atual e nome que vai ser
os.renames("./arquivo.txt", "MAOIEEE/texto.txt")
