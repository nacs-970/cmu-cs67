def word_count(txt):
    txt = list(filter(lambda x: x.isalpha() or x.isspace() or x.isdigit(),txt))
    txt = "".join(txt).lower().split()
    d,c = {},0
    for w in txt:
        c = 1 + d.get(w,0)
        d[w] = c
    return d
print(word_count("This jacket costs $5 MORE than that jacket, REALLY?"))
