#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_1
# 204111 Sec 002
# not finished
def eratosthenes(n:int,show_step:bool=False) -> list[int]:

    if n < 2: return []
    prime_list = []

    list_ = list(range(2,n+1))
    list_ = list(filter(lambda x: x%list_[0] != 0,list_))
    prime = list_[0]
    
    #while list_ != []:
    while prime**2 <= n: # when x can't divied others mean number is less than sqrt(x) mean x is prime
        #print(prime_list)
        if show_step: print(f"{prime}: {prime_list+list_}")
        prime_list.append(prime)
        prime = list_[0]
        list_ = list(filter(lambda x: x%prime != 0,list_))

    ans = prime_list+list_
    return ans
if __name__ == "__main__":
    n = 20
    print(eratosthenes(n,True))
