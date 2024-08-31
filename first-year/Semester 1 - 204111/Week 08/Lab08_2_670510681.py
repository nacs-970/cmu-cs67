#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab08_2
# 204111 Sec 002

def reverse_digits(x:int) -> int:
    absx = abs(x) # Negative number

    #if len(str(x)) == 0: return x # last one
    if x//10 == 0: return x # last one

    power = len(str(absx))-1
    head = reverse_digits(absx//10)
    tail = reverse_digits(absx%10)

    #return int(str(tail)+str(head))
    #return int(''.join([str(tail),str(head)]))

    ans = tail*10**(power) + head # head is x//10
    if x < 0: return ans * -1 # Negative number
    return ans



if __name__ == "__main__":
    print(reverse_digits(1234))
    print(reverse_digits(123456789))
    print(reverse_digits(1211))
    print(reverse_digits(1))
    print(reverse_digits(100))
    print(reverse_digits(-123))
