def average(list_num):
    list_num = list(filter(lambda x: x != None,list_num))
    return sum(list_num)/len(list_num)

def running_streaks(list_num):
    avg = average(list_num)
    count_,list_ = 0,[]
    for i in list_num:
        if i == None or i > avg:
            list_.append(count_)
            count_ = 0
            continue
        if i < avg:
            count_ +=1

    list_.append(count_)
    list_ = list(filter(lambda x: x != 0,list_))
    list_ = list(filter(lambda x: x == max(list_),list_))
    return list_

def running_streaks2(list_num):
    avg = average(list_num)
    count_,streaks = 0,[]

    def streaks_check(list_,count_=0):
        if len(list_) < 1:
            streaks.append(count_)
            return

        if list_[0] == None or list_[0] > avg:
            streaks.append(count_)
            count_ = 0

        elif list_[0] < avg:
            count_ += 1

        streaks_check(list_[1:],count_)

    streaks_check(list_num)
    streaks = list(filter(lambda x: x != 0,streaks))
    return streaks

import random
def test():
    for _ in range(100000):
        n = []
        for i in range(random.randint(1,100)):
            ch = [None,random.randint(0,100)]
            n.append(random.choice(ch))
        try:
            assert running_streaks2(n) == running_streaks(n)
        except:
            print(n)
            print(running_streaks(n))
            print(running_streaks2(n))
        return 0
    print(": w :")

if __name__ == "__main__":
    test()
    #print(running_streaks([1,1,1,2,1,1,1]))
    #print(running_streaks([1,1]))

