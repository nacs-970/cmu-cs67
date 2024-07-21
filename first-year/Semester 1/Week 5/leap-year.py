#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# 
# 204111 Sec 002
import random
def main():
    r = random.randint(2000,3000)
    print(r)
    print(leapyear(r))

def leapyear(year:int) -> bool:
    return year%4 == 0

if __name__ == "__main__":
    main()
