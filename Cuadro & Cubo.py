import math

class calculos:
    @staticmethod
    def calcular_cuadrado(numero):
        return math.pow(numero, 2)

    @staticmethod
    def calcucular_cubo(numero):
        return math.pow(numero, 3)

numero= int(input("Ingrese un número\n"))
cuadrado= calculos.calcular_cuadrado(numero)
cubo= calculos.calcucular_cubo(numero)

print(f"Cuadrado: {cuadrado}\n" + f"cubo: {cubo}\n")