"""
adicionando items
"""
s1 = {1,2,3,4,5}
print(s1)
print(100*"#")
s1.add("99")
print(s1)
# Update
s2 = {99,98,97}
s3 = {"a", "b", "c"}
s2.update(s3)
print(s2)
# valores duplicadaso serao tratados como unicos
print(100*"#")
# removendo elementos
s2.pop() # nesse caso vai remover itens aleatorios
print(s2)
print(100*"#")
s2.remove(99) # se tentar remover um item que ano existe da erro
print(s2)
print(100*"#")
s2.discard(98) # nao da erro se nmao tiver
print(s2)
# del deleta o set e clear deixa o set vazio
