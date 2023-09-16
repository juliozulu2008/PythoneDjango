"""
Programa para saber se o numero é inpar ou par
"""

numero = int(input("Digite um numero para que possamos saber se ele é impar ou par: "))
if (numero % 2) == 0:
    print(f"O {numero} é Par")
else:
    print(f"O {numero}, é impar!")

