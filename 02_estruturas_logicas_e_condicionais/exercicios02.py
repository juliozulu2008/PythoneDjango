idade = int(input("Digite sua idade: "))

if idade < 16:
    print(f"menor")
elif idade >= 16 and idade <= 18:
    print(f"Emancipado")
else:
    print(f"Maior")

idade2 = int(input("Digite a idade do nadador: "))

if idade2 >= 5 and idade2 <= 7:
    print("Infantil A")
elif idade2 >= 8 and idade2 <= 10:
    print("Infantil B")
elif idade2 >= 11 and idade2 <= 13:
    print("Juvenil A")
elif idade2 >= 14 and idade2 <= 17:
    print("Juvenil B")
else:
    print("Informe uma opçao que seja valida!")
