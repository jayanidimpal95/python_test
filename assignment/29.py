t=1
b=0
while(t!=0):
    n = raw_input("Enter:")
    li=n.split(" ")
    if(li[0]=='D'):
        b+=int(li[1])
    elif(li[0]=='W'):
        b=b-int(li[1])
    print "final balance:",b
    n=int(raw_input("Enter 1 for exit ELSE 2: "))
    if(n==1):   # exit condition if user enter 1
        t=0
print "final balance:",b
