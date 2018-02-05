"""
Los operadores booleanos.
Hay un orden de operaciones para operadores booleanos:
not se evalúa primero
and se evalúa a continuación
or es evaluado por último.
https://docs.python.org/3/reference/expressions.html#operator-precedence
"""
name = "John"
age = 17

print(name == "John" or not age > 17)

print(name is "Ellis" or not (name is "John" and age == 17))

x = 1 + 2 ** 3 / 4 * 5
print(x)
