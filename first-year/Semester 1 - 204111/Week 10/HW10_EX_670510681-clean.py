#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_EX
# 204111 Sec 002

cat_l = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|'''
cat_r = \
    '''| ／|、    
|(°、。7   
| |、 ~ヽ  
| ᒐᒐ_f_ )ノ
|__________'''

cat_m = \
    ''' ／|、     
(°、。7    
 |、 ~ヽ   
 ᒐᒐ_f_ )ノ 
__________ '''

cat_m = list(cat_m.split("\n"))
cat_l = list(cat_l.split("\n"))
cat_r = list(cat_r.split("\n"))

def cat_altar(n):

    top_ = list(map(lambda x: (n-1) * "           " + x,cat_m))
    mid_ = []

    for i in range(1,n):
        mid_.append(list(map(lambda x,y: (n-1-i)*"           " + x + (i+(i-1))*"          "+(i+i-2)*" "+ y,cat_l,cat_r)))

    for  i in mid_:
        top_.append("\n".join(i))

    return "\n".join(top_)

if __name__ == '__main__':
    print(cat_altar(1))
    print(cat_altar(2))
    print(cat_altar(3))
    print(cat_altar(4))
    print(cat_altar(5))
