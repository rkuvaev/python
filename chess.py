# coding : utf-8

#Программа для хода конём :)

import math

line_current = int(input("Введите номер строки (от 1 до 8), где находится конь: \n"))
row_current = int(input("Введите номер ряда (от 1 до 8), где находится конь: \n"))

line_target = int(input("Введите номер строки (от 1 до 8), куда хотите переместить фигуру: \n"))
row_target = int(input("Введите номер ряда (от 1 до 8), куда хотите переместить фигуру: \n"))

line_range = line_current - line_target
row_range = row_current - row_target

if abs(line_range) == 1 and abs(row_range) == 2:
    print("Поздравляем! Вы можете сделать ход в один ход ;)")
elif abs(line_range) == 2 and abs(row_range) == 1:
    print("Поздравляем! Вы можете сделать ход в один ход ;)")
else:
    print("К сожалению, за один ход не дойти :(")

print()
print("Чтобы выйти нажмите клавишу Enter")
input()