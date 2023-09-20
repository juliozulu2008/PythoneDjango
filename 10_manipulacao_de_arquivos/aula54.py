import os

# verificar se um arquivo e diretorio existe
print(os.name)
print(os.path.exists("texto.py"))
print(os.path.exists('teste.txt'))

# Exemplo de caminhos
print(os.path.exists("teste/teste.txt"))

#Criando arquivos
# os.mknod("Maoie.py")

#  comandos windows
print(os.getcwd()) # retorna diretorio windows
# # os.mkdir("JULIO") # cria diretorio Windows
# os.mkfifo("./curspdepythonedjango/JULIO") # cria diretorio Windows
# # os.removedirs("JULIO") # deleta Diretorio windows
# print(os.listdir()) # lista arquivos no diretorio
arquivo = open("../teste/teste.txt", 'w')
arquivo.writelines("Ola mundo!")
arquivo.close()
