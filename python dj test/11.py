list=[ 6, 6, 12, 19, 30]
print list
i=0
f=0
for i in range(len(list)-2):
    f=0
    c=list[i]+list[i+1]
    if(c!=list[i+2]):
        f=1
        break
if(f==0):
    print "yes additive sequence"
else:
    print "not additive sequence"
