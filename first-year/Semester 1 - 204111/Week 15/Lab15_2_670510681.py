#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# Lab15_2
# 204111 Sec 002

def unique_combo(heaps: list[tuple[str]]) -> set[tuple[str]]:
    # want a different pattern that in elements has no duping 
    set_ = [tuple(sorted(set(x))) for x in heaps]
    return set(set_)
if __name__ == "__main__":
    print(unique_combo([('red', 'green', 'blue', 'blue'), ('blue', 'green', 'red'), ('green', 'blue', 'red'), ('pink', 'purple', 'orange', 'pink'), ('orange', 'purple', 'pink')]))
