"""
Continue e Pass
"""

for x in range(10):
    if x == 3:
        continue # nesse caso nao vai ser exibido o numero 3 ele pula o laço
    print(x)

if x == 5:
    pass # pass ignora os erros e faz o programa ou laço seguir
print("Cuidado ao usar pass")
