n = raw_input("Enter password:")
l1=n.split(",")


for i in range(len(l1)):
    l=len(l1[i])
    f=0
    b=0
    s=0
    sp=0
    d=0
    if(l>=6 and l<=16):
        f=1
    else:
        f=0
    list2=l1[i]
    
    for x in  list2:
        if(x>='A' and x<='Z'):
            b=b+1
        if(x>='a' and x<='z'):
            s=s+1
        if(x=='$' or x=='#' or x=='@'):
            sp=sp+1
        if(x>='0' and x<='9'):
            d=d+1
    if(f and b and s and sp and d):
        print "valid password: ",list2
   
