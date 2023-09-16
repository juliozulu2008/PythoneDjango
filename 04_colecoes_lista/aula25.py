"""
slicing
"""
#index 0 1  2  3  4  5  6
l1 = [1, 2, 3, 4, 5, 6, 7]

print(l1[-1]) #inverte a order de impressao do array no caso vai ser impresso o "4"
print(l1[::]) # exibe todos
print(l1[1:]) # exibi desde o primeiro elemento ate o ultimo
print(l1[2:]) # exibi desde o segundo elemento ate o ultimo
print(l1[:3]) # exibi desde o Primeiro elemento ate o terceiro
print(l1[2:4]) # apenas elemedos do index 2 ate o 4
print(l1[1:4:2]) # apenas elemedos do index 2 ate o 4

nome = "Julio Cesar"
print(nome[1:3:6])
