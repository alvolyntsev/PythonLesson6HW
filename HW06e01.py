# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Triangle:
    def __init__(self, xA, yA, xB, yB, xC, yC):
        self.xA = xA
        self.yA = yA
        self.xB = xB
        self.yB = yB
        self.xC = xC
        self.yC = yC
    def get_sq(self):
        return (0.5*abs((self.xB-self.xA)*(self.yC-self.yA)-(self.xC-self.xA)*(self.yB-self.yA)))
    def get_high_A(self):
        aa2=abs((self.yB-self.yC)*self.xA+(self.xC-self.xB)*self.yA+(self.xB*self.yC-self.xC*self.yB))/(math.sqrt((self.yB-self.yC)**2+(self.xC-self.xB)**2))
        return (aa2)
    def get_perim(self):
        return (abs(math.sqrt((self.xA-self.xB)**2+(self.yB-self.yA)**2))+abs(math.sqrt((self.xC-self.xB)**2+(self.yB-self.yC)**2))+abs(math.sqrt((self.xC-self.xA)**2+(self.yA-self.yC)**2)))


triangle1=Triangle(-1,-1,2,7,5,8)
print(triangle1.get_sq(), triangle1.get_high_A(), triangle1.get_perim())