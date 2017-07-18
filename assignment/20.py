class Person:
    def getGender(self):
        print "gender"

class Female(Person):
    def getGender(self):
        print "Female"

class Male(Person):
    def getGender(self):
        print "Male"

f = Female()
m = Male()
f.getGender()
m.getGender()
