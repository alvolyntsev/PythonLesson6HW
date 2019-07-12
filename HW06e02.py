# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math
class Trapezium:
    def __init__(self, xA, yA, xB, yB, xC, yC, xD, yD):
        self.xA = xA
        self.yA = yA
        self.xB = xB
        self.yB = yB
        self.xC = xC
        self.yC = yC
        self.xD = xD
        self.yD = yD
    def ab(self):
         return abs(math.sqrt((self.xA - self.xB) ** 2 + (self.yB - self.yA) ** 2))
    def bc(self):
         return abs(math.sqrt((self.xC - self.xB) ** 2 + (self.yB - self.yC) ** 2))
    def cd(self):
         return abs(math.sqrt((self.xD - self.xC) ** 2 + (self.yC - self.yD) ** 2))
    def da(self):
         return abs(math.sqrt((self.xD - self.xA) ** 2 + (self.yA - self.yD) ** 2))
        #self.check_Trapez_ravn= (abs(math.sqrt((self.xA - self.xC) ** 2 + (self.yC - self.yA) ** 2))== abs(math.sqrt((self.xD-self.xB)**2+(self.yB-self.yD)**2)))
    def get_perim(self):
        return (abs(math.sqrt((self.xA-self.xB)**2+(self.yB-self.yA)**2))+abs(math.sqrt((self.xC-self.xB)**2+(self.yB-self.yC)**2))+abs(math.sqrt((self.xC-self.xD)**2+(self.yD-self.yC)**2))+abs(math.sqrt((self.xD-self.xA)**2+(self.yA-self.yD)**2)))
    def get_sides(self):
        return (Trapezium.ab(self),Trapezium.bc(self),Trapezium.cd(self),Trapezium.da(self))
    def get_high_ADC(self):
        aa2=abs((self.yD-self.yC)*self.xA+(self.xC-self.xD)*self.yA+(self.xD*self.yC-self.xC*self.yD))/(math.sqrt((self.yD-self.yC)**2+(self.xC-self.xD)**2))
        return (aa2)
    def get_high_ABC(self):
        aa2 = abs(
            (self.yB - self.yC) * self.xA + (self.xC - self.xB) * self.yA + (self.xB * self.yC - self.xC * self.yB)) / (
                  math.sqrt((self.yB - self.yC) ** 2 + (self.xC - self.xB) ** 2))
        return (aa2)
    def check_Trapez_ravn(self):
        return (abs(math.sqrt((self.xA - self.xC) ** 2 + (self.yC - self.yA) ** 2))== abs(math.sqrt((self.xD-self.xB)**2+(self.yB-self.yD)**2)))
    def get_sq(self):
        if Trapezium.check_Trapez_ravn(self)==True:
            if Trapezium.ab(self)== Trapezium.cd(self):
                return ((Trapezium.da(self)+Trapezium.bc(self))*Trapezium.get_high_ABC(self)/2)
            else:
                return ((Trapezium.ab(self)+Trapezium.cd(self))*Trapezium.get_high_ADC(self)/2)

        else: print('Трапеция не равнобочная')

trap = Trapezium(1,1,2,2,2,4,1,5)
print(trap.check_Trapez_ravn())
print(trap.get_sides())
print(trap.get_perim())
print(trap.get_sq())



