#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW14_1
# 204111 Sec 002

def read_file(filename,mode="rt"):
    try:
        with open(filename,mode,encoding="utf-8") as input_:
            return input_.read()
    except FileNotFoundError:
        return None

def append_ranking(infile_name:str='score_in.txt', outfile_name: str='score_out.txt'):
    d = {}
    # making a rank
    with open (infile_name,"rt") as lines:
        for i in lines:
            text = i.split()
            score = list(map(lambda x: 0 if x == 'None' else x,text[1:]))
            score = list(map(float,score))
            d[text[0]] = sum(sorted(score,reverse=True)[:2])
    sort_ = sorted(d,key = lambda x: d[x],reverse=True);rank = 1
    for i in sort_:
        d[i] = rank
        rank += 1

    # write
    destination = outfile_name
    with open(destination, "wt") as outfile:
        with open (infile_name,"rt") as lines:
            for x in lines:
                l = x.split()
                tmp = f"{l[0]} {x[len(l[0]) + 1:-1]} {d.get(l[0],0)}\n"
                outfile.write(tmp)

if __name__ == "__main__":
    append_ranking("./HW14_1-score_in.txt")
    print(read_file("./score_out.txt"))
    print("---")
    append_ranking("./HW14_1-score_in-2.txt")
    print(read_file("./score_out.txt"))
