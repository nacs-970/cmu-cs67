print(" - nestedloop helper - ")
def nestedloop_helper(col):
    for j in range(1,col+1):
        print("j = %d " % j, end="")

def nestedloop():
    row,col = 5,4
    for i in range(1,row+1):
        print("\ni is now %d" % i)
        nestedloop_helper(col)

nestedloop()
print()
print()
