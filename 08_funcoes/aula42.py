"""
JoKenPo
"""
import random

def jogar_jokenpo():
    opcoes = ["Pedra", "Papel", "Tesoura"]

    jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
    computador = random.choice(opcoes)

    print(f"Você escolheu {jogador}.")
    print(f"O computador escolheu {computador}.")

    if jogador in opcoes:
        if jogador == computador:
            print("Empate!")
        elif (jogador == "Pedra" and computador == "Tesoura") or \
             (jogador == "Papel" and computador == "Pedra") or \
             (jogador == "Tesoura" and computador == "Papel"):
            print("Você ganhou!")
        else:
            print("O computador ganhou!")
    else:
        print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")

if __name__ == "__main__":
    jogar_jokenpo()
