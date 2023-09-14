"""Operadores Logicos"""

# Tipo Boolean: True e False

a = 10
b = 5
print(a < b) # o print é false porque 5 nao é maior que 10
print(a > b)

if a > b and b < 0:
    print(f"O valor de {a}, é maior que {b}, e maior que 0")

if a > b or b < 0:
    print(f"O valor de {a}, é maior que {b}, e maior que 0")

if not a > b :
    print(f"O valor de {a}, é maior que {b}, exemplo utilizando o NOT")
