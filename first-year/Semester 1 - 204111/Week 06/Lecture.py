def count_8(start:int,stop:int):
    r = range(start,stop+1)
    count = filter(lambda x: "8" in str(x), r)
    #print(count) #filter is an object
    return len(list(count))

def vowel_count(text:str):
    text = text.lower()
    result = list(filter(lambda x: text[x] in ['a','e','i','o','u'],range(len(text))))
    return len(result)

def vowel_count2(text:str):
    text = text.lower()
    #result = list(filter(lambda x: x in ['a','e','i','o','u'],text))
    result = list(filter(lambda x: x in 'aeiou',list(text)))
    print(len(result))
    return len(result)

def comparing():
    list_a = [1,3,5,6]
    list_b = [1.0001,3.0001,5.0001,6.9999]
    e = 10**-3
    from math import isclose
    result = list(map(lambda a,b: isclose(a,b,abs_tol=e),list_a,list_b))
    print("List : ",result)
    print("All : ",all(result))
    print("Any : ",any(result))
    
if __name__ == "__main__":
    count_8(300,800)
    vowel_count2("abcedfghijk")
    comparing()