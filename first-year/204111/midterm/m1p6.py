def  adjacent_sum(list_a: list[int]) -> list[int]:
    return list(map(lambda x,y: x+y,list_a[1:],list_a[:-1]))