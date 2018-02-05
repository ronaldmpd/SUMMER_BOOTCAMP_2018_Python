"""
Un diccionario es similar a una lista, excepto que
tiene acceso a sus valores buscando una clave en lugar de un índice
"""

phone_book = {"John": 123, "Jane": 234, "Jerard": 345}
print(phone_book)


phone_book["Jill"] = 345
print(phone_book)

#borrar un elemento
phone_book.pop("John")

print(phone_book["Jane"])
