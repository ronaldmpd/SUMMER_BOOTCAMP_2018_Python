class Square:

    def __init__(self):
        self.sides = 4

square = Square()
print(square.sides)

class Car:
    def __init__(self, color,maximum_Speed):
        self.color = color
        self.maximum_Speed = maximum_Speed

car = Car("blue", 250)
print(car.color)

car2 = Car(maximum_Speed=250, color="magenta")
print(car2.color)


#Sobrecarga de operadores
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x+otro.x, self.y+otro.y)

    def __str__(self):
        return "Punto(%d,%d)" % (self.x, self.y)
    """
    Si el operando a la izquierda de * es un Punto
    """
    def __mul__(self, otro):
        return self.x*otro.x + self.y*otro.y

    """
    Si el operando a la izquierda de * es un tipo primitivo
    y el operando de la derecha es un Punto
    """
    def __rmul__(self, otro):
        return Punto(otro * self.x, otro * self.y)

puntoA = Punto(3,4)
puntoB = Punto(5,7)
res = puntoA + puntoB
print(res)




#Polimorfismo
print("Polimorfismo")
def multisuma (x, y, z):
    return x * y + z

print(multisuma(3, 2, 1))
print(multisuma(2, puntoA, puntoB))


