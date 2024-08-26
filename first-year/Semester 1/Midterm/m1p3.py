def count_lucky_num(start: int, stop: int) -> int:
    list_ = list(filter(lambda x: x%7 ==0 and '7' not in str(x),range(start,stop)))
    return len(list_)