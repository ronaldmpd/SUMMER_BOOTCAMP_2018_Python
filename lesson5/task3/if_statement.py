"""
La palabra reservada if se usa para formar una instrucción condicional
que ejecuta algún código
especificado después de verificar si su expresión es True.
Python usa indentación para definir bloques de código.
"""
name = "John"
age = 17

if name == "John" or age == 17:
    print("name is John")
    print("John is 17 years old")

tasks = ['task1', 'task2']

if len(tasks) == 0:
    print("empty")
