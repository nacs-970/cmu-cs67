#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_1
# 204111 Sec 002

def words_to_num(words:str) -> int:
    unit_list = { "zero":0,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10,
                 "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, 
                 "eighteen":18, "nineteen":19, "twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
    
    # split
    billion,million,thousand,hundred = "zero","zero","zero","zero"

    if 'billion' in words:
        billion,words = words.split('billion')
    if 'million' in words:
        million,words = words.split('million')
    if 'thousand' in words:
        thousand,words = words.rsplit('thousand',1)

    hundred = words.strip()
    
    billion = billion.strip()
    million = million.strip()
    thousand = thousand.strip()
    hundred = hundred.strip()

    def convertion(txt):
        num,txt = 0,txt.split()

        while txt:
            #print(txt[0])
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

if __name__ == "__main__":
    assert words_to_num("zero") == 0
    assert words_to_num("ten") == 10
    assert words_to_num("fourteen") == 14
    assert words_to_num("one thousand") == 1000
    assert words_to_num("two hundred forty-eight") == 248
    assert words_to_num("one hundred eleven") == 111
    assert words_to_num("forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two") == 42641323862
    assert words_to_num("one hundred twenty-three billion four hundred fifty-six million seven hundred eighty-nine thousand twelve") == 123456789012
    assert words_to_num("nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine") == 999999999999
    #print(words_to_num("fourteen"))
    #print(words_to_num("two hundred forty-eight"))
    #print(words_to_num("one hundred eleven"))
    #print(words_to_num("forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"))
    print(words_to_num("seven hundred forty-one billion seven hundred thirty-one million five hundred forty-four"))
    print(words_to_num("one billion"))
