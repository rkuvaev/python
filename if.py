# coding : utf-8

#Тестовая программа для определения четверти

x = int(input("Введите абциссу: \n"))
y = int(input("Введите ординату: \n"))

if x > 0 and y > 0:
    print("Номер вашей четверти #1")
elif x > 0 and y < 0:
    print("Номер вашей четверти #4")
elif x < 0 and y > 0:
    print("Номер вашей четверти #2")
elif x < 0 and y > 0:
    print("Номер вашей четверти #3")
elif x == 0 and y != 0:
    print("Точка принадлежит оси абцисс")
elif x != 0 and y == 0:
    print("Точка принадлежит оси ординат")
else:
    print("Точка находится в начале координат")

input()
