"""
Fromkeys faz as listas e dicionario retornarem como dicionarios
"""
tupla = ("Item", "Item 2", "Item 3")
t1 = (1, 3, 4,)
dicio = dict.fromkeys(tupla, t1) # se passar apenas 1 argumento o valor vai ficar NONE
print(dicio)
# nesse caso ira retornar NONE que é o null do Python

d1 = {
    "d2": {
        "Nome": "JULIO",
        "Idade": 27
    },
    "d3": {
        "Nome": "Kelly",
        "idade": 26
    }
}
print(d1)
