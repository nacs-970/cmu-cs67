#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab05_02 
# 204111 Sec 002

# 1 m = 30.4575
# ex : 1 2 2024 = 72
#    : 13 4 2024 = 0

def main():
    test()

def count_down_to_songkran(d:int,m:int,y:int) -> int:
    
    def leap_year(y:int):   # create local function
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0: return 1
        else: return 0
    
    def sum_month(m:int,y:int): # reminder that miss from 30*m 
        leap = leap_year(y)
        if m == 1: return 1 # 30 + 1
        elif m == 2: return leap-1 # 59 + leap
        elif m == 3 or m == 4: return leap # 90;120 + leap
        elif m == 5 or m ==6: return leap+1 # 150;180 + leap + 1
        elif m == 7: return leap+2 # 210 + leap + 2
        elif m == 8 or m == 9: return leap+3 # 240;270 + leap + 3
        elif m == 10 or m == 11: return leap+4 # 300;330 + leap + 4
        else: return leap+5 # 360 + leap + 5
    
    def remain_day_in_month(d:int,m:int,y:int): # find the remaining day of that month
        leap = leap_year(y)
        if m == 2: return 28 + leap - d
        elif m == 4 or m == 6 or m == 9 or m == 11: return 30 - d
        else: return 31 - d

    songkran = abs(102+leap_year(y)-(((30*m)+sum_month(m,y))-(remain_day_in_month(d,m,y)))+1)  # 102 from 1/1, using abs for a jump
    
    if m == 4 and d <= 13: return 13-d # 13/4 check
    elif m >= 4: return 365+leap_year(y+1)-songkran #jump
    else: return songkran # don't

def test():
    assert count_down_to_songkran(13,4,2025) == 0
    assert count_down_to_songkran(13,4,2024) == 0
    assert count_down_to_songkran(13,4,2023) == 0
    assert count_down_to_songkran(1,2,2024) == 72 
    assert count_down_to_songkran(4,2,2025) == 68 
    assert count_down_to_songkran(1,1,2024) == 103
    assert count_down_to_songkran(12,4,2024) == 1
    assert count_down_to_songkran(12,4,2025) == 1
    assert count_down_to_songkran(15,2,2024) == 58
    assert count_down_to_songkran(31,3,2024) == 13
    assert count_down_to_songkran(20,3,2024) == 24
    assert count_down_to_songkran(14,4,2024) == 364
    assert count_down_to_songkran(14,4,2025) == 364
    assert count_down_to_songkran(14,4,2023) == 365
    assert count_down_to_songkran(29,2,2024) == 44
    assert count_down_to_songkran(31,12,2024) == 103
    assert count_down_to_songkran(31,12,2025) == 103
    assert count_down_to_songkran(31,12,2023) == 104
    assert count_down_to_songkran(27,10,2023) == 169
    assert count_down_to_songkran(27,10,2024) == 168
    assert count_down_to_songkran(31,10,2024) == 164
    assert count_down_to_songkran(13,10,2024) == 182
    assert count_down_to_songkran(13,10,2023) == 183
    assert count_down_to_songkran(13,10,2023) == 183
    assert count_down_to_songkran(23,8,2023) == 234
    assert count_down_to_songkran(1,4,1600) == 12
    assert count_down_to_songkran(1,4,1600) == 12
    assert count_down_to_songkran(22,7,3000) == 265
    assert count_down_to_songkran(11,11,11) == 154
    #assert count_down_to_songkran(14,4,99) == 364
    print(":)")
    
if __name__ == "__main__":
    main()