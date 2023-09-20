import os
import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    nascimento = datetime.datetime.strptime(data_nascimento, '%Y-%m-%d').date()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

def registrar_paciente():
    nome = input("Nome completo: ")
    email = input("E-mail: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    telefone = input("Telefone: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")

    idade = calcular_idade(data_nascimento)

    if idade >= 65:
        grupo_de_risco = "Sim (65+)"
    else:
        grupo_de_risco = "Não"

    with open("pacientes.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"E-mail: {email}\n")
        arquivo.write(f"CPF: {cpf}\n")
        arquivo.write(f"RG: {rg}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write(f"Data de Nascimento: {data_nascimento}\n")
        arquivo.write(f"Grupo de Risco: {grupo_de_risco}\n")
        arquivo.write("\n")

def listar_pacientes():
    with open("pacientes.txt", "r") as arquivo:
        pacientes = arquivo.read()
        print(pacientes)

if __name__ == '__main__':
    while True:
        print("Registro de Pacientes")
        print("1. Registrar paciente")
        print("2. Listar pacientes")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_paciente()
        elif opcao == '2':
            listar_pacientes()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Encerrando o programa.")
