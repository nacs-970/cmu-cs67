#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# HW13_2
# 204111 Sec 002

def count_vote(pref_matrix:list[list[str]]) -> list[tuple[str, int]]:

    d = {}
    for i in range(len(pref_matrix)):
        for j in range(len(pref_matrix[i])):
            name = pref_matrix[i][j]
            d[name] = d.get(name,0) + (len(pref_matrix[i]) - j)

    ans = sorted(map(lambda x,y: (x,y),d,list(d.values())))
    ans = sorted(ans, key = lambda x: x[1], reverse = True)
    return ans

if __name__ == "__main__":
    count_vote([['Mewtwo', 'Pikachu', 'Suicune'],['Mewtwo', 'Suicune', 'Pikachu'],['Pikachu', 'Rayquaza', 'Charizard'],['Suicune', 'Pikachu', 'Charizard']]) == [('Pikachu', 8),('Mewtwo', 6),('Suicune', 6),('Charizard', 2),('Rayquaza', 2)]
    print(count_vote([['ab','ax'],['aa','c']]))
