#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_3
# 204111 Sec 002

DEBUG = False

def three_digits_to_word (num:int) -> str:
    # convert num to word
    num = str(num)
    str_ = ""

    number_table_1 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    number_table_2 = ["","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    lenght = len(num)

    # 111
    if lenght == 3: str_ += number_table_1[int(num[0])] + " hundred"
    
    # 011
    if lenght >= 2:
        
        # 010
        if num[-2] == "1":
            if lenght == 3: str_ += " " # 110 one hundred ten
            str_ += number_table_1[10+int(num[-1])]
            return str_
        if lenght == 3: str_ += " " # 121 one hundred twenty one
        if num[-2] == "0": str_+"" # 100
        else: str_ += number_table_2[int(num[-2])-1] # 110
        
        # 045 not 40
        if num[-2] != "0" and num[-1] != "0": str_ += "-"+number_table_1[int(num[-1])]

        # 001
        else: str_ += number_table_1[int(num[-1])]
    
    # 001
    if lenght == 1: str_ += number_table_1[int(num[0])]

    return str_.strip() # remove unwanted whitespace

def num_to_word (num:int) -> str:
    digit_len = len(str(num))
    if num == 0:return("zero")
    
    # split to three
    if digit_len > 3:
        if digit_len in [4,7,10]: # thousand,million and billion
            front = list(map(lambda x: str(num)[-x],list(range(0,digit_len,digit_len))))
            front = [front[-1]]
        else: front = []
        
        # count from behind
        back = list(map(lambda x: str(num)[-(x+2):-x]+str(num)[-x],list(range(1,digit_len,3))))
    else: front,back = [num],[]
    
    # join front and back
    slice_ = []
    slice_.extend(front)
    slice_.extend(back[::-1])
    slice_ = list(map(lambda x: int(x),slice_))

    range_ = list(range(len(slice_)))
    len_ = len(slice_)
    
    # filter 0 when more than 1 digit
    if len_ >= 2: slice_ = list(map(lambda x: "" if slice_[x]==0 else slice_[x],range_))
    
    # turn into word
    range_ = list(range(len(slice_)))
    str_ = list(map(lambda x: three_digits_to_word(slice_[x]),range_))

    slice_ = list(map(lambda x: str(x),slice_))

    if len_ >= 3: # 1,000,000
        if len_ == 4: str_[0] += ' billion' # 1,000,000,000
        if str_[-3] != '':str_[-3] += ' million'
    if len_ >= 2 and slice_[-2] != '':
        str_[-2] += ' thousand'

    #DEBUG
    if DEBUG:
        print(slice_)
        print(str_)
        print(" ".join(str_).strip())
        
    #remove whitespace
    return " ".join(str_).strip()
    

def test():
    assert num_to_word(42641323862) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"
    assert num_to_word(00000) == "zero"
    assert num_to_word(0) == "zero"
    assert num_to_word(111) == "one hundred eleven"
    assert num_to_word(100000000000) == "one hundred billion"
    assert num_to_word(10000000000) == "ten billion"
    assert num_to_word(1000000000) == "one billion"
    assert num_to_word(100000000) == "one hundred million"
    assert num_to_word(10000000) == "ten million"
    assert num_to_word(1000000) == "one million"
    assert num_to_word(100000) == "one hundred thousand"
    assert num_to_word(10000) == "ten thousand"
    assert num_to_word(1000) == "one thousand"
    assert num_to_word(100) == "one hundred"
    assert num_to_word(123456789012) == "one hundred twenty-three billion four hundred fifty-six million seven hundred eighty-nine thousand twelve"
    assert num_to_word(999999999999) == "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine"
    print("- < -")


if __name__ == "__main__":
    test()
    num_to_word(100)
    num_to_word(0000000000)
    num_to_word(1000000001)
    num_to_word(42641323862)
    #num_to_word(123456789012)
    #num_to_word(12345678901)
    #num_to_word(1234567890)
    #num_to_word(123456789)
    #num_to_word(12345678)
    #num_to_word(1234567)
    #num_to_word(123456)
    #num_to_word(12345)
    #num_to_word(1234)
    #num_to_word(123)
    #num_to_word(923)
    #num_to_word(953)
    #num_to_word(910)
    #num_to_word(920)
    #num_to_word(913)
    num_to_word(12)
    num_to_word(14)
    num_to_word(21)
    num_to_word(6)