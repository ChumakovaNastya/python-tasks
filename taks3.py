"""
Написать функцию season, принимающую
1 аргумент — номер месяца (от 1 до 12),
 и возвращающую время года,
 которому этот месяц принадлежит
  (зима, весна, лето или осень).
"""
a = int(input())
if a == 1 or a == 2 or a == 12:
    print("зима")
elif a == 3 or a == 4 or a == 5:
    print("весна")
elif a == 5 or a == 7 or a == 8:
    print("лето")
elif a == 9 or a == 10 or a == 11:
    print("осень")
else:
    print("error")
