#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_3
# 204111 Sec 002

def unmask_id(masked_id:str) -> list[str]:
#    mask_id = masked_id

    def check_digit(list_):
        list_ = list_[:-1]
        num = list(filter(lambda x: x != '-',list_))
        #num = list(map(lambda x: int(num[x])*(13-x) if num[x] != '*' else 0,range(13)))
        num = list(map(lambda x: int(num[x])*(13-x),range(12)))
        last = (11 - sum(num)%11)%10
        return list_ + str(last)

    count_ = masked_id.count('*')
    list_ = masked_id.replace('*','{}')
    range_ = list(map(lambda x: str(x).zfill(count_),range(10**count_)))
    list_ = list(map(lambda x: list_.format(*x),range_)) # * is unpack; ex '00' -> 0,0
    list_ = list(filter(lambda x: x[0]!='0',list_)) # filter 0
    print(list_)
    list_ = list(filter(lambda x: x == check_digit(x),list_))
    return list_

    #no_star = []
    #def replace_():
    #    if count_ == 0:return no_star


    #no_star = list(map(lambda x: masked_id.replace('*',str(x),1), range(10**count_)))  
    #no_star = list(map(lambda x: masked_id.replace('*',str(x),1),range(10)))
    #return no_star
    #def repalce_star(list_,index_):
    #    if index_ == len(list_):return [list_]
    #list_ = list(map(lambda x: x,range_))
    #list_ = list(map(lambda x: x,range_))
    #list_ = list(map(lambda x: x,range_))
    #list_ = list(map(lambda x: x,range_))
    #    if list_[index_] == '*':
    #        a = []
    #        def replace_star_2(n=0):
    #            if n == 10:return a
    #            res = list_[:index_] + str(n) + list_[index_+1:]
    #            a.extend(repalce_star(res,index_+1))
    #        replace_star_2()
    #        return a
    #    else:
    #        repalce_star(list_,index_+1)
    #return repalce_star(masked_id,0)

##
    #def repalce_star(list_):
    #    if '*' not in list_[:-1]:
    #        id_mask.append(list_)
    #        return 

    #    if '*' in list_[:-1]: 
    #        list_ = list(map(lambda x: list_.replace('*',str(x),1),range(10)))

    #    if '*' in list_ [0][:-1]:
    #        return repalce_star(list_)
    #        
    #return repalce_star(masked_id)

    #def repalce_star(list_,n=0):
    #    print(list_)
    #    if n > 9 and '*' not in list_[:-1]:return list_
    #    if '*' not in list_[:-1]:return list_
    #    if n > 9:n = 0

    #    if '*' in list_: 
    #        return [list_[:-1].replace('*',str(n),1)] + repalce_star(list_,n+1)
    #return repalce_star(masked_id)

            #return repalce_star(umask)

    #return masked_id[:-1] + str(check_digit(masked_id))


if __name__ == '__main__':
    print(unmask_id('1-2345-67890-12-*'))
    #print(unmask_id('1-2345-67890-12-*'))
    #print(unmask_id('*-2345-67890-12-*'))
    #print(unmask_id('1-2345-67890-1*-*'))
    #print(unmask_id('1-2345-67890-**-*'))
    #print(unmask_id('1-2345-6789*-**-*'))
    #print(unmask_id('1-2345-67***-**-*'))
    #print(unmask_id('1-2345-67*90-1*-*'))
    #print(unmask_id('1-2345-6**90-1*-*'))
    #print(unmask_id('1-2345-67**0-12-1'))
