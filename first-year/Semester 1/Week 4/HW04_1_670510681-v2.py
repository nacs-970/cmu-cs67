#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW04_1
# 204111 Sec 002
import random
def main():
    test()
    #p = int(input())
    #c = int(input())
    #print(calculate_exp(p,c))

def calculate_exp_13(p: int, c: int) -> int:
    if p > 0:
        total = p+c
        max_evolve = ((total-13)//11) + 1
        if p <= max_evolve:
            return p*1000
        else:
            return max_evolve*1000
    else:
        return 0

def calculate_exp_2(p: int, c: int) -> int:
    if p > 0:
        total = p+c
        # -2 ทุกครั้งที่evolveจะต้องเก็บ p ไว้ 1 สำหรับครั้งหน้าและเสีย p 1 ตัวไป
        max_evolve = abs((total-2))//11
        if p <= max_evolve:
          return p*1000
        else:
          return max_evolve*1000
    else:
        return 0

def calculate_exp_short(p: int, c: int) -> int:
    #max_evolve = abs((p+c-2))//11
    #max_evolve = (((p+c-13))//11)+1
    # min idea by P'Newton
    return min((p),abs(((p+c-13)//11)+1))*1000
    #return min((p),max_evolve)*1000

def test():
    #assert calculate_exp(20,1) == 1000
    #assert calculate_exp(20,11) == 2000
    #assert calculate_exp(1,12) == 1000
    #assert calculate_exp(11,12) == 1000
    #assert calculate_exp(24,0) == 2000
    #assert calculate_exp(13,0) == 1000
    #assert calculate_exp(2,12) == 1000
    #assert calculate_exp(2,22) == 2000
    #assert calculate_exp(120,0) == 10000
    #assert calculate_exp(6,62) == 6000
    #assert calculate_exp(6,61) == 5000
    #assert calculate_exp(1200,0) == 108000
    #assert calculate_exp(0,0) == 0
    # idea by ice cj
    for i in range(100000):
        p = random.randint(0,100)
        c = random.randint(0,100)
        # try ลองจนกว่าจะ error
        try:
            assert calculate_exp_short(p,c) == calculate_exp_13(p,c)
        # เมื่อ error แล้วให้มาทำ except
        except:
            print("Invalid Case")
            print(p,c)
            print(f"expct : {calculate_exp_13(p,c)}, got: {calculate_exp_short(p,c)}")
            return 0
    print(":)")
if __name__ == "__main__":
    main()
