#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_3
# 204111 Sec 002

def three_digits_to_word (num:int) -> str:
    # convert num to word
    num = str(num)
    str_ = ""

    number_table_1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number_table_2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    number_table_3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    number_table_4 = ["hundred","thousand","million","billion"]

    lenght = len(num)
    #if num 
    if lenght == 3:
        #a = list(map(lambda x: slice[0][0]==str(x),list(range(10))))
        #return print(a)

        if num[0] == "1":str_ += number_table_1[1]+" hundred"
        if num[0] == "2":str_ += number_table_1[2]+" hundred"
        if num[0] == "3":str_ += number_table_1[3]+" hundred"
        if num[0] == "4":str_ += number_table_1[4]+" hundred"
        if num[0] == "5":str_ += number_table_1[5]+" hundred"
        if num[0] == "6":str_ += number_table_1[6]+" hundred"
        if num[0] == "7":str_ += number_table_1[7]+" hundred"
        if num[0] == "8":str_ += number_table_1[8]+" hundred"
        if num[0] == "9":str_ += number_table_1[9]+" hundred"

    if lenght >= 2:

        if num[-2] == "1":
            if lenght == 3: str_ += " "
            if num[-1] == "0":str_ += number_table_2[0]
            if num[-1] == "1":str_ += number_table_2[1]
            if num[-1] == "2":str_ += number_table_2[2]
            if num[-1] == "3":str_ += number_table_2[3]
            if num[-1] == "4":str_ += number_table_2[4]
            if num[-1] == "5":str_ += number_table_2[5]
            if num[-1] == "6":str_ += number_table_2[6]
            if num[-1] == "7":str_ += number_table_2[7]
            if num[-1] == "8":str_ += number_table_2[8]
            if num[-1] == "9":str_ += number_table_2[9]
            return str_

        if lenght == 3: str_ += " "
        if num[-2] == "2":str_ += number_table_3[0]
        if num[-2] == "3":str_ += number_table_3[1]
        if num[-2] == "4":str_ += number_table_3[2]
        if num[-2] == "5":str_ += number_table_3[3]
        if num[-2] == "6":str_ += number_table_3[4]
        if num[-2] == "7":str_ += number_table_3[5]
        if num[-2] == "8":str_ += number_table_3[6]
        if num[-2] == "9":str_ += number_table_3[7]

        if num[-2] != "0":
            if num[-1] == "1":str_ += "-"+number_table_1[1]
            if num[-1] == "2":str_ += "-"+number_table_1[2]
            if num[-1] == "3":str_ += "-"+number_table_1[3]
            if num[-1] == "4":str_ += "-"+number_table_1[4]
            if num[-1] == "5":str_ += "-"+number_table_1[5]
            if num[-1] == "6":str_ += "-"+number_table_1[6]
            if num[-1] == "7":str_ += "-"+number_table_1[7]
            if num[-1] == "8":str_ += "-"+number_table_1[8]
            if num[-1] == "9":str_ += "-"+number_table_1[9]
        else:
            if num[-1] == "0":str_ += ""
            if num[-1] == "1":str_ += number_table_1[1]
            if num[-1] == "2":str_ += number_table_1[2]
            if num[-1] == "3":str_ += number_table_1[3]
            if num[-1] == "4":str_ += number_table_1[4]
            if num[-1] == "5":str_ += number_table_1[5]
            if num[-1] == "6":str_ += number_table_1[6]
            if num[-1] == "7":str_ += number_table_1[7]
            if num[-1] == "8":str_ += number_table_1[8]
            if num[-1] == "9":str_ += number_table_1[9]
    
    if lenght == 1:
        if num[0] == "0":str_ += number_table_1[0]
        if num[0] == "1":str_ += number_table_1[1]
        if num[0] == "2":str_ += number_table_1[2]
        if num[0] == "3":str_ += number_table_1[3]
        if num[0] == "4":str_ += number_table_1[4]
        if num[0] == "5":str_ += number_table_1[5]
        if num[0] == "6":str_ += number_table_1[6]
        if num[0] == "7":str_ += number_table_1[7]
        if num[0] == "8":str_ += number_table_1[8]
        if num[0] == "9":str_ += number_table_1[9]

    return str_.strip() # remove unwanted whitespace

