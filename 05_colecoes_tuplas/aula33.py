"""
Mais sobre tuplas
"""
t1, t2 = ("julio","Ravi"), ("Kelly", "Laura")
t3 = t1 + t2
print(t3)

for x in t3:
    print(x)

for x in range(len(t3)):
    print(x, t3[x])

# desenpacotar itens das listas e tuplas

a, b, c, d = t3
print(a)
print(100*"#")
print(b)
print(100*"#")
print(c)
print(100*"#")
print(d)
print(100*"#")
print(100*"#")
# se eu quiser passar 3 item para apenas duas variaveis eu utilizo o *
t4 = (1,2,3,4)
a1, b2, *c3 = t4
print(a1)
print(100*"#")
print(b2)
print(100*"#")
print(c3)
print(100*"#")
print(t4)
