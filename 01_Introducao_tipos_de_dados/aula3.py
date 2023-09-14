"""Catsing"""

x=1
y=2.9
z="99"

resultado = x + y

print(resultado)
res2 = y + int(z)
print(res2)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Digite seu nome: ")
nome = input()
print(f"{nome}, agora digite sua idade: ")
idade = int(input())
print(nome)
print(nome.__class__)
print(idade)
print(idade.__class__)