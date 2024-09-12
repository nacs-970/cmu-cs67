def average_time(list_num: list[float|None]) -> float:
    list_num = list(filter(lambda x: x != None,list_num))
    return sum(list_num)/len(list_num)

def running_streaks(list_num):
    avg = average_time(list_num)
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

if __name__ == "__main__":
    print(running_streaks([1,1,1,2,1,1,1]))
    print(running_streaks([1,1]))

