"""
modioficando valores do dicionario
"""

d1 = {"chave":"valor",
      "nome": "julio",
      "idade": 27,
      "Peso": 118.5,
      "casado": True}

d1["chave"] = "acesso"
print(d1)
print(100*"#")
d1.update({"nome":"JULIO"})
print(d1)
print(100*"#")
print("Para remover basta usar a funçao POP")
d1.popitem() # remove o ultimo,Obs Abaixo da versao 3.7 elimina um item aleatorio
print(d1)
print(100*"#")
d1.pop("Peso") # elimina uma chave especifica
print(d1)
print(100*"#")
del d1["chave"]
print(f"d1: {d1}")
# LOOP
for x in d1:
      print(x, d1[x])

print(100*"#")

d2 = d1.copy()
print(f"d2: {d2}")
print(100*"#")
#outra maneira de Copiar
d3 = dict(d1)
print(f"d3: {d3}")
print(100*"#")
