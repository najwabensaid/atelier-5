class Vecteur2D:

    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print("(", self.x, ", ", self.y, ")")

    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        v = Vecteur2D(a, b)
        return v


vec = Vecteur2D()
vec2 = Vecteur2D(1, 1)
vec.x = 10
vec.y = 20
vec.display()
vec2.display()
vec3 = vec + vec2
vec3.display()