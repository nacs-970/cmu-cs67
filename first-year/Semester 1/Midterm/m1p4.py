from functools import reduce
def find_min(list_a:list[int]) -> int:
    return reduce(lambda x,y: x if x < y else y, list_a)
