num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = int(input("Digite o 3 numero: "))
num4 = int(input("Digite o 4 numero: "))
num5 = int(input("Digite o 5 numero: "))

resultado = [num1, num2, num3, num4, num5]

resultado.sort()
print(f"O menor numero informado é o {resultado[0]}")
print(50*"_")
print(f"O maior numeor informado é o {resultado[4]}")

print(100* "====================")
# Inicializa a variável para armazenar a soma
S = 0

# Numerador inicial
numerador = 3

# Denominador inicial
denominador = 40

# Loop para calcular a soma dos termos
while denominador >= 1:
    termo = numerador / denominador
    S += termo
    numerador += 1
    denominador -= 1

print("Série 1:", S)

print(100* "====================")

# Inicializa a variável para armazenar a soma
S = 0

# Numerador inicial
numerador = 480

# Denominador inicial
denominador = 2

# Loop para calcular a soma dos 20 primeiros termos
for _ in range(20):
    termo = numerador / denominador
    S += termo
    numerador -= 5
    denominador += 20

print("Série 2:", S)

print(100* "====================")

# Inicializa a variável para armazenar a soma
S = 0

# Numerador inicial
numerador = 1

# Denominador inicial
denominador = 2

# Loop para calcular a soma dos 15 primeiros termos
for _ in range(15):
    termo = numerador / denominador
    S += termo
    numerador = numerador * 2 + 1
    denominador += 2

print("Série 3:", S)
