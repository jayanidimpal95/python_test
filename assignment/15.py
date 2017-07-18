n = input("Enter no. of head:")
l = input("Enter no. of leg:")

for chickens in range(n+1):
    rabbits = n-chickens
    if(chickens*2+rabbits*4==l):
        print(chickens,rabbits)
