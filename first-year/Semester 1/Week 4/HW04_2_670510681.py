#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW04_2
# 204111 Sec 002

def main():
    test()
    h1 = int(input())
    m1 = int(input())
    p1 = input()
    h2 = int(input())
    m2 = int(input())
    p2 = input()
    print(minute_diff(h1,m1,p1,h2,m2,p2))

def minute_diff(h1: int, m1: int, p1: str, h2: int, m2: int, p2: str) -> int: 
    p1 = p1.upper()
    p2 = p2.upper()
    h1 = abs(h1)
    m1 = abs(m1)
    h2 = abs(h2)
    m2 = abs(m2)
    # แปลงเป็น 24
    if p1 == "PM" and h1 != 12:
        h1 += 12
    if p2 == "PM" and h2 != 12:
        h2 += 12
    if h1 == 12 and p1 == "AM":
        h1 = 0
    if h2 == 12 and p2 == "AM":
        h2 = 0
    # แปลงเป็น นาที จะไม่เพี้ยน
    h1 = h1*60+m1
    h2 = h2*60+m2
    return (abs(h1-h2))

# in one day
def test():
    assert minute_diff(8,23,'AM',8,24,'AM') == 1
    assert minute_diff(8,23,'AM',1,24,'PM') == 301
    assert minute_diff(1,24,'PM',8,23,'AM') == 301
    assert minute_diff(1,24,'PM',8,23,'AM') == 301
    assert minute_diff(12,24,'PM',12,24,'AM') == 720
    assert minute_diff(12,24,'AM',12,24,'PM') == 720
    assert minute_diff(12,00,'AM',1,00,'AM') == 60
    assert minute_diff(11,00,'PM',12,00,'AM') == 1380
    assert minute_diff(12,00,'PM',11,00,'AM') == 60
    assert minute_diff(12,00,'PM',2,00,'PM') == 120
    assert minute_diff(11,59,'AM',12,00,'PM') == 1
    assert minute_diff(11,59,'PM',12,00,'AM') == 1439
    
    print("Ok!")

if __name__ == "__main__":
    main()
