def most_popular_friend(name_dict):
    intersec = set()
    for _,names in d.items():
        if not intersec:
            intersec |= names # union + update
        intersec &= names # intersec + update
    intersec = list(map(str,intersec))
    return intersec[0]

d = dict()
d["fred"] = {"wilma","betty","barnaey"}
d["wilma"] = {"fred","betty","dino"}

print(most_popular_friend(d))
