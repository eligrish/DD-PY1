salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
current_spend = spend
for current_cup in range (1, months + 1):
    current_cup = current_spend - salary
    current_spend = current_spend * (increase + 1)
    need_money += current_cup
# TODO Оформить решение

print(round(need_money))
