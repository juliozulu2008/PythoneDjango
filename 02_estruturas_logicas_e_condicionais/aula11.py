"""Estrutura logica if e Else e elif"""
nome = input("Digite seu nome: ")
idade = input("digite sia idade: ")

if nome != "":
    print(f"Bem Vindo! {nome}")
else:
    print("Preencha o campo (nome) Corretamente!")

if nome != "" and idade != "":
    print(f"Ola {nome}, seja bem vindo! vi aqui que tem {idade} anos! ")
elif idade < "18":
    print(f"{nome}, voçe pode entrar no estabelcimento")
else:
    print("Algum dos campos ano foram preenchidos corretamente, por favor verifique")



