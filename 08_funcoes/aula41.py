l1 = [1,2,3,4,5,6,7]
print(l1)
l1.pop
print(l1)
var1 = l1.pop()
print(var1)

def ola_mundo():
    print("Ola mando")

v1 = ola_mundo() # o retorno da funçao print é none
print(v1)

def ola_mundov2():
    return "Ola Mundo"


print(70*"=")
v2 = ola_mundov2()
print(v2) # Ja qui com o retorno da função é a string "Ola mundo"
print(70*"=")

numbers = int(input("Digite um numero para saber se ele é por ou inmpar: "))
def par_impar():
    if (numbers % 2) == 0:
        print("o numero é par")
    else:
        print("o numero é impar")

par_impar()
print(70*"=")
# o return sai da funçao
