#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec 002
def transform_id(int_id):
    int_id = str(int_id)
    year = int_id[:2]
    id = int_id[-3:]
    return f'{id}-{year}'
if __name__ == '__main__':
    assert transform_id(650241555) == '555-65'
    print("All OK!")
