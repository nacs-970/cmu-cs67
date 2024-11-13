#!/usr/bin/env python3
# ชื่อ นามสกุล ชื่อเล่น
# 6xxxxxxxx
# HW06_1
# 204111 Sec 00B
# ชื่อ TA หรือ เพื่อนที่ให้คำปรึกษา

def main():
    test_triangle()


def triangle(n):
    return ""


def test_triangle():

    T3 = '''*
*.*
* * *
'''

    T7 = '''*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * *
'''

    assert triangle(3) == T3
    assert triangle(7) == T7
    print("OK")


if __name__ == '__main__':
    main()
