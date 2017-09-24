# coding : utf-8

#Тестовое задание — расчёт дней, часов и минут

minutes = int(input("Введите количество минут: \n"))

days = minutes // (24 * 60)
hours = (minutes - days * 24 * 60) // 60
minutes = minutes - days * 24 * 60 - hours * 60

print(days, "дн.", hours, "ч.", minutes, "мин.")
