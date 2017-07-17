class Point:
    def __init__(self, x = 0):
        self.x = x
    
    def __str__(self):
        return str(self.x)
    
    def __add__(self,other):
        x = self.x + other.x
        return Point(x)

p1 = Point(2)
p2 = Point(8)
print(p1+p2)
