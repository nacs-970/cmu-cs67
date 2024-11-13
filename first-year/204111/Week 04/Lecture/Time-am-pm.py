def main():
    test_time()
def twelve_hr_time(hr:int, mins:int) -> str:
    tm = "am"
    if hr == 12:
        tm = "pm"
    elif hr == 0:
        hr += 12
        tm = "am"
    elif hr > 12:
        if hr == 24:
            tm = "am"
            hr = 12
    else:
        tm = "pm"
        hr = hr%12
    return f"{hr:02}:{mins:02} {tm}"

def test_time():
    assert(twelve_hr_time(8,30)) == "8:30 am"
    assert(twelve_hr_time(20,30)) == "8:30 pm"
    assert(twelve_hr_time(12,00)) == "12:00 pm"
    assert(twelve_hr_time(24,00)) == "12:00 am"
    assert(twelve_hr_time(23,00)) == "11:00 pm"
    assert(twelve_hr_time(13,00)) == "01:00 pm"
    assert(twelve_hr_time(0,0)) == "12:00 am"
if __name__ == "__main__":
  main()