#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_1
# 204111 Sec 002

def words_to_num(words:str) -> int:
    unit_list = { "zero":0,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10,
                 "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, 
                 "eighteen":18, "nineteen":19, "twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}

    billion,million,thousand,hundred = "zero","zero","zero",words

    if 'thousand' in words:
        thousand,hundred = words.split('thousand')
    if 'million' in words:
        million,thousand = thousand.split('million')
    if 'billion' in words:
        billion,million = million.split('billion')
    
    billion = billion.strip()
    million = million.strip()
    thousand = thousand.strip()
    hundred = hundred.strip()

    def convertion(txt):
        num = 0
        txt = txt.split()

        while txt:
            if txt[0].strip() == 'hundred':
                num *= 100
            elif "-" in txt[0]:
                ten,digit = txt[0].split('-')
                num += unit_list[ten] + unit_list[digit]
            else:
                num += unit_list[txt[0]]
            txt = txt[1:]

        return num

    billion = convertion(billion) * 10**9
    million = convertion(million) * 10**6
    thousand = convertion(thousand) * 10**3
    hundred = convertion(hundred)
    return billion + million + thousand + hundred

DEBUG = False

def three_digits_to_word (num:int) -> str:
    unit_list = ["", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"]
    unit_list_10 = ["","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    more_ten, digit = divmod(num,10)
    hundred, ten = divmod(more_ten,10)
    
    dash = ""
    if ten == 1:
        ten = unit_list[10+digit]
        digit = ""
    elif ten == 0:
        digit = unit_list[digit]
        ten = unit_list_10[ten]
    elif digit == 0:
        digit = unit_list[digit]
        ten = unit_list_10[ten-1]
    else:
        dash = "-"
        digit = unit_list[digit]
        ten = unit_list_10[ten-1]

    if hundred == 0: hundred_text= ""
    else: hundred_text = " hundred "

    hundred = unit_list[hundred]
    return (hundred + hundred_text + ten + dash + digit).strip()


def num_to_word (num:int) -> str:
    if num == 0:return "zero"

    # mod and floor method
    #billion = num // 10**10
    #million = num % 10**10
    #thousand = million % 10**3
    #million = million // 10**7
    #hundred = thousand % 10**2
    #thousand = thousand // 10**3
    #hundred = hundred // 10**2

    # divmod
    more_thousand,hundred = divmod(num,1000)
    more_million,thousand = divmod(more_thousand,1000)
    more_billion,million = divmod(more_million,1000)
    more_zillion,billion = divmod(more_billion,1000)
    
    if DEBUG == True:
        print(more_thousand,more_million,more_billion,more_zillion)
        print(hundred,thousand,million,billion)
        
    if hundred == 0:hundred=""
    else:hundred = three_digits_to_word(hundred)
    if thousand == 0:thousand=""
    else:thousand = three_digits_to_word(thousand)+" thousand "
    if million == 0:million=""
    else:million = three_digits_to_word(million)+" million "
    if billion == 0:billion=""
    else:billion = three_digits_to_word(billion)+" billion "
    
    return (billion+million+thousand+hundred).strip()
import random
def test():
    for i in range(100000):
        n = random.randint(0,999999999999)
        str_ = num_to_word(n)
        try:
            words_to_num(str_) 
        except:
            print(str_)
            return 0
    
if __name__ == "__main__":
    test()
