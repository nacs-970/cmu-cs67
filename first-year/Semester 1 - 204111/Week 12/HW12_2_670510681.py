#!/usr/bin/env python3
# Atithep Thepkij (Tun) 
# 670510681
# HW12_2
# 204111 Sec 002

import sys

def main():
    treasures = read_input()
    total_value('Gold', treasures)

    assert total_value('Gold', treasures) == 1090
    assert total_value('Platinum', treasures) == 42000
    assert total_value('Ruby', treasures) == -1

def read_input():
    treasures = {}

    for line in sys.stdin:

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

if __name__ == '__main__':
    main()
