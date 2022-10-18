salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
need_money = spend - salary
i = 2
for k in range(i, months+1):
       spend = 1.03 * spend
       need_money = need_money + spend - salary
print(round(need_money))
