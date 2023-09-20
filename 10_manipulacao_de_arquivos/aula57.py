"""
arqivos de texto simples escrita
"""

# Nome do arquivo onde você deseja escrever e ler o poema
nome_arquivo = "poema_de_amor.txt"

# Poema de amor com 10 linhas que rimam
poema = """
No teu olhar encontro o meu abrigo,
Em cada beijo, o mundo faz sentido.
Teu sorriso é a luz do meu destino,
No teu calor, sinto-me protegido.

Nosso amor é um sonho colorido,
Juntos, enfrentamos todo perigo.
Na dança do amor, estamos unidos,
Nossos corações batem no mesmo ritmo.
"""

# Abra o arquivo em modo de escrita ('w')
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(poema)

print(f"O poema de amor foi escrito com sucesso no arquivo '{nome_arquivo}'.")

# Reabra o arquivo em modo de leitura ('r')
with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(f"Conteúdo do arquivo '{nome_arquivo}':")
    print(conteudo)

