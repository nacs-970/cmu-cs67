def display_calendar(month: int, year: int) -> None:
    # Dictionary for days in each month
    dict_m = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # Adjust for the Gregorian calendar (January and February are treated as months 13 and 14 of the previous year)
    dict_gergor = {1: 13, 2: 14, 3: 3, 4: 4, 5: 5, 6: 6, 
                   7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12}
    # Days of the week
    dict_none = {0: 6, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
    
    def leap_year(y: int) -> int:  # Check if the year is a leap year
        return 1 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 0

    # Determine the number of days in the month
    days = dict_m[month]
    if month == 2:
        days += leap_year(year)

    # Determine the day of the week the month starts on
    k = year % 100
    j = year // 100
    h = (1 + ((13 * (dict_gergor[month] + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    # h = day of the week for the 1st of the month
    # where 0 = Saturday, 1 = Sunday, ..., 6 = Friday

    # Adjust for the alignment of days in the calendar
    l_day = ["  " for _ in range(dict_none[h])] + [f"{d:2}" for d in range(1, days + 1)]

    # Print the calendar header
    print("Su Mo Tu We Th Fr Sa")

    # Print the days of the month in the correct format
    for i in range(0, len(l_day), 7):
        print(" ".join(l_day[i:i+7]))

# Example usage
display_calendar(1, 2023)
display_calendar(2, 2023)

