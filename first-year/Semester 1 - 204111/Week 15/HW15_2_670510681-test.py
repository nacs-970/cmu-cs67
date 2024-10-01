#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# HW15_2
# 204111 Sec 002

from math import ceil
from functools import reduce
import random

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
                    tmp = [" "*6] + tmp
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
        final += ["".join(tmp).rstrip()]
    bot = ["0" + " "*5] + [str(i) + " "*4 for i in range(10,101,10)]
    #print("".join(bot).rstrip())
    final += ["".join(bot).rstrip()]

    if len(scores) == 0:
        final = final[1:]

    #print("\n".join(final))
    return final

def histogram2(scores):
   dict_scores = dict([(range(10), 0), (range(10, 20), 0), (range(20, 30), 0), (range(30, 40), 0),
                       (range(40, 50), 0), (range(50, 60), 0), (range(60, 70), 0), 
                       (range(70, 80), 0), (range(80, 90), 0), (range(90, 101), 0)])
   # print(dict_scores)
   for s in scores:
      for key in dict_scores:
         if s in key:
            # print(key)
            dict_scores[key] = dict_scores.get(key, 0) + 1
   # print(dict_scores)

   max_ = 0
   for value in dict_scores:
      if dict_scores[value] > max_:
         max_ = dict_scores[value]
   # print(max_)

   for i in dict_scores:
      dict_scores[i] = [(" "*6)]*(ceil(max_/5)-ceil(dict_scores[i]/5)) + [" " * (1 if len(str(dict_scores[i])) > 1 else 2) + str(dict_scores[i]) + " "*3, "_"*5] + ["|" + "*"*5 + "|"]*(ceil(dict_scores[i]/5))
   x = list(dict_scores.values())
   # print(x)
   
   result = []
   for i in range(ceil(max_/5)+2):
      line = []
      for j in x:
         line.append(j[i])
      # print(line)
      str_line = reduce(lambda x, y: x + y[1:] if x[len(x)-1] == '|' and (y[0] == '|') else x + " " + y if x[len(x)-1] == '_' and (y[0] == "_" or y[0] == ' ') else x[:len(x)-1] + y if x[len(x)-1] == " " and y[0] == '|' else x + y, line)
      result.append(("" if str_line[0] == "|" else " ")+str_line.rstrip())
   # print(result)
   result.append('0'+" "*5+"10"+" "*4+"20"+" "*4+"30"+" "*4+"40"+" "*4+"50"+" "*4+"60"+" "*4+"70"+" "*4+"80"+" "*4+"90"+" "*4+"100")

   #print("\n".join(result))
   return result

   #for i in result:
   #   print(i)
def test():
    for i in range(1000):
        t = tuple()
        for i in range(random.randint(0,200)):
            t += (random.randint(0,100),)
        try:
            assert histogram(t) == histogram2(t)
        except:
            print(t)
            print("\n".join(histogram(t)))
            print("\n".join(histogram2(t)))
            return 0

if __name__ == "__main__":
    test()
