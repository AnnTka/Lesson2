# Задание 1

def format_string(name):
    return f"Hello, {name}"


my_names = ["Ann", "Sid", "Kai", "Dima", "Noi"]

for my_name in my_names:
    # if my_name == "Ann": если конкретное имя выбираем
    my_string = format_string(my_name)
    print(my_string)

