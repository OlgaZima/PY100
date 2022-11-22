import random     # TODO написать функцию для получения списка уникальных целых чисел


def get_unique_list_numbers() -> list:
    list_random = []
    list_ = list(range(-10, 11))
    while len(list_random) < 15:
        list_choice = random.choice(list_)
        if list_choice not in list_random:
            list_random.append(list_choice)
    return list_random

# random sample() - позволит генерировать уникальные значения


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
