#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_1
# 204111 Sec 002

def eratosthenes(n:int,show_step:bool=False) -> list[int]:
    prime_list = []

    if n < 2:
        return []

    list_ = list(range(2,n+1))
    #list_ = list(filter(lambda x: x%list_[0] != 0,list_))
    
    #while list_ != []:
    while list_[0]**2 <= n: # when x can't divied others mean number is less than sqrt(x) mean x is prime
        #print(prime_list)
        if show_step: print(f"{list_[0]}: {prime_list+list_}")
        prime_list.append(list_[0])
        prime = list_[0]
        list_ = list(filter(lambda x: x%list_[0] != 0,list_))

    ans = prime_list+list_
    return ans

def eratosthenes2(n:int,show_step:bool=False) -> list[int]:
    prime = 2
    prime_list = [2]

    list_ = list(filter(lambda x: x%prime != 0,range(2,n+1)))
    
    #while list_ != []:
    while prime**2 <= n: # when x can't divied others mean number is less than sqrt(x) mean x is prime
        #print(prime_list)
        if show_step:
            print(f"{prime}: {prime_list+list_}")
        prime_list.append(list_[0])
        prime = list_[0]
        list_ = list(filter(lambda x: x%prime != 0,list_))

    ans = prime_list+list_
    return ans
from random import randint
def test():
    for i in range(100000):
        n = randint(0,100000)
        try:
            assert eratosthenes(randint(n)) == eratosthenes2(n)
        except:
            print(n)
            print(eratosthenes(n))
            print(eratosthenes2(n))
            return 0
    print("hi")


if __name__ == "__main__":
    test()
    #n = 100
    #print(eratosthenes(n,True))
    #print(eratosthenes(int(input())))
