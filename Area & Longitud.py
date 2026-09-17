import math

class area_longitud:
    @staticmethod
    def calcular_area_circulo(radio):
        return math.pow(radio,2) * math.pi
    
    @staticmethod
    def calcular_la_longitud(radio):
        return 2* math.pi * radio

radio= float(input("Ingrese el radio del circulo\n"))
area = area_longitud.calcular_area_circulo(radio)
longitud = area_longitud.calcular_la_longitud(radio)

print(f"area del circulo:{area}\n"+ f"longitud de la circunferecia:{longitud} ")