class Rectangle:

    l = 0
    h = 0
    nom = ""

    def __init__(self, l=0, h=0, nom='rectangle'):
        self.l = l
        self.h = h
        self.nom = nom

    def display(self):
        print("(", self.nom, ": (", self.l, ", ", self.h, ")")

    def surface(self):
        return self.l*self.h


class Carre(Rectangle):

    def __init__(self, l=0, h=0, nom='Carre'):
        super().__init__(l, h)
        self.nom = nom


c = Carre(4, 4, 'carre 1')
r = Rectangle(5, 4, 'rectangle 1')