"""
Jokenpo V2
"""
from random import choice

player_vitorias = 0
ia_vitorias = 0
empate = 0

def opcao_player():
    while True:
        escolha = input("Escolha Pedra, Papel ou Tesoura: ").lower()
        if escolha in ["pedra", "papel", "tesoura"]:
            return escolha
        else:
            print("Digite uma escolha válida!")

def opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina

while True:
    print(70 * "_")
    esc_maquina = opcao_maquina()
    esc_jogador = opcao_player()
    print(70 * "_")

    if (esc_jogador == "pedra" and esc_maquina == "tesoura") \
        or (esc_jogador == "papel" and esc_maquina == "pedra") \
        or (esc_jogador == "tesoura" and esc_maquina == "papel"):
        # Jogador Ganha
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina} "
              f"Resultado: Você Ganhou!!!")
        player_vitorias += 1

    elif esc_jogador == esc_maquina:
        # Empate
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina} "
              f"Resultado: Empate!!!")
        empate += 1

    else:
        # Jogador perde
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina} "
              f"Resultado: Você Perdeu!!!")
        ia_vitorias += 1

    print(70 * "_")
    print(f"Vitórias do Jogador: {player_vitorias}")
    print(f"Vitórias do CPU: {ia_vitorias}")
    print(f"Empates: {empate}")
    print(70 * "_")

    esc_jogador = input("Você quer jogar novamente? (sim/não): ")
    if esc_jogador.lower() not in ["sim", "s"]:
        break

