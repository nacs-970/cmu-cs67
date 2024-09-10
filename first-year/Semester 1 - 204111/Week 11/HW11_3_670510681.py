#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_3
# 204111 Sec 002

def runner_up() -> None:
    students = int(input("Total students: "))
    sum = 0
    max_,mid_,min_ = 0,None,None
    print("Enter score:")
    for i in range(students):
        #print(max_,mid_,min_)
        n = int(input())
        if n > max_: #and n != 0:
            min_ = mid_
            mid_ = max_
            max_ = n
        if n < max_ and n > mid_: 
            min_ = mid_
            mid_ = n
        if n < mid_ and n > min_:
            min_ = n
        sum += n
    print("---")

    #print(max_,mid_,min_)
    print(f"Max score is: {max_:.2f}")
    if mid_:
        print(f"Runner up is: {mid_:.2f}")
    else:
        print(f"Runner up is: None")

    print(f"Average is: {sum/students:.2f}")

if __name__ == "__main__":
    runner_up()

#8
#4
#5
#9
#6
#8
#9
