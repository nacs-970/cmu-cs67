#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# Lab12_1
# 204111 Sec 002
# explain Gregorian P'ta

def display_calendar(month: int, year: int) -> None:

    dict_m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    dict_gergor = {1:13, 2:14, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12}
    dict_none = {0:6, 1:0, 2:1, 3:2, 4:3, 5:4, 6:5}

    def leap_year(y:int):   # create local function
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0: return 1
        else: return 0

    days = dict_m[month]

    if month == 1:
        year -= 1

    if month == 2:
        days = dict_m[month] + leap_year(year)
        year -= 1

    # source : https://en.wikipedia.org/wiki/Zeller%27s_congruence#Formula
    k = year%100
    j = year//100

    # q = number day | h = sun, mon, tue [1,2,3,4,5,6,0]
    # q = 0 -> 1/2/2023

    #h = (q + (13*(month+1))//5 + k + (k//4) + 5 - j)%7 # Julian
    h = (1 + ((13 * (dict_gergor[month] + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7 # Gregorian

    l_day = ["--"]*(dict_none[h]) + list(range(1,days+1))

    # display
    print("Su Mo Tu We Th Fr Sa")
    while l_day:
        cutted = l_day[0:7]
        for i in cutted:
            print("{:2} ".format(i),end = "")
        print()
        l_day = l_day[7:]
    print()

if __name__ == "__main__":
    display_calendar(2,2020)
    display_calendar(2,2021)
    display_calendar(2,2022)
    display_calendar(2,2023)
    display_calendar(2,2024)
    display_calendar(2,2025)
    display_calendar(1,1600)
    display_calendar(3,2019)

    #display_calendar(1,2023)
    #display_calendar(2,2023)
    #display_calendar(3,2023)
    #display_calendar(4,2023)
    #display_calendar(2,2024)
    #display_calendar(4,2025)
    #display_calendar(1,2000)
