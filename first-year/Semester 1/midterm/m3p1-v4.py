def find_mode(score_list:list[int]) -> list[int]:
    score_list,dupe_check = sorted(score_list),[] # min -> max
    
    #nodupe = list(map(lambda x: dupe_check.append(x) if x not in dupe_check else x ,score_list))
    #nodupe = list(filter(lambda x: x != None,nodupe))

    nodupe = list(filter(lambda x: not(x in dupe_check or dupe_check.append(x)),score_list)) # not(T/F or F) .append(x) default is False
    count_ = list(map(lambda x: score_list.count(x),nodupe))
    ans = list(filter(lambda x: score_list.count(x) == max(count_),nodupe))
    #ans = list(filter(lambda x: score_list.count(x) == max(list(map(lambda x: score_list.count(x),nodupe))), nodupe))
    return ans

#print(find_mode([50,50,60,60]))
#print(find_mode([50,60]))
#print(find_mode([50,60,60]))
