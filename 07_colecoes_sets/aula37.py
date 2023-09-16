"""
Sets sao: Coleçao nao ordenada, imutavel e que nao permite valores duplicados
"""
# sao conhecidos como cinjuntos

s1 = {"1", "2", "3"}
print(type(s1))
print(s1)
print(100*"#")
t1 = (2, 6, 7, 99, 112)
s2 = set(t1)
print(type(s2))
print(s2)
print(100*"#")
print("para acessar os valores tem que usar loop")
for x in s2:
    print(x)
