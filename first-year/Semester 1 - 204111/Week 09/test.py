
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

def unmask_id_2(masked_id: str) :  
    masked_id_none_that = masked_id.replace("-", '')

    star_point = masked_id.count('*')  

    list_num = list(map(lambda x : str(x).zfill(star_point) ,((range(1,10**star_point)))   ))  

    list_replace = list(map(lambda x : adap_patterned_message(x, masked_id) ,list_num    )) 

    list_check = list(map(lambda x : x.replace("-", '')   ,list_replace )) 

    list_last = list(filter(lambda x : Check_digit(change_to_list(x))   ,list_check )) 

    last_result = list(map(lambda x : str(x)[0] + '-' + str(x)[1:5] + '-' + str(x)[5:10] + '-' + str(x)[10:12] + '-' + str(x)[-1],list_last))

    return(last_result)


def change_to_list(x) : 
    new_list = list((str(x)).zfill(13)) 
    return(list(map(lambda x : int(x) ,new_list )))

def adap_patterned_message(message: str, pattern:str) -> None :   
    message = message.replace(' ', '')
    list_message = list(message) 

    range_message = list(range(0,len(list_message))) 

    count_star = pattern.count("*")  

    range_pattern = list(range(0,len(pattern)))

    list_position = list(map(lambda x : range_message[x] if x <= (len(range_message) - 1) else   range_message[x%len(range_message)] ,range(0, count_star)   )) 

    star_position = find_star_position(pattern, num = 0, list_st_po = [] ) #ตำแหน่งของ *

    
    return(replace_recur(pattern, star_position, count_star, list_position, message, num = 0))




def find_star_position(pattern, num = 0, list_st_po = [] ) : 
        if num == len(pattern)  : 
            return(list_st_po) 

        else : 
            if pattern[num] == '*' :  
                return(find_star_position(pattern, num + 1, list_st_po + [num]))
            else : 
                return(find_star_position(pattern, num + 1, list_st_po + [])) 

def replace_recur(pattern,  star_position, count_star, list_position, message, num = 0): 
        if num == count_star :
            return (pattern) 
        else : 



            st_po = (star_position[num])
            ls_po = str(message[list_position[num]])
            list_new_pattern = list(pattern)
            list_new_pattern.insert(st_po, ls_po) 
            del list_new_pattern[(st_po + 1)]

            new_patern = ''.join(list_new_pattern) 

            
            

            return (replace_recur(new_patern, star_position, count_star, list_position, message, num + 1))

def Check_digit(list_a) :    

    range_digit = list(range(1, 13))  
    list_a_for_check = list_a[:12]

    value = abs((sum(list(map(lambda n : list_a_for_check[(n - 1)] * (14 - n) , range_digit ))))%11 - 11) 

    if value == 10: 
        value = 0 

    elif value == 11 : 
        value = 1

    else : 
        value = value 

    if (value == list_a[-1]) and list_a[0] != 0 : 
        return(True) 

    else : 
        return(False) 

def test():
    import random
    for i in range(1000):
        table = '*012345678'
        str_ = ''
        for i in range(13):
            if i in [1,6,11,14]:
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
