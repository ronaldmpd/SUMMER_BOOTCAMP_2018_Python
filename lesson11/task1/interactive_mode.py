import sys

class Employe:

    def __init__(self, nombcomp):
        first,last = nombcomp.lower().split(' ')
        self.__first, self._last = first,last
        self.email = first + "." + last + "@email.com"

    def getEmail(self):
        return self.email


author = "FAL"
# python lesson11/interactive_mode.py "franz lopez"
# from lesson11.task1.interactive_mode import Employe
# from lesson11.task1 import interactive_mode
# interactive_mode.sys.path

if __name__ == "__main__":
    nomc = sys.argv[1]
    emp = Employe(nomc)
    print(emp.getEmail())