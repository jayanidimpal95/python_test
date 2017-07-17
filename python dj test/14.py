n=input("Enter no.:")
f=0
if(n>0):
    while(n!=1):
        if (n%2 != 0):
          f=1
          break
        n = n/2;
    if(f==0):
        print("yes power of two")
    else:
        print("not a power of two")
else:
    print("Enter positive number")
