class Circle:
    def __init__(self,r):
        self.r=r

    def area(self):
        print "Area:",self.r*self.r*(22.0/7)
r=input("Enter radius:")
c=Circle(r)
c.area()
