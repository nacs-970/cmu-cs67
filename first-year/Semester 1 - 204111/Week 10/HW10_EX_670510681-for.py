#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_EX
# 204111 Sec 002

cat = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|'''

cat = cat.splitlines()
cat = list(map(lambda x: x[:-1],cat))

#cat_1 = ' ／|、    '
#cat_2 = '(°、。7   '
#cat_3 = ' |、 ~ヽ  '
#cat_4 = ' ᒐᒐ_f_ )ノ'
#cat_5 = '__________'
#cat = [cat_1,cat_2,cat_3,cat_4,cat_5]

def cat_altar(n):
    tmp = list(map(lambda x: ' '*(n-1)*11 + x ,cat))
    l = ['\n'.join(tmp)]
    if n == 1:return ''.join(l)
    for i in range(1,n):
        #print(" "*(n-i),end="") 
        #print(("*")*(2*i + 1))
        space_ = ' '*(n-1-i)*11
        space2_ = ' '*(2*i - 1)*10
        cat_l = list(map(lambda x: space_ + x+'|' + space2_ + " "*(i+i-2)+ '|' +x,cat))
        l.append("\n".join(cat_l))
    return "\n".join(l)


if __name__ == '__main__':
    print(cat_altar(1))
    print(cat_altar(2))
    print(cat_altar(3))
    print(cat_altar(4))
    print(cat_altar(5))
