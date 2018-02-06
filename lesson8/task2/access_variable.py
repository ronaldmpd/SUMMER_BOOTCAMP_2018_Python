
class MyClass:
    variable1 = 45
    variable2 = 180

    def foo(self):
        print("Hello from function foo")

my_object = MyClass()
my_object1 = MyClass()

my_object.variable2 = 3

print(my_object.variable2)
print(my_object1.variable2)

my_object.foo()

print(my_object.variable1)

