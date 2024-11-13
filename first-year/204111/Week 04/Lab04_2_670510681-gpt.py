#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab04_2
# 204111 Sec 002

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    my_min_mid_max(a,b,c)

def my_min_mid_max(a:int,b:int,c:int) -> None:
    min_,max_ = a,a
    if b<min_:
        min_=b
    if c<min_:
        min_=c

    if b>max_:
        max_=b
    if c>max_:
        max_=c
    mid = (a+b+c)-min_-max_
    print(f"min = {min_}")
    print(f"mid = {mid}")
    print(f"max = {max_}")

def my_min_mid_max_2(a:int,b:int,c:int) -> None:
    # P'ta
    mid_ = c
    if a>b:
        max_=a
        min_=b
    else:
        max_=b
        min_=a
    
    if c>max_:
        mid_=max_
        max_=c
        
    elif c<min_:
        mid_=min_
        min_=c
    print(f"min = {min_}")
    print(f"mid = {mid_}")
    print(f"max = {max_}")

def test():
  #assert(my_min_mid_max(1,2,3)) == 3,2,1
  pass

if __name__ == "__main__":
    main()
