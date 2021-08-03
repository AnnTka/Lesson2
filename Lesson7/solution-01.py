countries_cities = {
    "Belarus": ["Minsk", "Borisov"],
    "Russia": ["Moscow", "Petersburg"],
    "Georgia": ["Tbilisi", "Batumi"],
    "France": ["Paris"]
}

city = input("Введите город: ")


# поиск города в словаре:
def search_city():
    for key, value in countries_cities.items():
        if city in value:
            print(key)


print(search_city())
