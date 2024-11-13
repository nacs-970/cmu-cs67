#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec 002
def reverse_cap(list_a):
    list_a = list(map(lambda x: x[0].lower()+x[1:].upper(),list_a)) 
    return list_a
if __name__ == '__main__':
    assert reverse_cap(['I', 'bought', 'two', 'bananas']) == \
        ['i', 'bOUGHT', 'tWO', 'bANANAS']

    print("All OK!")
