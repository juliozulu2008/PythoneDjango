"""
Descobrir se um numero é Primo
"""
"""
Os Números Primos são números naturais maiores do que 1 que possuem somente dois divisores,
 ou seja, são divisíveis por 1 e por ele mesmo.
"""
print(50 * "_")

numero = int(input("Insira um numero para descubrir se o memso é primo: "))
if numero > 1:
    for x in range(2, numero):
        if (numero % x) == 0:
            print(f"Print esse nao é um numero primo, {numero}")
            break
    else:
            print(f"Esse numero é primo, {numero}")
else:
    print("esse numero nao é primo: numero menor ou igual a 1")

print(50*"_")
