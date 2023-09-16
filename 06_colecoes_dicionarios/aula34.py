"""
Dacionarios: Coleçao nao ordenada, mutavel e que ano permite valores Duplicados
"""
d1 = {"chave":"valor",
      "nome": "julio",
      "idade": 27,
      "Peso": 118.5,
      "casado": True}
print(d1)
print(type(d1))
print(100*"#")
print(d1["chave"])
print(d1["nome"])
print(d1.get("idade"))
# exinir chaves
print(d1.keys())
print(100*"#")
print(d1.values())
print(100*"#")
print(len(d1))
print(100*"#")
if "idade" in d1:
    print(" A Chave idade exsite")
else:
    print("Error!")
print(100*"#")

print(d1.items()) # lista todos as chaves e valores do dicionario
