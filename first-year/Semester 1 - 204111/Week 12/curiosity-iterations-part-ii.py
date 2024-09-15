print("- nested_loop -")
def nested_loop():
    rows = 5
    cols = 4

    for i in range(1,rows+1):
        print("\ni is now %d" % i)
        for j in range(1,cols+1):
            print("j = %d " % j, end="")

nested_loop()
print()

print()
print("- number pyramid -")
size = 5
for i in range(size):
    for j in range(i+1):
        print(j+1, end = "")
    print()

print()
print("- number pyramid upsidedown -")
size = 5
for i in range(size):
    for j in range(size - i):
        print(j+1, end = "")
        #print(size - j, end = "")
    print()

print()
print("- space syemetric pyramid -")
size = 5
for i in range(size):
    for j in range(size - i):
        print(" ", end = "")
    for k in range(i+1):
        print("* ",end="")
        #print(size - j, end = "")
    print()

print()
print("- selection within a loop -")
def count_pos_neg(x=[3,-2,8,-5,1]):
    input_ = False
    MAXNUM = 5
    pos_total,neg_total = 0,0
    for i in range(5):

        if input_:
            n = float(input(""))
        else:
            n = x[i]

        if n > 0:
            pos_total += n
        if n < 0:
            neg_total += n
    print("Positive Total :", pos_total)
    print("Negative Total :", neg_total)
count_pos_neg()

print()
print("- input data validation -")
def verify_month_ipput(x=12):

    break_ = True
    input_ = False

    while True:
        if input_:
            month = int(input("Enter a month (1 -12) :"))
        else:
            month = x
            print(month)
        if 1 <= month <= 12:
            print("correct")
            return month
        else:
            print("Error - invalid month.")
            if break_:
                break

verify_month_ipput()

print()
print("- interactive loop control -")
def display_square_and_cube(n=5):
    input_ = False
    final = n

    if input_:
        final = int(input("Enter the final number :"))

    print("Number Square Cube")
    print("------------------")

    for num in range(1,final+1):
        print("%3d %7d %6d" % (num, num**2, num**3))
display_square_and_cube()

print()
print("- evaluationg equations -")
def equation1(start,end):
    print("x value y value")
    print("------- ------- ")
    x = start
    while x <= end:
        y = 10 * (x ** 2) + 3 * x -2
        print("%4.2f %10.2f" % (x,y))
        x += 0.5
equation1(4,6)

print()
print("- scramble -")
def scramble(str_):

    def permuation(remain,str_="",):

        #print(str_)

        if len(remain) == 0 and str_ not in ans:
            ans.append(str_)

        else:
            for i in range(len(remain)):
                # 1 / 0
                # 0 permuation( "" + "23" , "" + 1)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # 2 / 1
                # 0 permuation( "1" + "2" , from 1/0 + 2)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # .. n
                permuation(remain[:i] + remain[i+1:],str_ + remain[i])

    ans = []
    permuation(str_)

    print(ans)
    return ans

scramble("123")

print()
print("- scramble 2 -")
def scramble(str_):

    def permuation(remain,str_=[],ans=[]):

        print(str_)

        if not remain and str_ not in ans:
            ans.append("".join(str_))
            #ans.append(str_)

        if remain:
            #permuation(remain[:i] + remain[i+1:],str_ + remain[i])
            permuation(remain[1:],str_ + [remain[0]])
            permuation(remain[:-1],[remain[-1]] + str_)
            permuation(remain[1:],[remain[0]] + str_)
            permuation(remain[:-1],str_ + [remain[-1]])
            #permuation(remain[:-1],str_ + remain[0])
            #permuation(remain[:-1],str_)

        return ans

    str_ = str_.split()
    ans = permuation(str_)

    print(ans)
    return ans

scramble("123")
