import random

people_without_gift = ["Ann", "Sid", "Kai", "Dmitriy", "Noi"]


def game(name):
    bool = True
    while bool:
        name_two = random.choice(people_without_gift)
        if name_two != name:
            bool = False
    people_without_gift.pop(people_without_gift.index(name_two))
    return f"{name} дарит подарок {name_two} "


friends = ["Ann", "Sid", "Kai", "Dmitriy", "Noi"]
for friend in friends:
    print(game(friend))
