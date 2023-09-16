"""
Mudando Items
"""
l1, l2, l3 = [1,2,2], [2,"julio", True], ["oie", "eu ", "Sou Dev"]
print(l1)
print(100*"#")
print(l2)
print(100*"#")
print(l3)
print(100*"#")
print("Modificando itens da lista: ")
l1[1] = 0
print(l1)
print(100*"#")
print("Modificando mais de um item na lista")
l1[::] = 1,2,3
print(l1)
print(100*"#")
print("modificando itens especificos da lista")
l1[1:3] = 0,0,0
print(l1)
print("Tomar cuidado com o uso da lista pois podemos alterar o tamnaho da lista")
