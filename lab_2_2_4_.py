a = int(input("введлите натуральное число = "))

d = 1

while a >= d:
  d += 1
  j = 2

  while j < d:

    if d % j == 0:
      d += 1
      j = 2
    
    j += 1
  while a % d == 0:
    a = a // d
    print(d)