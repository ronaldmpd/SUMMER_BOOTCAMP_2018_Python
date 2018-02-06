
class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current


# Para Complex cree el objeto y realize una llamada al metodo
complex = Complex()
complex.create(2,3)
print("real"  + str( complex.r))
print("imag"  + str ( complex.r))

# Para Calculator cree el objeto y realize llamadas a los metodos
# identifique y resuelva el problema
calculator = Calculator()
calculator.add(5)
print(calculator.get_current())
calculator.add(10)
print(calculator.get_current())