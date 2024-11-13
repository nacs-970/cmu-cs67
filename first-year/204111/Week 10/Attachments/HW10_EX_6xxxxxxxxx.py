#!/usr/bin/env python3
# @Author: kk
# @Last Modified time: 2022-09-24 21:16:41

cat = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''


def main():
    print(cat_altar(int(input())))


def cat_altar(n):
    return cat*n


if __name__ == '__main__':
    main()
