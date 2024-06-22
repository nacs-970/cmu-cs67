#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab02_2
# 204111 Sec 002

import math
milli = int(input("Input miliseconds: "))
# // หารเอาผลไม่เอาเศษ | % หารเอาแค่เศษ
sec = milli // 1000 # ได้วินาทีมา
milli = milli % 1000 # เอาเศษมิลิ
mins = sec // 60 # แปลง วิ เป็นนาที
sec = sec % 60 # เอาเศษวิ
hour = mins // 60 # แปลงแนาทีเป็น ชม
mins = mins % 60 # เอาเศษนาที
day = hour // 24 # แปลง ชม เป็น วัน
hour = hour % 24 # เอาเศษวัน

print(f"{day} day(s), {hour} hour(s), {mins} minute(s), {sec} second(s), and {milli} millisec(s)")
