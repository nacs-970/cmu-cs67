def find_mode(score_list:list[int]) -> list[int]:
    score_list = sorted(score_list) # min -> max
    range_ = range(len(score_list))
    score_list += ['x']
    nodupe = list(filter(lambda x: score_list[x] != score_list[x+1],range_))
    nodupe = list(map(lambda x: score_list[x],nodupe))
    
    index_ = range(len(nodupe))
    count_ = list(map(lambda x: score_list.count(x),nodupe))
    ans = list(filter(lambda x: score_list.count(x) == max(count_), nodupe))
    return ans

#print(find_mode([50,50,60,60]))
#print(find_mode([50,60]))
#print(find_mode([50,60,60]))

