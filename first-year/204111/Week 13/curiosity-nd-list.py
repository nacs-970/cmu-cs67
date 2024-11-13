# row > | col v
print("- making 2d list-")
def make_2d_list(rows,cols,a = []):
    for row in range(rows):
        a += [[0] * cols]
    return a
a = make_2d_list(3,2)
print(a)
a[0][0] = 1; print(a)

print("- shallow copy avoid -")
a = [[0] * 2] * 3
print(a)
a[0][0] = 1; print(a)

print("- looping -")
a = [[2,3,5],[1,4,7]]
print("before: a=\n",a)
rows = len(a)
cols = len(a[0])

for row in range(rows):
    for col in range(cols):
        a[row][col] += 1

print("after: a=\n",a)

print("- deepcopy -")
import copy
a = [[1,2,3],[4,5,6]]
b = copy.copy(a)
c = copy.deepcopy(a)

print("before")
print(a)
print(b)
print(c)
a[0][1]
print("after")
print(a)
print(b)
print(c)

print("- deepcopy 2 -")
a = [[0]*2]*3
a[0][0] = 1
print("a =",a)
b = [[0]*2]*3
c = copy.deepcopy(b)
b[0][0] = 2
c[0][0] = 3
print("b =",b)
print("c =",c)

print('- accessing rows and cols -')
print('rows cheap')
a = [[1,2,3],[4,5,6]]
rowlist = a[1]
print(a)
print('cols expensive')
a = [[1,2,3],[4,5,6]]
colList = []
for i in range(len(a)):
    colList += [a[i][1]]
print(colList)

print("- non rectangular 2d -")
a = [[1,2,3],[4,5],[6],[7,8,9,10]]
rows = len(a)
for row in range(rows):
    cols = len(a[row])
    print("Row", row, "has", cols, "col:", end="")
    for col in range(cols):
        print(a[row][col], end = " ")
    print()
print("- map -")
scores = [['A',50,45],['B',48,36],['C',39,49]]
avg = list(map(lambda x: [x[0],sum(x[1:])/(len(x)-1)],scores))
print(avg)
print("- reduce -")
from functools import reduce
a = [[1,2,3],[4,5,6],[7,8,9]]
print("from",a)
a = reduce(lambda x,y: x + y, a)
print("to  ",a)
print("- 3d list -")
a = [ [[1,2],[3,4]], [[5,6,7],[8,9]], [[10]] ]
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print("a[%d][%d][%d] = %d" % (i,j,k,a[i][j][k]))
        print("___")
print("- unzip / transpose -")
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
b = list(zip(*a))
print(b)
c = list(zip(*b))
print(c)
