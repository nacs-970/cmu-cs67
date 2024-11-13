import sys
DEBUG=True

import random

def main():
    l= [['Marineford', 'Platinum', 42000], ['Marineford', 'Diamond', 300], ['Enies Lobby', 'Bronze', 43000], ['Elbaf', 'Silver', 9600], ['Dressrosa', 'Gold', 190],  ['Punk Hazard', 'Gold', 900],['A','Gold']]
    treasures = read_input(l)
    total_value('Gold', treasures)
    #assert total_value('Gold', treasures) == 1090
    #assert total_value('Ruby', treasures) == -1
    #assert total_value('Bronze', treasures) == 45000
    #assert total_value('Labubu', treasures) == -1
    #assert total_value('Silver',treasures)==9600
    
    print('all ok')

def read_input(l):
    treasures = {}
    for line in l:

        if '#' in line:
            continue
        line=line.split(',')
        line=list(map(lambda x: x.strip(),line))
        value=int(''.join(list(filter(lambda x:x.isdigit(),line[2]))))
        
        if line[1] in treasures:
            if DEBUG: print('in this')
            old_value=treasures.get(line[1])
            if DEBUG: print(old_value[0])
            new_value=[old_value[0],(line[0],value)]
            treasures[line[1]]=new_value
        else:
            if DEBUG: print(value)
            treasures[line[1]]=[(line[0],value)]
            if DEBUG: print(line[1])

    if DEBUG: print(type(value))
    if DEBUG: print(treasures)
    print(treasures)
    return treasures

def total_value(treasure_type, treasures):
    total = 0
    if DEBUG: print(treasure_type)
    if DEBUG: print(treasures)
    
    if treasure_type in treasures:
        value=treasures.get(treasure_type)
        for list_ in value:
            if DEBUG:print(list_)
            total+=list_[-1]
            if DEBUG: print(total)
    else:
        total=-1
    #print(total)
    return total
    
def main():
    treasures = read_input()
    total_value('Gold', treasures)

    assert total_value('Gold', treasures) == 1090
    assert total_value('Platinum', treasures) == 42000
    assert total_value('Ruby', treasures) == -1

def read_input(l):
    treasures = {}

    for line in l:

        if line[0] == "#": continue
        line = line.split(",")
        line = list(map(str.strip,line))

        place = line[0]; value = int(line[2])

        if line[1] not in treasures: treasures[line[1]] = []
        treasures[line[1]] += [tuple([place,value])]

        #print(line)

    #print(treasures)
    return treasures


def total_value(treasure_type, treasures):
    total = 0

    if treasure_type not in treasures:
        return -1

    for n in treasures[treasure_type]:
        #print(n)
        total += n[1]
    
    return total
def test()
if __name__ == '__main__':
    main()