"""
Remover elementos
"""

l1 = ["Julio", 27, "Kelly", 26, "Laura", 5, "Ravi", 1, 0, "Maoie"]
print(l1)
print(100*"#")
l1.pop(8)
print(l1)
print(100*"#")
for x in range(len(l1)):
    print(x, l1[x])

print(100*"#")
l1.remove("Maoie") # remove especifico "nome"
print(l1)
print(100*"#")
#apagar tudo com o del
del l1[0] # tambem da para apagar especifico
print(l1)
print(100*"#")
print("Funçao clear apara tudo dentro da lista mais nao apaga a lista")
l1.clear()
print(l1)
print(100*"#")
l1.extend(["julio","Kelly", "laura", "Ravi"])
print(l1)
print(100*"#")
print("Agora a funçao para ordenar a lista")
l1.sort() # reverse = True para lista reversa
print(l1)
l1.sort(key= str.lower()) # ordena tudo em letra minuiscula
print(l1)
l1.sort(key=str.upper()) # ordenta tudo em letra maiuscula
print(l1)
print(100*"#")
