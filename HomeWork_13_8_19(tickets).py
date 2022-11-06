n = int(input('количество билетов на мероприятие:  '))
sum = 0
for i in range(n):
  age = int(input('Возраст участника:  '))
  if age < 18:
    sum +=0
  elif 18 <= age <25:
    sum += 990
  else:
    sum += 1390
if n > 3:
  sum *= 0.9
print(f'Итоговая стоимость билетов {sum} руб')