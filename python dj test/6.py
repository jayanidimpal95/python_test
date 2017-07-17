try:
    s=raw_input("Enter email id:")

    index=s.index('@')
    user=s[0:index]
    dot=s.index('.')
    company=s[index+1:dot]
    if(user.isalnum() or company.isalnum()):
        print("please enter only character in username and company name")
    else:
        print(user)
except:
    print("Invalid")
