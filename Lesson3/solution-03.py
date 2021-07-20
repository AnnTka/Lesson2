# Создать список из отдельных символов, преобразовать в строку, инвертировать и  вывести на печать:

list = ['s', 'l', 'l', 'i', 'k', 'S', 'e', 'M', 'h', 'c', 'a', 'e', 'T']

# sentence = "".join(reversed(list)) - мой вариант


list = list[::-1]

list_rev = "".join(list)
# "".join(map(str, list)) - можно так

print(list_rev)
