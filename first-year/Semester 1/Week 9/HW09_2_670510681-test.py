#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_2
# 204111 Sec 002
def median_of_median(list_a: list[float]) -> float:

    def median(list_):
        len_ = len(list_)
        mid = len_//2
        if len_%2 == 1: return list_[mid]
        return (list_[mid] + list_[mid-1])/2

    if len(list_a) == 3: 
        min_ = min(list_a)
        max_ = max(list_a)
        mid_ = sum(list_a)-min_-max_
        return float(median([min_,mid_,max_]))

    if len(list_a) <= 2:
        return float(median(list_a))

    step = len(list_a)//3
    step_a,step_b = step,2*step
    
    list_1 = list_a[:step_a]
    list_2 = list_a[step_a:step_b]
    list_3 = list_a[step_b:] # remainder will got median

    list_1 = median_of_median(list_1)
    list_2 = median_of_median(list_2)
    list_3 = median_of_median(list_3)

    return median_of_median([list_1,list_2,list_3]) # find median

def median_of_median2(list_a: list[float]) ->float :  
 
    x_1 = list_a[: (len(list_a))//3]
    x_2 = list_a[len(list_a)//3 : (len(list_a)//3)*2  ]
    x_3 = list_a[len(list_a)//3*2:]  
    last = ([x_1] + [x_2] + [x_3]) 
    new_list_a = list(map(lambda x : x if len(x) > 1 else sum(x + [0]) ,last )) 
 
 
 
    if len(list_a) >= 6 :
        return (recur_long(new_list_a))
 
    else :
        return (min_recur(new_list_a))
 
 
 
 
def min_recur(new_list_a) :  
    list_result = list(map(lambda x : check_list(x) ,new_list_a   )) 
    return float(find_mean(list_result))
 
def recur_long(new_list_a) :  
 
 
    # print(new_list_a) 
    list_last_check = list(map(lambda x : x if '[' not in str(x) else 'return again' ,new_list_a ))
 
    if 'return again' not in list_last_check  :  
 
        return float(find_mean(new_list_a) )
 
    else :  
 
 
        list_check_num = list(map(lambda x : x if '[' not in str(x) or  len(x) <= 3 else sep(x) ,new_list_a  ))  
 
        #print(list_check_num)
 
 
 
        def recur_check(list_check_num ,n=0, list_result = []) :  
            if n == 3 : 
                return(list_result) 
            else : 
                list_result_new = list(map(lambda x: check_list(x)  ,list_check_num[n]))
 
                return(recur_check(list_check_num, n + 1, list_result + [list_result_new]))
 
 
        list_check_num_2 = recur_check(list_check_num ,n=0, list_result = []) 
 
        #print(list_check_num_2)
 
 
        new_list_check = list(map(lambda x : check_list(x) if '[' not in str(x) or len(x) < 6   else x  ,list_check_num_2)) 
 
 
 
        double_check = list(map(lambda x : 'Fuka' if '[' in str(x)  else 'Murasaki' ,new_list_check   ))
 
        if double_check == 'Murasaki' : 
            list_a = (list(map(lambda x : find_mean(x)  ,new_list_check ))) 
            return(recur_long(list_a)) 
 
        else : 
            return(recur_long(new_list_check) ) 
 
 
def sep(list_x): #ใช้ในการแยก list เป็น 3 ส่วน
    x_1 = list_x[:(len(list_x))//3]
    x_2 = list_x[len(list_x)//3 : ( len(list_x)//3)*2  ]
    x_3 = list_x[len(list_x)//3*2:] 
    last = ([x_1] + [x_2] + [x_3]) 
    return (list(map(lambda x : x if len(x) > 1 else sum(x + [0]) ,last   )))
 
def find_mean(list_x): #ใช้หาค่ากลาง
    #print(list_x)
    #print(type(list_x.count(max(list_x))))
    if list_x[0] == list_x[1] == list_x[2] : 
        list_mean = [list_x[0]] 
 
    elif list_x.count(max(list_x)) > 1 :
        list_mean = [max(list_x) ]
    elif list_x.count(min(list_x)) > 1 : 
        list_mean = [min(list_x)]
 
    else :
        list_mean = list(filter(lambda x : x < max(list_x) and x > min(list_x)     ,list_x))
 
    return(list_mean[0]) 
 
def check_list(x) : #ใช้แปลงรูปก่อนหาค่ากลาง
    if '[' not in str(x) : 
        return(x) 
    elif len(x) == 2 : 
        return( (sum(x)/2 ))
    else : 
        return (find_mean(x) ) 



def test():
    import random
    for i in range(1000):
        l = []
        for j in range(random.randint(1,20)):
            l += [random.randint(1,100)]
        try:
            assert(median_of_median2(l)) == median_of_median(l)
        except:
            print(l)
            print('expect :',median_of_median(l))
            print('got :',median_of_median2(l))
            return 0
    print('--')




if __name__ == '__main__':
    #assert(median_of_median([59, 78, 29, 13, 22, 60, 12, 68, 77, 53, 3, 68, 43])) == 53
    test()
