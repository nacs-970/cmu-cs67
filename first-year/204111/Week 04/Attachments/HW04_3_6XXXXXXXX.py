#!/usr/bin/env python3
# firstname_lastname
# 6xxxxxxxx
# HW04_2
# 229223 Sec 00B

def main():
    test_is_overlapped()


def is_overlapped(l1: float, t1: float, w1: float, h1: float,
                  l2: float, t2: float, w2: float, h2: float) -> bool:
    return False


def test_is_overlapped():
    assert is_overlapped(10, 10, 50, 75, 30, 55, 60, 60) is True
    assert is_overlapped(10, 10, 50, 75, 70, 55, 60, 60) is False


if __name__ == "__main__":
    main()
