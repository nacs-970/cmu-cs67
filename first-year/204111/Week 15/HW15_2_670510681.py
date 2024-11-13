#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# HW15_2
# 204111 Sec 002

#         1           1     3     1                       1 
#   0   _____   0   _____ _____ _____   0     0     0   _____ 
# _____|*****|_____|*****|*****|*****|_____ _____ _____|*****| 
#0     10    20    30    40    50    60    70    80    90    100 

#                                      26 
#                                     _____ 
#                                    |*****| 16 
#                                11  |*****|_____ 
#                           9   _____|*****|*****| 
#         1           2   _____|*****|*****|*****|  5 
#   0   _____   0   _____|*****|*****|*****|*****|_____   0 
# _____|*****|_____|*****|*****|*****|*****|*****|*****|_____ 
#0     10    20    30    40    50    60    70    80    90    100
from math import ceil
def histogram(scores: tuple[int]) -> None:
    ans = []; dict_bin = dict((i,0) for i in range(0,11))

    # categorize scores
    for score in scores:
        dict_bin[(score//10)] = dict_bin.get(score//10,0) + 1

    # bin size 11 | 90 - 100
    dict_bin[9] = dict_bin.get(9) + dict_bin.get(10)
    del dict_bin[10]
        
    #print(dict_bin) 

    # find max height
    max_height = max(dict_bin.values())
    if max_height: max_height = ceil(max_height/5) + 2
    else: max_height = 3

    # max length values for zfill
    max_z = len(str(max(dict_bin.values())))

    # generate bar
    prev = 0; prev_width = 0
    for i in dict_bin:

        value = dict_bin[i]; bar_height = ceil(value/5)

        # zfill
        str_ = " "*( max(1,max_z - len(str(value))) ) + str(value)
        #print(max_z,str_)

        # top of the bar

        len_ = len(str_)
        front = (6-len_)//2; back = 6 - (front + len_)
        if bar_height < prev and prev - bar_height > 1:
            #print(prev_width, str_)
            if prev_width == 6:
                front = (5-len_)//2; back = 5 - (front + len_)
            else:
                front = (4-len_)//2; back = 5 - (front + len_)

        tmp = [" "*front + str_ + " "*back]

        #if ans and bar_height < prev:
        #    l = map(len,ans[prev - bar_height])
        #    b = max(l)
        #    if len_%2 == 1:
        #        front = (b-len_)//2 - (b-len_)%2 ; back = 6 - (front + len_)
        #    else:
        #        front = (b-len_)//2  - (b+1)%2; back = 6 - (front + len_)
            #print(max(l))


        #if bar_height < prev:
        #    front = (5-len_)//2 + (len_%2); back = 6 - (front + len_)


        #front = (6-len_)//2; back = 6 - (front + len_)
        #print(front, len_, back)
        #if len_%2 == 1:back += 1

        #tmp = ["."*(6)]
        #print(len(tmp[0]))

        
        if not bar_height and i == 0:
            tmp += [" _____"]

        elif bar_height == prev:
            tmp += [" _____"]
        elif bar_height < prev:
            tmp += ["_____"]
        else:
            tmp += [" _____"]

        # bar
        for h in range(bar_height):
            str_ = "*****|"

            if (bar_height-h) > prev:
                str_ = "|" + str_ 
                prev_width = len(str_)

            tmp += [str_]
        #tmp += [str(i*10) + "     "]

        # fill
        if bar_height < prev and prev - bar_height > 2:
            for h in range(max_height - len(tmp)):
                if max_height - h > max_height - 1:
                    #print("yes")
                    tmp = [" "*5] + tmp
                else:
                    #print("yes2")
                    tmp = ["."*6] + tmp
        else:
            #print("no")
            tmp = [" "*6]*(max_height - len(tmp)) + tmp
        #tmp = [" "*6]*(max_height - len(tmp)) + tmp
        #if bar_height < prev:
        #    #print("hello")
        #    tmp = [" "*5]*(max_height - len(tmp)) + tmp
        #else:
        #    tmp = [" "*6]*(max_height - len(tmp)) + tmp

        prev = bar_height

        #if not ans:
        #    for l in range(len(tmp)):
        #        tmp[l] = " " + tmp[l]
        #len_ = map(len,tmp)
        #print(max(len_))
        ans += [tmp]

    #for i in range(len(ans[0][:-1])):
    #    ans[0][i] = " " + ans[0][i]

    final = []
    for col in range(max_height):
        tmp = []
        for row in range(len(ans)):
            #print(len(ans[row][col]))
            tmp += [ans[row][col]]
        #print("".join(tmp).rstrip())
        final += ["".join(tmp).replace("|......|","|     |").replace("|......","|     ").replace("."," ").rstrip()]
    bot = ["0" + " "*5] + [str(i) + " "*4 for i in range(10,101,10)]
    #print("".join(bot).rstrip())
    final += ["".join(bot).rstrip()]

    if len(scores) == 0:
        final = final[1:]

    print("\n".join(final))
    #return final
    #print(scores)

import random
if __name__ == "__main__":
    #histogram((1,10,20,30,40,50,60,70,80,90))
    #histogram((1,19, 39, 59, 42, 42, 42, 100))
    #histogram((19, 39, 59, 42, 42, 42, 100))
    histogram((62, 49, 75, 86, 71, 63, 74, 42, 57, 75,56, 58, 67, 78, 63, 73, 60, 49, 66, 77,47, 69, 74, 63, 65, 64, 55, 52, 52, 57,86, 75, 68, 70, 34, 34, 68, 46, 60, 56,60, 65, 66, 70, 64, 84, 61, 46, 60, 76,59, 64, 68, 69, 68, 47, 72, 80, 11, 44,53, 70, 50, 79, 81, 68, 75, 48, 62, 68))
    histogram((86, 43, 48, 20, 14, 89, 43, 20, 26, 82, 21, 28, 88, 77, 12, 42, 42, 78, 93, 94, 85, 67, 39, 48, 83, 37, 71, 52, 36, 14, 86, 63, 34, 54, 21, 27, 88, 55, 51, 14, 66, 100, 93, 91, 26, 58, 27, 46, 10, 23, 41,33, 13, 41, 22, 23, 76, 37, 79, 51, 10, 86, 83, 20, 42, 76, 80, 37, 70, 82, 23, 74, 20, 99, 22, 9, 43, 59, 63, 20, 27, 11, 75, 61, 45))
    histogram((59, 85, 98, 88, 78, 35, 71, 27, 88, 40, 12, 25, 48, 46, 9, 34, 75, 79, 59, 62, 70, 13, 35, 40, 9, 81, 58, 96, 27, 16, 44, 94, 100, 53, 10, 49, 79, 90, 73, 25, 22, 71, 12, 19, 46, 93, 21, 92, 63, 19, 61, 70, 68, 99, 23, 72, 94, 98, 30, 64, 38, 72, 92, 32, 44, 73, 80, 19, 49, 17, 29, 76, 72, 60, 24, 64, 23, 75, 86, 24, 38, 40, 83, 75, 72, 79, 88, 100, 19, 36, 60, 92, 28, 46, 96, 11, 15))
    histogram((30, 80, 39, 95, 17, 30, 46, 68, 62, 60, 34, 95, 23, 48, 56, 92, 39, 83, 11, 79, 54, 42, 71, 49, 42, 15, 69, 63, 26, 10, 64, 56, 89, 87, 100, 61, 85, 42, 61, 42, 43, 60, 98, 24, 11, 11, 38, 10, 50, 93, 75,78, 56, 87, 63, 38, 11, 24, 92, 15, 92, 71, 14, 72, 23, 99, 31, 40, 70, 63, 89, 26, 12, 75, 49, 17, 67, 50, 18, 15, 57, 76, 95, 16, 19, 57, 78, 88, 76, 47, 14, 43, 43, 65, 75, 39, 73, 41, 78, 43, 18, 87, 82, 23, 30, 66, 42, 37, 74, 34, 38, 35, 76, 37, 53, 20, 53, 47, 80, 78, 75, 34, 11, 95, 32, 10, 77, 27, 51, 94, 75, 65, 53, 47, 76, 43, 69, 9, 11, 23, 34, 25, 58, 26, 56, 40, 60, 44, 18, 63, 98, 24, 80, 35, 86, 63, 95, 58, 24, 10, 41, 92, 93, 61, 42, 73, 89, 80, 34, 60, 53, 66, 75, 68, 70, 97, 31, 60, 68, 38, 99, 76, 38, 31, 25, 43, 35, 20, 36, 88, 48, 73, 25)) 
    histogram((27, 94, 5, 28, 83, 14, 44, 46, 29, 55, 28, 92, 46, 56, 8, 5, 45, 27, 41, 57, 1, 41, 51, 32, 89, 91, 71, 73, 49, 51, 82, 12, 88, 23, 26, 25, 26, 48, 27, 61, 82, 62, 70, 42, 41, 51, 8, 16, 90, 15, 48, 6, 55, 43, 46, 28, 35, 2, 5, 49, 44, 16, 30, 65, 58, 100, 29, 73, 32, 97, 77, 80, 53, 29, 61, 44, 38, 11, 29, 72, 8, 27, 17, 56, 10, 64, 51, 85, 79, 90, 89, 27, 80, 22, 21, 80, 63, 66))
    histogram((79, 64, 27, 43, 23, 4, 79, 45, 45, 64, 61, 37, 76, 36, 73, 71, 91, 4, 22, 14, 51, 53, 4, 62, 26, 91, 79, 30, 4, 33, 99, 5, 1, 39, 78, 61, 25, 78, 64, 69, 20, 93, 60, 43, 14, 97, 75, 99, 38, 21, 95, 68, 64, 55, 40, 77, 27, 57, 55, 29, 32, 11, 31, 98, 35, 9, 50, 91, 58, 20, 61, 25, 98, 43, 77, 77, 100, 29, 29, 48, 11, 63, 74, 93, 49, 84, 67, 60, 58, 51, 5, 85, 37, 22, 74, 94, 44, 95, 41, 76, 16, 59, 24, 91, 72, 35, 78, 83, 30, 50, 33, 84, 91, 45, 75, 63, 50, 47, 19, 58, 97, 74, 13, 58, 54, 43, 63, 99, 58, 70, 55, 67, 46, 46, 2, 5, 60, 0, 36, 65, 85, 7, 94, 66, 3, 70, 22, 70, 51, 47, 62, 25, 31, 94, 54, 1, 7, 53, 72, 58, 99, 55, 4, 91, 6, 69, 92, 25, 73, 16, 2, 10, 35, 76, 34, 72, 67))

    #histogram(tuple(range(101))) 
    histogram(tuple()) 
    #histogram(tuple( random.randint(9,100) for x in range(random.randint(0,200))))
