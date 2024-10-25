money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
 # Текущие состояние подушки безопасности
while True:
    i = money_capital + salary # Бюджет
    if i >= spend: # Если бюджет больше расходов
        months +=1
        money_capital = i - spend # текущий капитал
        spend *= (1 + increase)
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)
