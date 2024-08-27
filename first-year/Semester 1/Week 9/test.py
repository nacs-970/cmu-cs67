
def unmask_id(masked_id:str) -> list[str]:
    mask_id = masked_id

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
    list_ = list(map(lambda x: list_.format(*x),range_)) # * is unpack
    list_ = list(filter(lambda x: x[0]!='0',list_)) # filter 0
    list_ = list(filter(lambda x: x == check_digit(x),list_))
    return list_

def unmask_id_2(masked_id:str) -> list[str]:
#    mask_id = masked_id
    
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

    def replace_(list_,str_,index_=0):
        if index_ == len(str_):return list_
        else:
            list_ = list_.replace('*',str_[index_],1)
            return replace_(list_,str_,index_+1)

    list_ = list(map(lambda x: replace_(masked_id,x,0), range_))
    list_ = list(filter(lambda x: x[0]!='0',list_)) # filter 0
    list_ = list(filter(lambda x: x == check_digit(x),list_))
    return list_

def test():
    import random
    for i in range(1000):
        table = '*012345678'
        str_ = ''
        for i in range(13):
            if i in [1,6,12,15]:
                str_ += '-'
            str_ += random.choice(table)
        try:
            assert unmask_id_2(str_) == unmask_id(str_)
        except:
            print(str_)
            print(f'excpet :{unmask_id(str_)}') 
            print(f'got :{unmask_id_2(str_)}')
            return 0
    print('nah i\'d win')

if __name__ == '__main__':
    test()
