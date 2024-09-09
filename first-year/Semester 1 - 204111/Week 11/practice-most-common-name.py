def most_common_name(names):
    max_c = 0;max_v = None
    d = {}
    for i in names:
        c = 1 + d.get(i,0)
        d[i] = c
        if c > max_c:
            max_c,max_v = c,i
    d = dict(filter(lambda x: x[1] == max_c,d.items()))
    if len(d) > 1:
        d = set(map(lambda x: x[0],d.items()))
        return d
    return max_v
print(most_common_name(["Jane","Aaron","Cindy","Aaron"]))
print(most_common_name(["Jane","Aaron","Jane","Aaron"]))

