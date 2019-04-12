"""
Написать функцию is_year_leap, принимающую 1 аргумент — год,
и возвращающую True, если год високосный, и False иначе.
"""

a = int(input())
if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
    print("True")
else:
    print("False")
