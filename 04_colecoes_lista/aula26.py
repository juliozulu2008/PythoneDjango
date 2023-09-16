"""
Funçoes, concatenar listas
"""
l1 = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
l2 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
l3 = l1 + l2
print(60*"==")
print(l1)
print(60*"==")
print(l2)
print(60*"==")
print(l3)
print(60*"==")
#Funçao Len de length - Tamanho
print(len(l3))
print(10*"++++++++++++++++++++")
"""
Funçoes que só podem ser usadar com dados numericos
"""
print("Funçoe somente com numeros!")
print("funçao sum")
print(sum(l3)) # somatorio da lista 3
print(60*"==")
print("Funçao max")
print(max(l3)) # maior valor de um elemento da lista
print(60*"==")
print("funçao min")
print(min(l3)) # menor valor de um elemento da lista
"""
Funçoes uteis para utilizar com a listas
"""

nome = "JULIO CESAR"
valor = range(10)


print(nome)
print(valor)

l4 = list(range(10))
print(l4) # tranformou a funçao range em uma lista

l5 = list(nome)
print(l5) #tranformou o valor da variavel "nome" em uma lista

l6 = list("123456789")
print(l6)

elemento = "J"
if elemento in nome:
    print(elemento)
else:
    pass
