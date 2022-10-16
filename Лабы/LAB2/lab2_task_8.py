money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

# TODO Оформить решение

def life(increase, money_capital=10000, salary=5000, spend=6000):
    month = 0
    while money_capital >= 0:
        spend = spend + spend * increase
        money_capital = money_capital + salary - spend
        increase += 0.05
        if money_capital > 0:
            month += 1
    return month


month = life(increase)
print(month)
