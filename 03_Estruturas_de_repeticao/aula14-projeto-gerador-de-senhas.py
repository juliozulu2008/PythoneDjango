print("Olá Este é o gerador de senhas!!")
chave = input("Digite a base de sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "4"
    elif letra in "Ee": senha = senha + "5"
    elif letra in "Ii": senha = senha + "1"
    elif letra in "Oo": senha = senha + "0"
    elif letra in "Uu": senha = senha + "11"
    elif letra in "Ss": senha = senha + "$"
    elif letra in "1" : senha = senha + "I"
    elif letra in "0" : senha = senha + "O"
    elif letra in " " : senha = senha + "#"
    else: senha = senha + letra

print(senha)

