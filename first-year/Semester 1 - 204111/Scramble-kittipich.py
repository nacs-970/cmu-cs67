seed = ["c"]
for letter in 'at':
    tmp = set()
    for e in seed:
        tmp |= set(map(lambda x: e[:x] + letter + e[x:], range(len(e) + 1)))
    seed = tmp
print(seed)

def scramble(word):
    seed = [word[0]]
    for letter in word[1:]:
        tmp = set()
        for e in seed:
            tmp |= set(map(lambda x: e[:x] + letter + e[x:], range(len(e) + 1)))
        seed = tmp
    print(seed)
    return list(seed)
    
scramble("cat")