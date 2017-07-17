string = raw_input("Enter string:")
count1=0
count2=0
for i in string:
    if(i.isdigit()):
            count1=count1+1
    elif(i.isalpha()):
            count2=count2+1 
print "DIGITS:",count1
print "LETTERS:",count2
