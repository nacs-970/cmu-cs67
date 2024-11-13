#!/usr/bin/env python3
# firstname lastname (nickname)
# 6xxxxxxxx
# HW04_2
# 204111 Sec 00B
# TA หรือ เพื่อนที่่ให้คำปรึกษา

def main():
    test_minute_diff()


# implement this function
def minute_diff(hour1, min1, period1, hour2, min2, period2):
    return 0


# test function
def test_minute_diff():
    assert(minute_diff(8, 23, "AM", 8, 24, "AM")) == 1
    assert(minute_diff(8, 23, "AM", 1, 24, "PM")) == 301
    assert(minute_diff(1, 24, "PM", 8, 23, "AM")) == 301


if __name__ == "__main__":
    main()
