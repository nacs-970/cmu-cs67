#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Lab07_2
# 204111 Sec 002

def square_frame(n:int,sep: str=' ') -> str: # str (n>=3) and don't use sep_ 

    space = (n-2)**2 # find a space in square
    range_ = list(range(1,((n**2)-space)+1))
    max_ = len(str(range_[-1]))
    range_ = list(map(lambda x: str(x).zfill(max_),range_))

    top = range_[:n]
    
    body =  range_[n:] # 05 -> 12
    index_ = list(range(n-2)) # 05(0) 06(1) 00 00 00 00 11(-2) 12(-1)
    body = list(map(lambda x: [body[-(x+1)]]+(n-2)*[max_*sep]+[body[x]],index_)) # 12(-1) 11(-2) max_*[sep_] 05(0) 06(1)

    bottom = range_[n:] # 05 -> 12
    bottom = bottom[n-2:-(n-2)][::-1]# reverse , cannot [n-2:-(n-2):-1] because will be ' '

    body_print = list(map(lambda x:sep.join(body[x]),range(len(body))))
    ans = sep.join(top)+'\n'+'\n'.join(body_print)+'\n'+sep.join(bottom)

    #print(ans)
    return ans

def square_frame_2(n: int, sep: str=' ') -> str:

    wight = (n*3)-1
    high = (n*2)-1
    
    
    front_middle = list(map(lambda x: ((n*4)-(x-1))-4,(list(range(1,n-1))) ))
    front_middle1 = str(list(map(lambda x: ((n*4)-(x-1))-4,(list(range(1,n-1))) ))).strip('[]').replace(',','').split(' ')
    result_frontmid = str(list(map(lambda x: x.zfill(len(str(max(front_middle)))) ,front_middle1))).strip('[]').replace(',','').replace('\'','').split(' ')
    
    up = str(list(range(1,n+1))).strip('[]').replace(',','').split(' ')
    result_up = str(list(map(lambda x: x.zfill(len(str(max(front_middle)))) ,up))).strip('[]').replace(',','').replace('\'','')
    
    bottom = str(list(range(high,wight))[::-1]).strip('[]').replace(',','').split(' ')
    result_bottom = str(list(map(lambda x: x.zfill(len(str(max(front_middle)))) ,bottom))).strip('[]').replace(',','').replace('\'','')
    
    back_middle = str(list(map(lambda x: n+x,(list(range(1,n-1))) ))).strip('[]').replace(',','').split(' ')
    result_backmid = str(list(map(lambda x: x.zfill(len(str(max(front_middle)))) ,back_middle))).strip('[]').replace(',','').replace('\'','').split(' ')
    
    middle = '\n'.join(list(map(lambda x,y: str(x)+' '*(len(result_up)-(len(str(max(front_middle)))+len(str(min(front_middle)))))+str(y),result_frontmid,result_backmid)))
    
    return((result_up+'\n' + middle+ '\n' + result_bottom).replace(' ',sep))


def test():
    import random
    import string
    for i in range(10000):
        sep = ""
        sep += random.choice(string.printable)
        try:
            assert square_frame_2(i+3,sep) == square_frame(i+3,sep)
        except:
            print(i+3,sep)
            print('got :\n',square_frame_2(i+3,sep))
            print('exp :\n',square_frame(i+3,sep))
            return 0
    print(";)")

if __name__ == "__main__":
    test()
    square_frame(4,'.')
    square_frame(3)
    square_frame(10)
    square_frame(20,'.')
