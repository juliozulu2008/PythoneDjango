"""
Exercicio - Trocar Variaveis  em Python
"""
x = input("Insira o valoe da varivael x: ")
y = input("Insira o valoe da varivael y: ")

temp = x
x = y
y = temp
print(f"O valor de x depois da troca é = {x}")
print(f"O valor de y depois da troca é = {y}")
