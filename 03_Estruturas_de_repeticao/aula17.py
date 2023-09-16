"""
do while * nao existe mas tem como fazer KKKKK
"""
palpite = 0
numero = 9

while True: # se deixarmo o while true, ele vira um do while
    print("Tente adivinha qual o numero correto? ")
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero:
        print("Parabens!")
        break
    else:
        print("Tente novamente!")

