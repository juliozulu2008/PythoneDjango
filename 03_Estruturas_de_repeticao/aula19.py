"""
Como achar o fatorial de um numero
"""
# exemplo de fatorial 4! = 4*3*2*1 outro exemplo 9! = 9*8*7*6*5*4*3*2*1 e 0! = 1 e 1! = 1

numero = int(input("Digite um numero para acharmos seu fatorial: "))

fatorial = 1

if numero < 0:
    print("Não existe fatorial de numero negativos!")
elif numero == 0:
    print(f"O fatorial de {numero} eh 1")
else:
    for x in range(1,numero+1):
        fatorial *= x
    print(f"O fatorial de {numero} é : {fatorial}")


