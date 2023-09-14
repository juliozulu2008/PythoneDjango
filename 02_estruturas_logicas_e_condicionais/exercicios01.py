"""Execiçoe spara treinar"""

# Araea de um retangulo
print("Area de um Retangulo!")
altura = input("Qual é o valor da altura? ")
base = input("Qual é o valor da Base? ")
area = float(altura) * float(base)
print(area)
print("===========================================================")
#area de um quadrado
print("Area de um Quadrado!")
altura2 = input("Qual é o valor do altura? ")
base2 = input("Qual é o valor da base? ")
area = float(altura2) * float(base2)
print(area)
print("===========================================================")
# calculo de Porcentagem de desconto
print("Porcentagem de desconto")
valor_produto = input("Qual ao valor do Produto? ")
valor_desconto = input("Qual é a % de desconto?")
res = float(valor_produto) - float(valor_desconto)
print(res)
print("===========================================================")
print("Area de um Circulo!")
dia = input("Informe o diametro do circulo? ")
raio = input("Informe o raio do crirculo? ")
pi = 3.141592
res1 = float(pi)*float(raio)**2
print(res1)
print("===========================================================")
# converçao de reais em dolar
print("Conversao de reais em dolar!")
cotacao = input("Informe a Contação doi dola no dia de hoje? ")
valor = input("Informe o valor a ser convertido? ")
res2 = float(cotacao) * float(valor)
print(res2)
print("===========================================================")
# conversao de dolar para reais
print("Conversao de dolar para reais")
cota=input("Informe o valor da cotaçao do real hoje? ")
valor1= input("informw o valor a ser convertido? ")
res3 = float(cota)*float(valor1)
print(res3)
