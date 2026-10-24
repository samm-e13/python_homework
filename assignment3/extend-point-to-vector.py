class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equality(self1, self2):
        if (self1.x == self2.x and self1.y == self2.y):
            return True
        else:
            return False

    def __str__(self):
        return f"({self.x}, {self.y})"

    def dist(self1, self2):
        return ((self1.x - self2.x)**2 + (self1.y-self2.y)**2) **.5

class vector(point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"vec: ({self.x}, {self.y})"

    def __add__(self1, self2):
        x = self1.x + self2.x 
        y = self1.y + self2.y
        return vector(x, y)

a = point(3, 5)
b = point(2, 4)
print(a)
print(b)
print(a.equality(b))
print(a.dist(b))

x = vector(1,5)
y = vector(5,6)
print(x)
print(y)
print(x+y)