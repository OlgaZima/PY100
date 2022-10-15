list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
"""max_ = list_numbers[0]
pos = 0
for i in range(1, len(list_numbers)):
    if list_numbers[i] > max_:
        max_ = list_numbers[i]
        pos = i"""

pos = list_numbers.index(max(list_numbers))
list_numbers[pos], list_numbers[-1] = list_numbers[-1], list_numbers[pos]

print(list_numbers)
