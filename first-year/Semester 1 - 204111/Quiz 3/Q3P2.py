def lucky_number(list_num):
    if len(list_num) == 1:
        return list_num[0]

    a = list_num[:len(list_num)//2] 
    b = list_num[len(list_num)//2:] 
    a,b = lucky_number(a),lucky_number(b)

    if len(list_num) == 2:
        if sum(list_num)%2 == 1:
            return min(list_num)
        else:
            return max(list_num)
    
    return lucky_number([a,b])

if __name__ == "__main__":
    print(lucky_number([1,2,3,3]))

