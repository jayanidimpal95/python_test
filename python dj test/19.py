class S:
    def __init__(self):
        self.n=''
    
    def accept(self):
        self.n = raw_input("Enter string:")
    def prints(self):
        print (self.n)
        
    
a=S()
a.accept()
a.prints()
