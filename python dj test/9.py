import sys
class Ps:
    def validate(self,n):
        l=len(n)
        l1=list(n)
        f=0
        b=0
        s=0
        sp=0
        d=0
        if(l>=6 and l<=12):
            f=1
        else:
            f=0

        for x in  l1:
            if(x>='A' and x<='Z'):
                b=b+1
            if(x>='a' and x<='z'):
                s=s+1
            if(x=='$' or x=='#' or x=='@'):
                sp=sp+1
            if(x>='0' and x<='9'):
                d=d+1
        if(f and b and s and sp and d):
            print "valid"
        else:
            print "not valid"


def main():
    p=Ps()
    p.validate(raw_input("Enter password:"))

if __name__ == "__main__": main()
        
