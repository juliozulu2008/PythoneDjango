"""
Adicionar elementos a lista
"""
l1 = ["Julio", "Kelly", "Laura", "Ravi"]
print(l1)

for x in l1:
    print(x)

print(100*"#")

print(len(l1))

print(100*"#")

for x in range(4):
    print(x)

print(100*"#")

for x in range(len(l1)):
    print(x, l1[x])

n1 = "Julio Cesar Dias"
l2 = list(n1)
print(l2)
print(100*"#")
l3 = l2.split(",")

print(l2)

#adicionar elementos
print(100*"#")
l1.append(1)
print(l1)
