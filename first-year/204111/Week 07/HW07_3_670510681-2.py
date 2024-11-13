#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_3
# 204111 Sec 002

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
    
def test():
    assert num_to_word(42641323862) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"
    assert num_to_word(0) == "zero"
    assert num_to_word(111) == "one hundred eleven"
    assert num_to_word(1000) == "one thousand"
    assert num_to_word(100) == "one hundred"
    assert num_to_word(123456789012) == "one hundred twenty-three billion four hundred fifty-six million seven hundred eighty-nine thousand twelve"
    assert num_to_word(999999999999) == "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine"

    print("- < -")

if __name__ == "__main__":
    test()