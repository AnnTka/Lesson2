# 1. Найти значение выражений:
x1 = 17 / 2 * 3 + 2
print(x1)
x2 = 2 + 17 / 2 * 3
print(x2)
x3 = 19 % 4 + 15 / 2 * 3
print(x3)
x4 = (15 + 6) - 10 * 4
print(x4)
x5 = 17 / 2 % 2 * 3
print(x5)


# 2. Расставить скобки так, чтобы значение выражений не поменялось:
x1 = 17 / 2 * 3 + 2
x1_new = (17 / 2) * 3 + 2
if x1 == x1_new:
    print(True)
x2 = 2 + 17 / 2 * 3
x2_new = 2 + (17 / 2 * 3)
if x2 == x2_new:
    print(True)
x3 = 19 % 4 + 15 / 2 * 3
x3_new = (19 % 4) + (15 / 2 * 3)
if x3 == x3_new:
    print(True)
x4 = (15 + 6) - 10 * 4
x4_new = (15 + 6) - (10 * 4)
if x4 == x4_new:
    print(True)
x5 = 17 / 2 % 2 * 3
x5_new = (17 / 2) % 2 * 3
if x5 == x5_new:
    print(True)


# 3. Найти сумму возрастов друзей:
age_dima = 21
age_jane = 23
age_vova = 18
summ_age = age_dima + age_vova + age_jane
print(summ_age)


# 4. Среднее арифметическое возраста друзей:
avg_age = summ_age / 3
print(avg_age)


# 5:
side_square = 10

# Список, содержащий периметр, площадь и диагональ квадрата соответственно:
new_list = [side_square * 4, side_square * side_square, (side_square ** 2 + side_square ** 2) ** 0.5]
print(new_list)


# 6. Найти в списке ниже количество не уникальных элементов:
my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]

# От общего кол-ва элементов в списке отнимаем кол-во уникальных элементов:
print((len(my_list)) - len(set(my_list)))


# 7. Из предыдущего списка извлечь с 2-го по 4-й символ в обратном порыдке:
list_my = my_list[1:4]
list_my.reverse()
print(list_my)