def num_to_word (num:int) -> str:

    digit_len = len(str(num))

    # int filter
    index_ = list(filter(lambda x: str(num)[x].isdigit(),list(range(digit_len))))
    num = list(map(lambda x: str(num)[x],index_))
    num = int("".join(num))

    #if digit_len != 0: quot,rem = divmod(num,10**digit_len)# division result (quotient) , remainder

    # split to three
    if digit_len > 3:
        if digit_len in [4,7,10]: # thousand and million
            #front = [num//(10**(digit_len-1))]
            front = list(map(lambda x: str(num)[-x],list(range(0,digit_len,digit_len))))
            #front = list(map(lambda x:divmod(num,10**x)[0],list(range(digit_len))))
            front = [front[-1]]
        else: front = []
        back = list(map(lambda x: str(num)[-(x+2):-x]+str(num)[-x],list(range(1,digit_len,3))))
        #quot = list(map(lambda x:divmod(num,10**x)[0],list(range(digit_len))))
        #rem = list(map(lambda x:divmod(num,10**x)[1],list(range(1,digit_len))))
    else: front,back = [num],[]
    #print(front,back)
    #front = list(map(lambda x: str(x),front))
    #back = list(map(lambda x: str(x),back))

    slice_ = []
    slice_.extend(front)
    slice_.extend(back[::-1])
    #slice_ = list(map(lambda x: str(x),slice_))
    slice_ = list(map(lambda x: int(x),slice_))
    

    #slice_ = list(map(lambda x: [x],slice_))

    range_ = list(range(len(slice_)))
    len_ = len(slice_)
    
    #return print(slice_)
    # filter 0 when more than 1
    if len_ >= 2: slice_ = list(map(lambda x: "" if slice_[x]==0 else slice_[x],range_))
    #if len_ >= 2: slice_ = list(filter(lambda x: x!=0,slice_))
    #return print(slice_)
    
    # turn into word
    range_ = list(range(len(slice_)))
    str_ = list(map(lambda x: three_digits_to_word(slice_[x]),range_))

    #len_ = len(slice_)
    slice_ = list(map(lambda x: str(x),slice_))
    

    ## have a decimal separator
    #if len_ >= 3:
    #    if len_ == 4:
    #        print(slice_[0])
    #        if len(slice_[0]) == 1:
    #            str_[0] += ' thousand million'
    #            if 
    #        else:
    #            str_[0] += ' billion'
    #            str_[1] += ' million'
    #    else: str_[0] += ' million'

    #if len_ >= 2 and str_[-2]!="":
    #    len_t = len(slice_[-2]) # thousand
    #    str_[-2] += ' thousand'
    #    #return print(str_)
    #str_ = list(map(lambda x: slice_[x],range_))
    
    if len_ >= 3:
        if len_ == 4: str_[0] += ' billion'
        if str_[-3] != '':str_[-3] += ' million'
    if len_ >= 2 and slice_[-2] != '':
        str_[-2] += ' thousand'
    
    #remove whitespace
    str_ = list(filter(lambda x: x != '',str_))

    #print(slice_)
    #print(str_)
    #print(" ".join(str_))
    return " ".join(str_)

DEBUG = False

def three_digits_to_word2 (num:int) -> str:
    # convert num to word
    num = str(num)
    str_ = ""

    number_table_1 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number_table_2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    number_table_3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    number_table_4 = ["hundred","thousand","million","billion"]

    lenght = len(num)

    # 111
    if lenght == 3: str_ += number_table_1[int(num[0])] + " hundred"
    
    # 011
    if lenght >= 2:
        # 010
        if num[-2] == "1":
            if lenght == 3: str_ += " "
            str_ += number_table_2[int(num[-1])]
            return str_
        if lenght == 3: str_ += " " # 110 one hundred ten
        if num[-2] == "0": str_+"" # 100
        else: str_ += number_table_3[int(num[-2])-2] # 110
        
        # 045
        if num[-2] != "0" and num[-1] != "0": str_ += "-"+number_table_1[int(num[-1])]

        # 001
        else:
            #if num[-1] == "0":str_ += ""
            str_ += number_table_1[int(num[-1])]
    
    # 001
    if lenght == 1 and num[0] != "0": str_ += number_table_1[int(num[0])]
    if lenght == 1 and num[0] == "0": str_ += "zero"

    return str_.strip() # remove unwanted whitespace

def num_to_word2 (num:int) -> str:
    digit_len = len(str(num))

    # int filter
    index_ = list(filter(lambda x: str(num)[x].isdigit(),list(range(digit_len))))
    num = list(map(lambda x: str(num)[x],index_))
    num = int("".join(num))

    # split to three
    if digit_len > 3:
        if digit_len in [4,7,10]: # thousand,million and billion
            front = list(map(lambda x: str(num)[-x],list(range(0,digit_len,digit_len))))
            front = [front[-1]]
        else: front = []
        back = list(map(lambda x: str(num)[-(x+2):-x]+str(num)[-x],list(range(1,digit_len,3))))
    else: front,back = [num],[]
    # join front and back
    slice_ = []
    slice_.extend(front)
    slice_.extend(back[::-1])
    slice_ = list(map(lambda x: int(x),slice_))

    range_ = list(range(len(slice_)))
    len_ = len(slice_)
    
    # filter 0 when more than 1
    if len_ >= 2: slice_ = list(map(lambda x: "" if slice_[x]==0 else slice_[x],range_))
    
    # turn into word
    range_ = list(range(len(slice_)))
    str_ = list(map(lambda x: three_digits_to_word2(slice_[x]),range_))

    slice_ = list(map(lambda x: str(x),slice_))

    if len_ >= 3:
        if len_ == 4: str_[0] += ' billion'
        if str_[-3] != '':str_[-3] += ' million'
    if len_ >= 2 and slice_[-2] != '':
        str_[-2] += ' thousand'
    
    #remove whitespace
    str_ = list(filter(lambda x: x != '',str_))
    
    #DEBUG
    if DEBUG == True:
        print(slice_)
        print(str_)
        print(" ".join(str_))
        
    return " ".join(str_)

def test():
    assert num_to_word(42641323862) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"
    assert num_to_word(0) == "zero"
    assert num_to_word(111) == "one hundred eleven"
    assert num_to_word(1000) == "one thousand"
    assert num_to_word(100) == "one hundred"
    assert num_to_word(123456789012) == "one hundred twenty-three billion four hundred fifty-six million seven hundred eighty-nine thousand twelve"
    assert num_to_word(999999999999) == "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine"

    print("- < -")

def random_():
    import random
    for j in range(10000):
        i = random.randint(0,999999999999)
        try:
            assert num_to_word2(i) == num_to_word(i)
        except:
            print(i)
            print("Expect :",num_to_word(i))
            print("Got___  :",num_to_word2(i))
            return 0
    print("; o ;")

if __name__ == "__main__":
    random_()