"""
Tupla é uma variavel que pode carregar varios tipos de dados ao mesmo tempo igual a lista
oq ue muda é que a lista pode mudar e a tupla nao, quase igual um array em C que tem que expecificar
o tamanho
"""
t1 = ("item", "item 2", "item3")
print(t1)
print(t1[2])

print("è possivel tranformar uma tupla em lista e um,a lista em tupla caso seja nessesarioa a alteraçao")
l1 = list(t1)
print(l1)
print(type(l1))
l1.append("item4")
print(100*"#")
t1 = tuple(l1)
print(t1)
print(type(t1))
print(100*"#")
