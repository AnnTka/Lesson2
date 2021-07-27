dict_eng_to_rus = {
    "apple": "яблоко",
    "house": "дом",
}

# перевод слова засчет вытягивания
dict_rus_to_eng = {
    # в какой вид мы хотим привести
    value: key
    # возврат парами в список
    for key, value in dict_eng_to_rus.items()
}


def from_eng_to_rus(eng):
    rus = dict_eng_to_rus[eng]
    return rus


from_eng_to_rus("apple")


def from_rus_to_eng(rus):
    eng = dict_eng_to_rus[rus]
    return eng


from_rus_to_eng("яблоко")
