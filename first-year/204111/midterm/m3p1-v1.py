def find_mode(score_list:list[int]) -> list[int]:
    score_list = sorted(score_list) # min -> max
    range_ = range(len(score_list))
    score_list += ['x']
    nodupe = list(filter(lambda x: score_list[x] != score_list[x+1],range_))
    nodupe = list(map(lambda x: score_list[x],nodupe))
    
    index_ = range(len(nodupe))
    count_ = list(map(lambda x: score_list.count(x),nodupe))
    ans = list(map(lambda x: nodupe[x] if count_[x] == max(count_) else 'x',index_))
    ans = list(filter(lambda x: x != 'x',ans))
    return ans
