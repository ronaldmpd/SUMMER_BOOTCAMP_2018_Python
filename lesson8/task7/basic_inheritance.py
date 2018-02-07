
class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def getName(self):
        return self.firstname + " " + self.lastname


class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first,last)
        self.staffnum = staffnum

    def getInfo(self):
        res = Person.getName(self)
        res += " " + str(self.staffnum)
        return res

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.getName())
print(y.getInfo())