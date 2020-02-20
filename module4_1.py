from sys import argv

zp, hour, rate_hour, bonus = argv

hour = float(hour); rate_hour = float(rate_hour); bonus = float(bonus)

print('Имя скрипта: ', zp); print('Выработка в часах: ', hour); print('Ставка в часах: ', rate_hour); print('Премия: ', bonus)

def zp(hour, rate_hour, bonus):
    return (hour * rate_hour) + bonus

print('Заработная плата сотрудника: ', zp(hour, rate_hour, bonus))

