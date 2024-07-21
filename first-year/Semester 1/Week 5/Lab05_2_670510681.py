#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab05_02 
# 204111 Sec 002

# ex : 1 2 2024 = 72
#    : 13 4 2024 = 0

def main():
    test()
    
def count_down_to_songkran(d:int,m:int,y:int) -> int:
    # create local function
    def leap_year(y:int):
        if y % 4 == 0:
            if y % 400 == 0:
                return 1
            elif y % 100 == 0:
                return 0
            else:
                return 1
        else:
            return 0
    
    def sum_month(m:int,y:int):
        #month = "31,28,31,30,31,30,31,31,30,31,30,31"
        # 31 = 7 | 30 = 4 | 28 = 1
        #sum day start from 1/1
        leap = leap_year(y)
        if m == 1:
            return 31
        elif m == 2:
            return 31 + 28 + leap
        elif m == 3:
            return (2*31)+(28+leap)
        elif m == 4:
            return (2*31)+(1*30)+(28+leap)
        elif m == 5:
            return (3*31)+(1*30)+(28+leap)
        elif m == 6:
            return (3*31)+(2*30)+(28+leap)
        elif m == 7:
            return (4*31)+(2*30)+(28+leap)
        elif m == 8:
            return (5*31)+(2*30)+(28+leap)
        elif m == 9:
            return (5*31)+(3*30)+(28+leap)
        elif m == 10:
            return (6*31)+(3*30)+(28+leap)
        elif m == 11:
            return (6*31)+(4*30)+(28+leap)
        elif m == 12:
            return (7*31)+(4*30)+(28+leap)
    
    def remain_day_in_month(d:int,m:int,y:int):
        # find the remaining day of that month
        leap = leap_year(y)
        if m == 2:
            return 28 + leap - d
        else:
            if m == 4 or m == 6 or m == 9 or m == 11:
            #if str(m) in '4,6,9,11'.split(','):
                return 30 - d
            else:
                return 31 - d

    leap = leap_year(y)
    dayremain = remain_day_in_month(d,m,y)
    sum_ = sum_month(m,y)
    songkran = abs(102+leap-(sum_-dayremain)+1)  # 102 from 1/1, using abs for a jump
    
    # 1-4 normal sum , 5++ add 1 year
    # check if is less or equal to 13/4
    if m == 4 and d <= 13:
        return 13-d
    #jump
    elif m >= 4:
        # 365 - remaining day of that year
        songkran = 365+leap_year(y+1)-songkran
        return songkran
    # don't jump
    else:
        return songkran 

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
    assert count_down_to_songkran(14,4,99) == 365
    print(":)")
    
if __name__ == "__main__":
    main()
