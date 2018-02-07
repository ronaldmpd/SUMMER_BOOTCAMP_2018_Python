#python -B import.py   #no genera _pycache_ .pyc

import calculator

calc = calculator.Calculator()
calc.add(2)
print(calc.get_current())

import my_module

my_module.hello_world("Tom")
