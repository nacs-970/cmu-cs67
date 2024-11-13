#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec 002

#def count_4n59(n):
#    count_ = 0
#    if n <= 54:count_ += (n//45) + (n//54)
#    if n > 54 and n < 450: return ((n//100)*2)+2
#    if n >= 450:return ((n//100)*2)+2+8
#    return count_

#def count_4n54(n):
#    #print(n)
#    if n == 1: return 0
#    if '45' in str(n) or '54' in str(n):
#        return 1 + count_4n5(n-1)
#    return count_4n5(n-1)

#def count_4n53(n):
#    def count_(list_):
#        if len(list_) == 0:return 0
#        if '45' in str(list_[0]) or '54' in str(list_[0]):
#            return 1 + count_(list_[1:])
#        return 0 + count_(list_[1:])

#    range_ = list(range(1,n+1))
#    ans = count_(range_)
#    return ans

def count_4n5(n):
    range_ = list(filter(lambda x: '4' in str(x) and '5' in str(x),range(1,n+1)))
    #print(range_)
    return len(range_)

#import random
    
if __name__ == '__main__':
    assert count_4n5(45) == 1
    assert count_4n5(99) == 2 # 45,54
    #print(count_4n5(500))
    #print(count_4n5(200))
    #print(count_4n5(300))
    #print(count_4n5(600))
    #assert count_4n5(9999) == 558 # 45,54
    #n = random.randint(1,9999)
    #count_4n53(9999)
    #print(count_4n52(9999)) # 558
    #try:
    #    assert count_4n53(n) == count_4n52(n)
    #except AssertionError:
    #    print(n,count_4n5(n),count_4n52(n))
    #print("All OK!")
