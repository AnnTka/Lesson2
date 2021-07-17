# Рассчитать итоговую сумму на вкладе:

deposit = 2130  # рублей
deposit_time = 5  # лет
interest_rate = 10  # %

# Начисление в конце каждого года:
bonus = 120  # рублей


for i in range(deposit_time):
    deposit = deposit + (deposit / interest_rate) + bonus

print('На счету ' + str(deposit) + ' рублей')
