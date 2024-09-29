print("- linear search (unordered) -")
def linear_search(list_,key_):
    pos = 0; found = False
    while pos < len(list_) and not found:
        if list_[pos] == key_:
            found = True
        else:
            pos += 1
    #print(pos)
    return found

list_ = [1,2,32,8,17,19,42,13]
#list_ = [15,18,2,19,18,0,8,14,19,14]
print(linear_search(list_,18))
print(linear_search(list_,13))

print()

print("- linear search (ordered) -")
print("only consider element that lower than key")
def ordered_linear_search(list_,key_):
    pos = 0; found = False; stop = False
    while pos < len(list_) and not found and not stop:
        if list_[pos] == key_:
            found = True
        elif list_[pos] > key_:
            stop = True
        else:
            pos += 1
    print(pos)
    return found
list_ = [0,1,2,8,13,17,19,32,42]
#list_ = [3,5,6,8,11,12,14,15,17,18]
print(ordered_linear_search(list_,3))
print(ordered_linear_search(list_,13))

print()

print("- binary search -")
print("split half or bisection search (must be ordered)")
def binary_search(list_,key_):
    lo = 0; hi = len(list_) - 1; found = False
    while lo <= hi and not found:
        mid = (lo + hi)//2
        if key_ == list_[mid]:
            found = True
        elif key_ < list_[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return found
print(binary_search(list_,3))
print(binary_search(list_,13))

print("- insertion sort -")
print("start from left side and compare move lower to the left")
def insertion_sort(list_):
    size = len(list_); l = list_[:]
    for n in range(1,size):
        i = n
        while i > 0 and l[i] < l[i-1]:
            l[i],l[i-1] = l[i-1],l[i] # tuple swap
            i -= 1
    return l
list_ = [3,7,4,9,5,2,6,1]
print(insertion_sort(list_))

#print("- merge sort revisit not finish -")
#def merge_sort_recursive(list_):
#
#    index = len(list_)//2
#    left = list_[:index]; right = list_[index:]
#    merge_sort_recursive(left)
#    merge_sort_recursive(right)
#
#def merge_sort_iteration(list_):
#    index = len(list_)//2
#    list_a = list_[:index]; list_b = list_[index:]
#    len_a,len_b = len(list_a),len(list_b)
#    i,j = 0,0; ans = []
#    while i < len_a and j < len_b:
#        if list_a[i] < list_b[j]:
#            ans.append(list_a[i])
#            i += 1
#        else:
#            ans.append(list_b[j])
#            j += 1
#    if i < len_a:
#        ans.extend(list_a[i:])
#    if j < len_b:
#        ans.extend(list_b[j:])
#    return ans

#print(merge_sort_iteration(list_))
#print(merge_sort_recursive(list_))

print("- radix sort -")
print("Least Significant Digit: LSD")

def radix_sort_int(list_):
    max_ = len(str(max(list_)))
    list_ = list(map(lambda x: str(x).zfill(max_), list_))
    for i in range(-1,-(max_+1),-1):
        dict_ = dict(map(lambda x: (str(x),[]),range(10)))
        for j in list_:
            dict_[j[i]] += [j]
        list_ = [n for values in dict_ for n in dict_.get(values)]
    return list(map(int,list_))

list_ = [170,45,75,90,802,2,24]
print(radix_sort_int(list_))

def radix_sort_str(list_):
    import string
    max_ = max(list(map(len,list_)))
    list_ = list(map(lambda x: x + " "*(max_-len(x)), list_))
    for i in range(-1,-(max_+1),-1):
        dict_ = dict(map(lambda x: (str(x),[])," " + string.ascii_letters))
        for j in list_:
            dict_[j[i]] += [j]
        list_ = [n for values in dict_ for n in dict_.get(values)]

    return list(map(str.strip,list_))

list_ = ["Caterpillar","Ant","Cat","Batman","Bat"]
#list_ = ["bat","ant","beer","rum","wine","candy"]
print(radix_sort_str(list_))

print()
print("Most Significant Digit: MSD")

def radix_sort_int(list_):
    max_ = len(str(max(list_)))
    list_ = list(map(lambda x: str(x).zfill(max_), list_))
    for i in range(max_):
        dict_ = dict(map(lambda x: (str(x),[]),range(10)))
        for j in list_:
            dict_[j[i]] += [j]
        list_ = [n for values in dict_ for n in dict_.get(values)]
    return list(map(int,list_))

list_ = [170,45,75,90,802,2,24]
#list_ = range(1,11)
print(radix_sort_int(list_))

def radix_sort_str(list_):
    import string
    max_ = max(list(map(len,list_)))
    list_ = list(map(lambda x: x + " "*(max_-len(x)), list_))
    for i in range(max_):
        dict_ = dict(map(lambda x: (str(x),[])," " + string.ascii_letters))
        for j in list_:
            dict_[j[i]] += [j]
        list_ = [n for values in dict_ for n in dict_.get(values)]

    return list(map(str.strip,list_))

list_ = ["Caterpillar","Ant","Cat","Batman","Bat"]
#list_ = ["bat","ant","beer","rum","wine","candy"]
print(radix_sort_str(list_))
