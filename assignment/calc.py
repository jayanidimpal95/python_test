import logging
logging.basicConfig(filename='calc_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Started')

class Add:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):      #Function for addition
        print str(self.x)+"+"+str(self.y)+"= "+str(self.x+self.y)

class Sub:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sub(self):      #Function for subtraction
        print str(self.x)+"-"+str(self.y)+"= "+str(self.x-self.y)

class Mul:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def multi(self):        #Function for multiplication
        print str(self.x)+"*"+str(self.y)+"= "+str(self.x*self.y)

class Div:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def div(self):      #Function for division
        try:
            d=self.x/self.y
            print str(self.x)+"/"+str(self.y)+"= "+str(d)
        except ZeroDivisionError as e:
            logging.error('user enter y as %d '%y)
            print('Divide by 0 is not possible')

class Power:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def pow(self):      #Function for power
        print str(self.x)+"**"+str(self.y)+"= "+str(self.x**self.y)

t=1
x=0
y=0
while(t!=0):
    try:
        x = float(input("Enter 1st no.:"))
        y = float(input("Enter 2nd no.:"))  
    except Exception as e:
        print "please enter no. "
        logging.error('x is not a no.')
        logging.error('y is not a no.')
        continue

    op = raw_input("Enter operator(+,-,*,/,**):")

    if(op=="+"):
        a=Add(x,y)   
        a.add()     #calling to addition function
        logging.info('addition done')
    elif(op=="-"):
        a=Sub(x,y)
        a.sub()     #calling to subtraction function
        logging.info('sub done')
    elif(op=="*"):
        a=Mul(x,y)
        a.multi()   #calling to multiplication function
        logging.info('multiplication done')
    elif(op=="/"):
        a=Div(x,y)
        a.div()
        logging.info('division done')
    elif(op=="**"):     #calling to power function
        a=Power(x,y)
        a.pow()
        logging.info('power done')
    else:
        logging.error('user enter Not a valid operator %s'%op)
        print("Not a valid operator")
        continue
    try:
        n=int(raw_input("Enter 1 for exit ELSE any key: "))
        if(n==1):   # exit condition if user enter 1
            t=0
    except:
        print("continue..")
    logging.info('next iteration')
logging.info('Finished')
