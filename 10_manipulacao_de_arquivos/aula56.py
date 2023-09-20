"""
Leitura de arquivo de texto simples
"""

arq = open("./MAOIEEE/texto.txt")
print(arq.read()) # lendo dadaos do arquivo
arq.close()
#################################
'''
outra maneira de abrir arquivos- Forma pytoniana
'''


with open("./MAOIEEE/texto.txt") as txt:
    print(txt.read())
