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

#cat_m = ' ／|、     \n(°、。7    \n |、 ~ヽ   \n ᒐᒐ_f_ )ノ \n__________ \n'
#blank = ' '

def main():
    cat_altar(3)
    #print(cat_altar(int(input())))

#space = '''a
#a'''
#star = '''#
##'''
#space = space.split("\n")
#star = star.split("\n")
#print(type(cat_m))
cat_m = list(cat_m.split("\n"))
cat_l = list(cat_l.split("\n"))
cat_r = list(cat_r.split("\n"))
def cat_altar(n):

    top_ = list(map(lambda x: (n-1) * "           " + x,cat_m))
    mid_ = []

    #bot_ = []

    #len_ = range(1,len(cat_l))

    for i in range(1,n):
        mid_.append(list(map(lambda x,y: (n-1-i)*"           " + x + (i+(i-1))*"          "+(i+i-2)*" "+ y,cat_l,cat_r)))

    #for i in range(1,n):

        #print(" "*(n-i-1),end="") 
        #print("*"*(2*i+1),end="")
        #print(" "*(n-i-1),end="") 
        #print()
    #return "\n".join(mid_)
    for  i in mid_:
        top_.append("\n".join(i))

    #return mid_
    return "\n".join(top_)


    #for i in range(n):
    #    for j in range(n-1):
    #        space_ = " "
    #        print(j*10*space_,end="")
    #    for j in range(n)

    #return cat_m*n


if __name__ == '__main__':
    #print(cat_l,end="")
    #print(cat_r,end="")
    #print(cat_m,end="")
    #print("".join([blank,cat_m,blank]))
    #print(f"{blank}{cat_m}{blank}")
    #print(space.split("\n"))
    print(cat_altar(2))
    print(cat_altar(3))
    print(cat_altar(4))
    print(cat_altar(5))
    #main()A
