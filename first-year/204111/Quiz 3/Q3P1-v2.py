def average_time(list_num: list[float|None]) -> float:
    list_num = list(filter(lambda x: x != None,list_num))
    return sum(list_num)/len(list_num)

def running_streaks(list_num):
    avg = average_time(list_num)
    count_,list_ = 0,[]

    for i in list_num:
        if i == None or i >= avg:
            list_.append(count_)
            count_ = 0
            continue
        else:
            count_ +=1

    list_.append(count_)
    list_ = list(filter(lambda x: x != 0,list_))
    list_ = list(filter(lambda x: x == max(list_),list_))
    return list_

if __name__ == "__main__":
    print(running_streaks([1,1,1,2,1,1,1]))
    print(running_streaks([1,1]))

