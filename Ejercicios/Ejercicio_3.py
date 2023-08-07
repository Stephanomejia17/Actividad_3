from math import sqrt
class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def imprimir(self):
        print("(", self.x, ",", self.y, ")")
    def mover(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y
    def calcular_distancia(self, punto: 'Point') -> float:
        return sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)


if __name__ == "__main__":
    Mipunto = Point(1,2)
    Mipunto2 = Point(4, 20)

    Mipunto.imprimir()
    Mipunto2.imprimir()

    Mipunto.mover(5,1)
    Mipunto.imprimir()

    print(Mipunto.calcular_distancia(Mipunto2))