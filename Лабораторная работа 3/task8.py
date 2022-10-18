money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
sum = money_capital - spend
while sum > 0:
    sum = sum + salary - spend
    spend = 1.06*spend
    month += 1

print(month)
