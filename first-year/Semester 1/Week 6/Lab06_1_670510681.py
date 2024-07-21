#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab06_1
# 204111 Sec 002

def triangle(n:int) -> str:
    num = list(range(1,n-1))
    struct = list(map(lambda x: ((("*")+("."*(x+(x-1)))+("*"))),num))
    end_ = [(n-1)*("* ")+("*")] # "(*\ *\ *\ )*"
    struct =  list("*")+struct+end_
    #print(struct)
    # add newline at the end too
    struct = '\n'.join(struct) + "\n"
    return struct

def test_triangle():

    T3 = '''*
*.*
* * *
''' # this has a \n

    T7 = '''*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * *
'''

    assert triangle(3) == T3
    assert triangle(7) == T7
    print("OK")
if __name__ == "__main__":
    test_triangle()
