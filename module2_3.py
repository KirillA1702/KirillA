months_by_season = {
  'зима': [12, 1, 2],
  'весна': [3, 4, 5],
  'лето': [6, 7, 8],
  'осень': [9, 10, 11]
}

num_month = int(input('Введите номер месяца: '))
answer = ''

for season in months_by_season:
  if num_month in months_by_season[season]:
      answer = season.capitalize()
      break
  else:
      answer = 'Не существует такого месяца!'

print(answer)
