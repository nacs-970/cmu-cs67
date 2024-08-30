#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_3
# 204111 Sec 002

def unmask_id(masked_id:str) -> list[str]:
    
    def check_digit(list_):
        list_ = list_[:-1]
        num = list(filter(lambda x: x != '-',list_))
        #num = list(map(lambda x: int(num[x])*(13-x) if num[x] != '*' else 0,range(13)))
        num = list(map(lambda x: int(num[x])*(13-x),range(12)))
        last = (11 - sum(num)%11)%10
        return list_ + str(last)

    count_ = masked_id.count('*')
    #list_ = masked_id.replace('*','{}')
    range_ = list(map(lambda x: str(x).zfill(count_),range(10**count_)))

    def replace_(list_,num,index_=0): # replace with element of range_
        if index_ == len(num):return list_
        else: # 000 , 001 
            list_ = list_.replace('*',num[index_],1)
            return replace_(list_,num,index_+1)

    list_ = list(map(lambda x: replace_(masked_id,x,0), range_))
    list_ = list(filter(lambda x: x[0]!='0',list_)) # filter 0
    list_ = list(filter(lambda x: x == check_digit(x),list_))
    return list_

if __name__ == '__main__':
    print(unmask_id('1-2345-67890-12-4'))
    print(unmask_id('1-2345-67890-12-*'))
    print(unmask_id('*-2345-67890-1*-*'))
    print(unmask_id('1-2345-67890-1*-*'))
    print(unmask_id('1-2345-67890-**-*'))
    print(unmask_id('1-2345-6789*-**-*'))
    print(unmask_id('1-2345-67***-**-*'))
    print(unmask_id('1-2345-67*90-1*-*'))
    print(unmask_id('1-2345-6**90-1*-*'))
    print(unmask_id('1-2345-67**0-12-1'))
