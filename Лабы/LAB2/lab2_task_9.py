salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


# TODO Оформить решение
def life(increase, salary=5000, spend=6000):
    need_money = 0
    for i in range(10):
        if i >= 1:
            spend = spend + spend * increase
        sum = spend - salary
        need_money += sum
    return need_money

need_money = life(increase)

print(round(need_money))
