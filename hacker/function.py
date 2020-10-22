"""
The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.
"""

def is_leap(year):
    leap = False
    
    if leap % 4 != 0:
        return leap
    elif leap%100 == 0 & leap%400 != 0:
        return leap
    else:
        leap = "WTF"
    
    return leap

year = 2001 # int(input())
print(is_leap(year))