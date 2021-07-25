import random


def search_min_and_max(*args, **kwargs):
    func_type = kwargs["func_type"]
    args_sum = 0
    # if len(args) == 0:
    #     return
    max_el = 0  # Вместо 0 можно args[0] или is not None
    for element in args:
        if element > max_el:
            max_el = element
        args_sum += element
    return args_sum, max_el


random_elements = []
for _ in range(10):
    random_el = random.randint(1, 100)
    random_elements.append(random_el)

min_el = search_min_and_max(*random_elements, func_type="min")
print(min_el)

max_el = search_min_and_max(*random_elements, func_type="max")
print(max_el)
