# Not finish yet
def same_letters(str1: str, str2: str) -> bool:
    str1,str2 = str1.lower(),str2.lower()
    str1 = list(filter(lambda x: x.isalpha(), str1))
    str2 = list(filter(lambda x: x.isalpha(), str2))

    def check(list_a,list_b):
        if list_a == []:return True
        if list_a[0] in list_b:
            replace(list_b,list_a[0],'',count=1)
            return check(list_a[1:],list_b)
        else: return False

    return check(str1,str2)
same_letters('gs','Sg')
