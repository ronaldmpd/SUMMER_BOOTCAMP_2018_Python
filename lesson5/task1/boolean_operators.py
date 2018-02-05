"""
Los operadores booleanos comparan declaraciones y devuelven resultados
en valores booleanos.
El operador booleano "and".
El operador booleano "or".
El operador booleano not invierte la expresión booleana.
"""
name = "John"
age = 17

print(name == "John" or age == 17)

# Si el nombre es igual a "John" y no tiene 23 años.
print(name == "John" and not (age==23))
