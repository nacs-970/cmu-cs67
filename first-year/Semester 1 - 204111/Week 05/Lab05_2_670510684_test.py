#!/usr/bin/env python3
# Onichar Kitilungka (Toey)
# 670510684
# Lab05_2
# 204111 Sec 002
from random import randint

def main():
    
    d = int(input())
    m = int(input())
    y = int(input())
    print(count_down_to_songkran(d,m,y))
    
def count_down_to_songkran(d:int , m:int , y:int ) -> int:
    
    if d==13 and m == 4:
        return 0
    if d>13 and m==4:
        y = y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (30-d)+335+13+1
            return days
        else:
            days = (30-d)+335+13
            return days
    if d<13 and m==4:
        days = 13-d
        return days
        
    if m==1:
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (31-d)+59+13+1
            return days
        else:
            days = (31-d)+59+13
            return days
            
    if m==2:
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (28-d)+31+13+1
            return days
        else:
            days = (28-d)+31+13
            return days
            
    if m==3:
        days = (31-d)+13
        return days
        
    if m==5:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (31-d)+304+13+1
            return days
        else:
            days = (31-d)+304+13
            return days
            
    if m==6:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (30-d)+274+13+1
            return days
        else:
            days = (30-d)+274+13
            return days
            
    if m==7:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (31-d)+243+13+1
            return days
        else:
            days = (31-d)+243+13
            return days
            
    if m==8:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (31-d)+243+13+1
            return days
        else:
            days = (31-d)+243+13
            return days
            
    if m==9:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (30-d)+213+13+1
            return days
        else:
            days = (30-d)+213+13
            return days
            
    if m==10:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (31-d)+182+13+1
            return days
        else:
            days = (31-d)+182+13
            return days
            
    if m==11:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (30-d)+152+13+1
            return days
        else:
            days = (30-d)+152+13
            return days
            
    if m==12:
        y=y+1
        if ((y%4==0 and y%100!=0)or(y%4==0 and y%400==0)):
            days = (31-d)+121+13+1
            return days
        else:
            days = (31-d)+121+13
            return days
        
def count_down_to_songkran_tun(d:int,m:int,y:int) -> int:
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
    
    def summonth(m:int,y:int):
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
    sum_ = summonth(m,y)
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

def count_down_to_songkran_short(d:int,m:int,y:int) -> int:
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

    leap = leap_year(y)
    dayremain = remain_day_in_month(d,m,y)
    sum_ = (30*m)+sum_month(m,y)
    songkran = abs(102+leap-(sum_-dayremain)+1)  # 102 from 1/1, using abs for a jump
    
    if m == 4 and d <= 13: return 13-d # 13/4 check
    elif m >= 4: return 365+leap_year(y+1)-songkran #jump
    else: return songkran # don't

def count_down_to_songkran(d: int,m: int,y :int):    
    def Feb_days(Leap_year_status):
        if Leap_year_status==True:
            return 29
        else:
            return 28

    def Leap_status(y :int):
        if y % 4 == 0:
            if y % 400 == 0:
                return True
            elif y % 100 == 0:
                return False
            else:
                return True
        else:
            return False
    
    if m<4 :
        Leap_year_status = Leap_status(y) 
        Feb = Feb_days(Leap_year_status)
        
        if(m==1):
            return (31-d)+Feb+31+(13)
        elif(m==2):
            return (Feb-d)+31+(13)
        elif(m==3):
            return (31-d)+(13)

    elif m>4 :
        Leap_year_status = Leap_status(y+1)
        Feb = Feb_days(Leap_year_status)
        
        if(m==5):
            return (31-d)+(31*6)+(30*3)+Feb+(13)
        elif(m==6):
            return (30-d)+(31*6)+(30*2)+Feb+(13)
        elif(m==7):
            return (31-d)+(31*5)+(30*2)+Feb+(13)
        elif(m==8):
            return (31-d)+(31*4)+(30*2)+Feb+(13)
        elif(m==9):
            return (30-d)+(31*4)+(30)+Feb+(13)
        elif(m==10):
            return (31-d)+(31*3)+(30)+Feb+(13)
        elif(m==11):
            return (30-d)+(31*3)+Feb+(13)
        elif(m==12):
            return (31-d)+(31*2)+Feb+(13)
    else:                                   
        Leap_year_status = Leap_status(y) 
        Feb = Feb_days(Leap_year_status)
        
        if d<13:
            return 13-d
        elif d>13:
            return (30-d) + (31*7) + (30*3) + 12 + Feb
        elif d==13:
            return 0 

def test():
    for i in range(1,10000):
        d = randint(1,28)
        m = randint(1,12)
        y = randint(1,3999)
        try:
            assert count_down_to_songkran(d,m,y) == count_down_to_songkran_short(d,m,y)
        except:
            print(d,m,y)
            print("expect",count_down_to_songkran_short(d,m,y))
            print("got",count_down_to_songkran(d,m,y))
            return 0
    print("@~@")

if __name__ == '__main__':
    test()
    #main()