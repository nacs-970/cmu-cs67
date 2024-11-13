#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_2
# 204111 Sec 002

def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str]) -> list[str]:
    first_id,second_id = "",""
    #posibility = []
    #sequence_count = len(l_lane) + len(r_lane)
    list_ = []

    def posibility_(first,second,sequence=""):
        #if not(first[:1] or second[:1]):
        if first == [] and second == []:
            #list_.append(sequence[:-1])
            #if sequence[:-1] not in list_:
            list_.append(sequence[:-1])

        #if not(first[:1]):
        #    first = second

        #if not(second[:1]):
        #    second = first
        
        if first[:1]:
            #print(first[:1],second[:1])
            first_id = first[0] + ">"
            #first_id = first[0]
            #sequence = sequence + first[0] + ">"
            #sequence = sequence + first[0] + ">"
            #first = first[1:]
            #print(sequence)
            #posibility_(first,second,sequence) 
            #posibility_(first[1:],second,sequence)
                        # first[1:] here to make it not mutable and "sequence + first_id" as the same reason
            posibility_(first[1:],second,sequence + first_id) 

        if second[:1]:
            #print(first[:1],second[:1])
            second_id = second[0] + ">"
            #second_id = second[0]
            #sequence = sequence + second[0] + ">"
            #second = second[1:]
            #print(second)
            #posibility_(first,second,sequence)
            #posibility_(first,second[1:],sequence)
            posibility_(first,second[1:],sequence + second_id)
        #return list_
        
        #if first[:1]:
        #    first_id = first[:1][0]
        #    first = first[1:]
        #    sequence += first_id+">"
        #    posibility_(first,second,sequence) 

        #if not(first[:1]):
        #    rest = ">".join(second)
        #    sequence += rest

        #    if sequence not in list_:
        #        list_.append(sequence)

        #    return list_
        #    #return rest


        #if second[:1]: 
        #    second_id = second[:1][0]
        #    second = second[1:]
        #    sequence += second_id+">"
        #    posibility_(first,second,sequence) 
        
        #return list_ + ['>'.join(first+second)]


        #if first[:1]:
        #    first_id = first[:1][0]
        #    first = first[1:]

        #if second[:1]:
        #    second_id = second[:1][0]
        #    second = second[1:]

        #if first_id not in sequence:
        #    sequence += first_id+">"
        #    posibility_(first,second,sequence) 

        #if second_id not in sequence:
        #    sequence += second_id+">"
        #    posibility_(first,second,sequence) 

        #return list_


            #print("first",first[1:],second,sequence)

        #if second[:1]: 
        #    second_id = second[:1][0]
        #    second = second[1:]

        #    if second_id not in sequence:
        #        sequence += second_id+">"
        #        posibility_(first,second,sequence) 
        #    #print("second",first,second[1:],sequence)

        #return list_

        #if second[:1]:
        #    if not(first[:1]): 
        #        first_id = second[:1][0]
        #        sequence += first_id+">"
        #        posibility_([],second[1:],sequence)
        #    else:
        #        second_id = second[:1][0]
        #        sequence += second_id+">"
        #        posibility_(first,second[1:],sequence)

        #if not(first[:1]):
        #    first_id = second_id
        #    first = second[:1]
        #    second = second[1:]

        #sequence += first_id + ">"
        #return posibility_(first[1:],second,sequefront + back

    #f_end = '>'.join(l_lane+r_lane)
    #b_end = '>'.join(r_lane+l_lane)
    
    l_lane , r_lane = list(l_lane), list(r_lane)
    #front = posibility_(l_lane,r_lane)
    posibility_(l_lane,r_lane)
    return list_

    list_ = []
    back = posibility_(r_lane,l_lane)

    #if len(front) != 1 and f_end not in front:
    #    front += [f_end]

    #if len(back) != 1 and b_end not in back:
    #    back += [b_end]

    list_ = front + back

    #range_ = range(len(list_))
    #list_ += ["x"]
    #list_ = list(map(lambda x: list_[x] if list_[x] != list_[x+1] else "", range_))
    #list_ = list(filter(lambda x: x != "",list_))

    return list_
    #return posibility_(r_lane,l_lane,"")

if __name__ == "__main__":
    #l = 'R2','R4'
    #r = 'O34','O22'
    l = 'A','B'
    r = '1','2'
    #l_end = '>'.join(l+r)
    #r_end = '>'.join(r+l)
    print(arrival_sequences(l,r))
    #print(arrival_sequences(r,l))
    #print(l_end,r_end)
