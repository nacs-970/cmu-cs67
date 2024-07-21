#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW06_2
# 204111 Sec 002

def main():

    print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
'''))


def decode_helper(code_table, str_index):  # รับรหัส 1 ตัว แล้วคืน 1 อักขระที่ถูกต้อง
    if str_index == '.':
        return "\n"

    elif int(str_index) > len(code_table)-1 or int(str_index) < (-1)*(len(code_table)): # check out of range for code_table for both positive and negative int
        return "_"
    #elif int(str_index) <= len(code_table):
    else:
        return code_table[int(str_index)]


def decode(code_table, text):
    # แยกรหัสทั้งหมด ให้กลายเป็น list เช่น ['3', '.', '5', '3', '4', '2', '.', ...]
    l_text = text.split()

    # เรียกใช้ฟังก์ชัน decode_helper() ที่มีหน้าที่รับรหัสหนึ่งตัว แล้วคืน 1 อักขระที่ถูกต้อง
    result_list = list(map(lambda x: decode_helper(code_table, x), l_text))

    # รวม list ของอักขระ ให้เป็น string
    result = ''.join(result_list)
    return result


def test():
    assert (decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
-10 -1 -9 9 .
''')) == '''i
like
ice-crea_
_-a_
'''
    print("@ o @")

if __name__ == "__main__":
    test()
