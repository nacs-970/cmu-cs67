import random
import string

def triangle(n:int) -> str:
    num = list(range(1,n-1))
    body = list(map(lambda x: ((("*")+("."*(x+(x-1)))+("*"))),num)) # map use with array
    end_ = [(n-1)*("* ")+("*")] # "(*\ *\ *\ )*"
    struct =  list("*")+body+end_ # add head, body and end_
    struct = '\n'.join(struct) + "\n" # replace ,
    return struct

def check():
    letter = string.printable
    for i in range(10000):
        n = ""
        for i in range(random.randint(1,100)): n+= random.choice(letter)
        try:
            assert test() == right()
        except:
            print("Expect : ", right(), "Got : ", test())
            return 0
        
if __name__ =="__main__":
    check()