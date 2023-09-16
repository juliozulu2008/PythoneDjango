"""
adicionar items
"""

l1 = []
print(l1)
l1.append(1)
print(l1)
l1.append("Julio")
print(l1)

print(100*"#")

for x in range(len(l1)):
    print(x, l1[x])
# adiccionar uma lita dentrod e uma lista

l1.append([1,2,3])
print(l1)

print(100*"#")

for x in range(len(l1)):
    print(x, l1[x])

print(100*"#")

print("Metodo Insert")
# esse adiciona um ele mento no local desejado e empurra os outros para ferente
print(l1)
print(100*"#")
l1.insert(2, 999)
print(l1)
print(100*"#")
for x in range(len(l1)):
    print(x, l1[x])

print(100*"#")
print("Metodo Extend")
# o mesmo que apend porem esse aceita mais de um argumento
l1.extend(["Kelly", 27, "Laura", 5, "Ravi"])
print(l1)
print(100*"#")
for x in range(len(l1)):
    print(x, l1[x])

print(100*"#")
