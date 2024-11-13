#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# HW15_1
# 204111 Sec 002

def manga_add(manga_shelf: list[tuple[str, int]], new_m:tuple[str, int], show_steps: bool = False) -> None:
    #manga_shelf[:] = sorted(manga_shelf,key = lambda x: x[1])
    #manga_shelf[:] = sorted(manga_shelf,key = lambda x: x[0])
    lo = 0; hi = len(manga_shelf) - 1
    key_name = new_m[0]; key_value = new_m[1]
    if not manga_shelf:
        manga_shelf.append(new_m)
        return
    while lo <= hi:
        mid = (lo + hi)//2
        if show_steps:
            print(f"[{mid}] {manga_shelf[mid]}")
        #print(manga_shelf[lo],manga_shelf[mid], manga_shelf[hi])
        
        # find the right position
        if key_name == manga_shelf[mid][0]:
            if key_value < manga_shelf[mid][1]:hi = mid - 1
            else: lo = mid + 1
            
        elif key_name < manga_shelf[mid][0]:hi = mid - 1
        else:lo = mid + 1
    
    # insert new book into shelf
    final = manga_shelf[mid]
    if key_name < final[0]:
        manga_shelf.insert(mid,new_m)
    elif key_name > final[0]:
        manga_shelf.insert(mid+1,new_m)
    else:
        if key_value <= final[1]:
            manga_shelf.insert(mid,new_m)
        else:
            manga_shelf.insert(mid+1,new_m)
            
    manga_shelf[:] = manga_shelf

if __name__ == "__main__":
    #shelf = [('Bleach', 10), ('Naruto', 5), ('One Piece', 24)]
    #shelf = [('Bleach',10) ,('Bleach', 100), ('Bleach', 10000)]
    #shelf = [('Bleach', 100), ('Bleach', 10000)]
    #shelf = [('Bleach', 1), ('Bleach', 3), ('Bleach', 4)]
    shelf = []
    new = ("Naruto", 18)
    manga_add(shelf, new, True)
    print('--')
    print(shelf)
