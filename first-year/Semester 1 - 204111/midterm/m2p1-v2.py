# Not finish yet
import string
def same_letters(str1: str, str2: str) -> bool:
    str1 = list(filter(lambda x: x.isalpha(), str1.lower()))
    str2 = list(filter(lambda x: x.isalpha(), str2.lower()))
    count1 = list(map(lambda x: str1.count(x),string.ascii_lowercase))
    count2 = list(map(lambda x: str2.count(x),string.ascii_lowercase))
    ans = list(map(lambda x: count1[x] != 0 and count2[x] != 0,range(26)))
    return all(ans)

    def check(list_a,list_b):
        if list_a == []:return True
        #print(list_a[0])
        if list_a[0] not in list_b:return False
        return check(list_a[1:],list_b)

    return check(str1,str2) and check(str2,str2)

#print(same_letters('Hg','hxg'))
#print(same_letters('ksdJCVyrRqFnjrIGcmTpnHVmJgggKyQzMbkrrqbpeJaqPwrGjPpmeqqffySxbqCfbLYvUIWoUEYyplXZjmZQNheCNuDhcnYeg','BfysdwmrhdaptwJhsCepakwBscLWAVOlJXNztstXyuClqaPzFWaLNPOMGwFoYkgWbttKCIKrUXxuuizEsQFSXckkmDoUyLqmI'))
#print(same_letters('GAZrSMEVKnfkNxkvtIONCSvkjAfVXpXXqLaXuCiUjlKLExcgWBqNVjJTCqCGmmrWMXPPEauIVqBvLFsJqCnwPoXhLLGunx','vVVTIFXmCJYqdBqrqvtOzyIKNpmbWXNdcgNYWQIlzUMUJbvYVzMaYzOvvjhCnFiGOFkSGDaBgpjtKJnCezZLyaDZDhFBbJ'))
