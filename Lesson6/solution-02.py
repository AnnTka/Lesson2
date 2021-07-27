import math

group1 = int(input("Количество учащихся первой группы = "))
group2 = int(input("Количество учащихся второй группы = "))
group3 = int(input("Количество учащихся третьей группы = "))


# Первый вариант:
groups = [group1, group2, group3]
desks = 0
for el in groups:
    # делим количество учащихся на два места за партой и округляем в бОльшую сторону:
    desks += math.ceil(el/2)
print("Количество парт для закупки(1) - " + str(desks))


# Второй вариант:
groups = sum([math.ceil(i/2) for i in groups])
print("Количество парт для закупки(2) - " + str(groups))
