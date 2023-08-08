from math import pi
from math import sqrt
class Circulo:
    def __init__(self, centro: float, radio: int):
        self.x1: int = int((centro * 10) // 10)
        self.y1: int = int((centro * 10) % 10)
        self.radio: int = radio

    def area(self) -> float:
        return pi * (self.radio)**2
    def perimetro(self) -> float:
        return 2 * pi * self.radio
    def pertenece_al_ciculo(self, punto: float) -> bool:
        self.x2: int = int((punto * 10) // 10)
        self.y2: int = int((punto * 10) % 10)
        if((sqrt(self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) <= self.radio):
            return True
        else:
            return False



MiCirculo = Circulo(1.2, 3)
print(MiCirculo.area())
print(MiCirculo.perimetro())
print(MiCirculo.pertenece_al_ciculo(4.3))