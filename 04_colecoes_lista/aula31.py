"""
Copiando lista
"""
l1, l2 = ["a","b","c"],[1,2,3]
print("Da pra usar + ou o exntend")
l3 = l1+l2
print(l3)
print("exemplo usando o extente")
l4 = [99,98,00]
l3.extend(l4)
print(l3)
l5 = [1,2,333]
print(100*"#")
print(l1)
print(100*"#")
l1 = l5.copy()
print(100*"#")
print(l1)
print(100*"#")
