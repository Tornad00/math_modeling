a = float(input('длина первого отрезка: '))
b = float(input('длина второго отрезка: '))
c = float(input('длина третьего отрезка: '))

if a == b and b == c and a == c:
  print('Равносторонний')

elif a == b or b ==c or c == a:
  print('Равнобедеренный')

elif a != b and a != c and b != c:
  print('Разносторонний')

else:
  print('Треугольник не существует')