"""
Exemplo de modulo
"""

#import (modulo) -> Importa todas as funçoes
#from (modulo) importe (funçao) -> impota funçoes especificas
#import (modulo) as (apelido do modulo) exemplo import random as rd


import aula50
from random import (random, choice)

print(aula50.primo(1))


print(random())

l1 = ["Pedra", "Papel", "Tesoura"]
print(choice(l1))
