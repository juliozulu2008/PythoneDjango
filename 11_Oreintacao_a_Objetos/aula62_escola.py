class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__area = lado * lado

    def reortona_area(self): # Nesse caso o acesso esta sendo feito dentrp de um metodo
        print(self.__area)



quad = Quadrado(2) # O metodo esta sendo chamado
quad.reortona_area() # O metodo pertençe a classe quadrado
quad.area = 7
quad.reortona_area()
print(quad.__dict__)
# NAME MANGLING = _CLASSE__ATRIBUTO
quad._Quadrado__area = 27
quad.reortona_area()
print(quad.__dict__)
