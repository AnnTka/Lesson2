import datetime
from datetime import datetime


def my_decorator(func):

    # количество параметров в () должно совпадать с основной ыункцией, но называть их необязательно
    def timer(year):
        # запоминаем время на начало работы программы:
        start_time = datetime.now()
        # вызываем нашу функцию:
        result = func(year)  # если вместо year написать год, то функция будет выдавать новый результат
        # запоминаем время на конец работы программы:
        end_time = datetime.now()
        # выводим за какое время сработала программа и вышел результат:
        print(end_time - start_time)
        # выводим результат функции
        return result

    return timer


@my_decorator
def filter_cars(year):
    car_list = [
        {"sn": 123, "color": "red", "year": 2005},
        {"sn": 456, "color": "yellow", "year": 2010},
        {"sn": 789, "color": "black", "year": 2015},
        {"sn": 147, "color": "black", "year": 2005},
        {"sn": 258, "color": "blue", "year": 1995},
    ]

    result = []
    for car in car_list:
        if car["year"] > year:
            result.append(car)
    return result


# решение через lambda:
# year = 2005
# filter(lambda x: ["year"] > year, car_list)


def main():
    year = 2000
    filtered_cars = filter_cars(year)
    print(filtered_cars)


if __name__ == "__main__":
    main()
