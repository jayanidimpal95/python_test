
class UserDefindEx(Exception):
    def __init__(self):
        print ("user-defined Exception")
 
try:
    raise UserDefindEx()
 
except UserDefindEx as e:
    print (e)
