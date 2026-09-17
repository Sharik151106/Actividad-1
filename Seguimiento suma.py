import math

class Segumiento_Suma:

    @staticmethod
    def calcular_x(x,y):
        return x + math.pow(y,2)

suma=0
x=20
y=40

suma= suma + x
x = Segumiento_Suma.calcular_x(x,y)

suma= suma + (x/y)

print(f"X vale: {x}\n"+ f"Y vale: {y}\n" + f"El valor de la suma es: {suma}")