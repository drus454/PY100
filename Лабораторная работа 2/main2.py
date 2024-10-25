salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

for months in range(months):
    if months >= 0:
        months += 1
        i = spend - salary
        spend *= (1 + increase)
        money_capital += i
money_capital = round(money_capital, 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",money_capital)
