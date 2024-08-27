import random
import string

def same_letters(str1: str, str2: str) -> bool:
    str1 = list(filter(lambda x: x.isalpha(), str1.lower()))
    str2 = list(filter(lambda x: x.isalpha(), str2.lower()))

    def check(list_a,list_b):
        if list_a == []:return True
        #print(list_a[0])
        if list_a[0] in list_b:
            return check(list_a[1:],list_b)
        else: return False
    return check(str1,str2) and check(str2,str2)

def same_letters2(str1: str, str2: str) -> bool:
    str1,str2 = str1.lower(),str2.lower()
    str1 = list(filter(lambda x: x.isalpha(), str1))
    str2 = list(filter(lambda x: x.isalpha(), str2))
    
    #max_,min_ = str2,str1
    #if len(str1) >= len(str2): max_,min_ = str1,str2
    
    ans = list(map(lambda x: x in str1,str2))
    ans2 = list(map(lambda x: x in str2,str1))
    if False in ans or False in ans2:return False
    return True

def test():
    for i in range(20000):
        t1,t2 = '',''
        for i in range(random.randint(1,100)):
            #t1 += random.choice(string.printable)
            #t2 += random.choice(string.printable)
            t1 += random.choice(string.ascii_letters)
            t2 += random.choice(string.ascii_letters)
        try:
            assert same_letters(t1,t2) == same_letters2(t1,t2)
        except:
            print('t1 :',t1)
            print('t2 :',t2)
            print(f'excpect {same_letters2(t1,t2)} got {same_letters(t1,t2)}')
            return 0

if __name__ == "__main__":
    test()
