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

def find_mean(contents):
    lines = contents.splitlines()
    total = len(lines)
    rank = []
    d = dict()
    for i in range(total):
        line = [x.strip() for x in lines[i].split()]
        unmod_scores = line[1:]
        score = list(map(lambda x: 0 if x == 'None' else x,line[1:]))
        score = list(map(float,score))
        d[line[0]] = sum(sorted(score,reverse=True)[:2]),unmod_scores
    return d

def append_ranking(infile_name:str='score_in.txt', outfile_name: str='score_out.txt'):
    d = find_mean(read_file(infile_name))
    #print(d["6xxx10113"][1])

    sort_ = sorted(d,key = lambda x: d[x][0],reverse=True)
    rank = 1; buff = []
    for i in sort_:
        #tmp = [i," ".join(map(str,d[i][1])),str(rank) + "\n"]
        #tmp = "{} {:5} {:5} {:5} {}\n".format(i,*d[i][1],rank)
        tmp = [i,d[i][1],str(rank) + "\n"]
        buff += [tmp]
        rank += 1
    buff = sorted(buff,key = lambda x: x[0])

    destination = outfile_name
    with open(destination, "wt") as outfile:
        for line in buff:
            tmp = "{} {} {} {} {}".format(line[0],*line[1],line[2])
            outfile.write(tmp)

if __name__ == "__main__":
    append_ranking("./HW14_1-score_in.txt")
    print(read_file("./score_out.txt"))
    print("---")
    append_ranking("./HW14_1-score_in-2.txt")
    print(read_file("./score_out.txt"))
