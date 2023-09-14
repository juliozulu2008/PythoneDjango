"""
ESTRUTURAS DE REPETIÇÃO

while
for
do while * nao tem mais tem como fazer kkkkk

"""

#while

a = 0
while a <= 10:
    print(a)
    a += 1
    if a == 9:
        break

print(f"=====================================")


#FOR
b = 0
for b in range(10):
    print(b)
    b += 1

#mais sobre For
c = "Paraná"

for x in c:
    print(x)

for d in range(10,33): # exemplo de uso de range ...
    print(d)

for e in range(0, 10, 2): # primeiro parametro é onde começa, segundo onde termina e terciro como que vai chegar la
    print(e)

for f in range(6):
    print(f)
else:
    print("Fim do Looping!")
